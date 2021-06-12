class ShoppingCart:
    def __init__(self):
        self._items = {}

    def get_total_item_count(self):
        return sum(self._items.values())

    def get_item_count(self, item):
        return self._items[item] if item in self._items else 0

    def add_item(self, item, quantity):
        self._items[item] = self.get_item_count(item) + quantity

    def remove_item(self, item_to_remove, quantity_to_remove):
        if self.get_item_count(item_to_remove) >= quantity_to_remove:
            self._items[item_to_remove] = self.get_item_count(item_to_remove) - quantity_to_remove

    def get_total_price(self):
        return sum([item.unit_price*quantity for item, quantity in self._items.items()])

    def get_item_counts(self):
        return [{"item": item, "count": quantity, "line_price": item.unit_price*quantity} for item,quantity in
                self._items.items()]

    def _get_total_weight(self):
        return sum([item.unit_weight * quantity for item, quantity in self._items.items()])

    def suggest_shipping(self, shipping_factory):
        weight = self._get_total_weight()
        if weight < 1:
            return [shipping_factory.get_usps()]
        elif weight < 200:
            return [shipping_factory.get_ups(), shipping_factory.get_fedex()]
        else:
            return [shipping_factory.get_independent()]