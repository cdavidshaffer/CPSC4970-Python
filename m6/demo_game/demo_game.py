import random
import sys

import pygame
from pygame import key
from pygame.sprite import Sprite, Group, spritecollideany
from pygame.surface import Surface
from pygame.time import Clock

from m6.demo_game import settings


def wrap_world_rect(rect):
    """Modify rect so that it wraps around if its left side is less than zero or greater than the world width"""
    if rect.left < 0:
        rect.left += settings.WORLD_WIDTH
    if rect.left >= settings.WORLD_WIDTH:
        rect.left -= settings.WORLD_WIDTH


class Ground(Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.image = pygame.image.load("images/ground.png").convert()
        self.world_rect = self.image.get_rect().copy()
        self.world_rect.bottom = settings.WINDOW_HEIGHT
        assert self.world_rect.width == settings.WORLD_WIDTH


class Explosion(Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25)).convert()
        self.image.fill((0, 0, 200))
        self.world_rect = self.image.get_rect().move(x, y)

    def update(self, *args, **kwargs):
        pass


class Player(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.facing_right = pygame.transform.rotate(pygame.image.load("images/player.png").convert_alpha(), -90)
        self.facing_left = pygame.transform.rotate(self.facing_right, 180)
        self.image = self.facing_right
        self.world_rect = self.image.get_rect().move(0, 300)
        self.world_inset_rect = None
        self.update_inset()

    def update_inset(self):
        self.world_inset_rect = self.world_rect.inflate(-20, -20)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        wrap_world_rect(self.world_rect)
        self.update_inset()

    def move_left(self):
        self.world_rect.left -= 20
        self.image = self.facing_left

    def move_right(self):
        self.world_rect.left += 20
        self.image = self.facing_right


class BadGuy(Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Surface((25, 25)).convert()
        self.image.fill((255, 0, 0))
        self.world_rect = self.image.get_rect().move(x, y)

    def update(self):
        self.world_rect.move_ip(random.randint(-10, 10), random.randint(-10, 10))
        wrap_world_rect(self.world_rect)


class Viewport:
    def __init__(self):
        self.left = 0

    def update(self, sprite):
        self.left = sprite.world_rect.left - 300
        if self.left > settings.WORLD_WIDTH:
            self.left -= settings.WORLD_WIDTH
        if self.left < 0:
            self.left += settings.WORLD_WIDTH

    def compute_rect(self, group, dx=0):
        for sprite in group:
            sprite.rect = sprite.world_rect.move(-self.left + dx, 0)

    def draw_group(self, group, surface):
        self.compute_rect(group)
        group.draw(surface)
        self.compute_rect(group, settings.WORLD_WIDTH)
        group.draw(surface)


class Game:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Cool game")
        self.player = Player()
        self.player_group = Group()
        self.player_group.add(self.player)
        self.bad_guys = Group()
        for i in range(15):
            self.bad_guys.add(BadGuy(random.randrange(0, settings.WORLD_WIDTH),
                                     random.randrange(0, settings.WINDOW_HEIGHT)))
        self.static_sprites = Group()
        self.static_sprites.add(Ground())
        self.viewport = Viewport()
        self.viewport.update(self.player)

    def game_loop(self):
        clock = Clock()
        while True:
            self.handle_events()
            self.draw()
            self.update()
            pygame.display.flip()
            clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and event.mod == pygame.KMOD_LCTRL:
                    pass

    def update(self):
        self.player_group.update(key.get_pressed())
        self.bad_guys.update()
        self.viewport.update(self.player)
        self.check_collisions()

    def check_collision(self, player, bad_guy):
        return player.world_inset_rect.colliderect(bad_guy.world_rect)

    def check_collisions(self):
        if self.player.alive() and \
                (collided_with := spritecollideany(self.player, self.bad_guys, self.check_collision)) is not None:
            self.player.kill()
            collided_with.kill()
            self.player_group.add(Explosion(self.player.world_rect.left, self.player.world_rect.top))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.viewport.draw_group(self.static_sprites, self.screen)
        self.viewport.draw_group(self.player_group, self.screen)
        self.viewport.draw_group(self.bad_guys, self.screen)


if __name__ == '__main__':
    Game().game_loop()
