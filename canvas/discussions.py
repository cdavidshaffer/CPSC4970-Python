import keyring
from canvasapi import Canvas


def main():
    c = Canvas("https://auburn.instructure.com", keyring.get_password("canvasapi", "shaffer"))
    course = c.get_course(1340489)
    for t in course.get_discussion_topics():
        print(f"{t.title}:  {t.read_state}, {t.unread_count} unread follow-ups, {t.html_url}")
        #print(dir(t))


if __name__ == '__main__':
    main()
