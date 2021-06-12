from shopping_cart import ShoppingCart
import unittest


class ShippingFake:
    @staticmethod
    def get_usps():
        return "usps"

    @staticmethod
    def get_ups():
        return "ups"

    @staticmethod
    def get_fedex():
        return "fedex"

    @staticmethod
    def get_independent():
        return "independent"


class StockItemFake:
    def __init__(self, unit_price, unit_weight=1):
        self.unit_price = unit_price
        self.unit_weight = unit_weight


class ShoppingCartTest(unittest.TestCase):

    def test_a_shopping_is_empty_when_first_created(self):
        """SPEC: a cart is empty when it is first created"""
        cart = ShoppingCart()
        some_item = "pickles"
        self.assertEqual(0, cart.get_total_item_count())
        self.assertEqual(0, cart.get_item_count(some_item))

    def test_adding_increases_occurrences(self):
        """SPEC: adding stock items increases the number of occurrences of the stock item in the cart"""
        cart = ShoppingCart()
        item_1 = "pickles"
        quantity_1_1 = 10
        quantity_1_2 = 30
        item_2 = "oranges"
        quantity_2 = 37
        cart.add_item(item_1, quantity_1_1)
        cart.add_item(item_2, quantity_2)
        cart.add_item(item_1, quantity_1_2)
        self.assertEqual(quantity_1_1 + quantity_1_2, cart.get_item_count(item_1))
        self.assertEqual(quantity_2, cart.get_item_count(item_2))
        self.assertEqual(quantity_1_1 + quantity_1_2 + quantity_2, cart.get_total_item_count())

    def test_removing_decreases_occurrences(self):
        """SPEC: removing a stock item decreases, possibly to zero, the number of occurrences of this stock item
         in the cart"""
        cart = ShoppingCart()
        item_1 = "pickles"
        quantity_1 = 10
        quantity_to_remove = 7
        cart.add_item(item_1, quantity_1)

        cart.remove_item(item_1, quantity_to_remove)

        self.assertEqual(quantity_1 - quantity_to_remove, cart.get_item_count(item_1))

    def test_removing_nonexistent_item_ignored(self):
        """SPEC: if there are fewer occurrences of the stock item than specified, ignore the request"""
        cart = ShoppingCart()
        item_1 = "pickles"
        cart.remove_item(item_1, 100)

        self.assertEqual(0, cart.get_item_count(item_1))

    def test_removing_too_many_ignored_ignored(self):
        """SPEC: if there are fewer occurrences of the stock item than specified, ignore the request"""
        cart = ShoppingCart()
        item_1 = "pickles"
        quantity_1 = 5
        cart.add_item(item_1, quantity_1)
        cart.remove_item(item_1, 100)

        self.assertEqual(quantity_1, cart.get_item_count(item_1))

    def test_compute_total_price_of_items_in_cart(self):
        """SPEC: compute the total of the prices of the items in the cart"""
        cart = ShoppingCart()
        unit_price_1 = 7
        item_1 = StockItemFake(unit_price_1)
        quantity_1_1 = 10
        quantity_1_2 = 30
        unit_price_2 = 3
        item_2 = StockItemFake(unit_price_2)
        quantity_2 = 37
        cart.add_item(item_1, quantity_1_1)
        cart.add_item(item_2, quantity_2)
        cart.add_item(item_1, quantity_1_2)

        self.assertEqual((quantity_1_1+quantity_1_2)*unit_price_1 + quantity_2*unit_price_2, cart.get_total_price())

    def test_compute_item_counts(self):
        """SPEC: get the list "item counts", that is, a list containing dictionaries with the following keys,values:
            item -- the item
            count -- the number of occurrences of an item in the cart, must be > 0
             line_price -- the price of count occurrences of item
        where no two elements of the list have the same item"""
        cart = ShoppingCart()
        unit_price_1 = 7
        item_1 = StockItemFake(unit_price_1)
        quantity_1_1 = 10
        quantity_1_2 = 30
        unit_price_2 = 3
        item_2 = StockItemFake(unit_price_2)
        quantity_2 = 37
        cart.add_item(item_1, quantity_1_1)
        cart.add_item(item_2, quantity_2)
        cart.add_item(item_1, quantity_1_2)

        item_counts = cart.get_item_counts()

        self.assertEqual(2, len(item_counts))
        item_1_d = item_counts[0] if item_counts[0]["item"] == item_1 else item_counts[1]
        self.assertEqual(quantity_1_1+quantity_1_2, item_1_d["count"])
        self.assertEqual((quantity_1_1+quantity_1_2)*item_1.unit_price, item_1_d["line_price"])
        item_2_d = item_counts[0] if item_counts[0]["item"] == item_2 else item_counts[1]
        self.assertEqual(quantity_2, item_2_d["count"])
        self.assertEqual(quantity_2*item_2.unit_price, item_2_d["line_price"])

    @staticmethod
    def cart_with_weight(weight):
        cart = ShoppingCart()
        unit_weight_1 = weight
        item_1 = StockItemFake(0, unit_weight_1)
        cart.add_item(item_1, 1)
        return cart

    def test_suggest_low_weight_shipping(self):
        """SPEC: suggest a shipping strategy based on the total weight of the items:
                less than one pound: US postal service
                greater than or equal to 1 pound and less than 200 pounds: UPS or FedEx
                greater than or equal to 200 pounds: independent freight contractor"""
        cart = self.cart_with_weight(0.5)

        shipping = cart.suggest_shipping(ShippingFake)

        self.assertEqual(1, len(shipping))
        self.assertEqual(ShippingFake.get_usps(), shipping[0])


    def test_suggest_mid_weight_shipping(self):
        """SPEC: suggest a shipping strategy based on the total weight of the items:
                less than one pound: US postal service
                greater than or equal to 1 pound and less than 200 pounds: UPS or FedEx
                greater than or equal to 200 pounds: independent freight contractor"""
        cart = self.cart_with_weight(50)

        shipping = cart.suggest_shipping(ShippingFake)

        self.assertEqual(2, len(shipping))
        self.assertIn(ShippingFake.get_ups(), shipping)
        self.assertIn(ShippingFake.get_fedex(), shipping)

    def test_suggest_high_weight_shipping(self):
        """SPEC: suggest a shipping strategy based on the total weight of the items:
                less than one pound: US postal service
                greater than or equal to 1 pound and less than 200 pounds: UPS or FedEx
                greater than or equal to 200 pounds: independent freight contractor"""
        cart = self.cart_with_weight(500)

        shipping = cart.suggest_shipping(ShippingFake)

        self.assertEqual(1, len(shipping))
        self.assertIn(ShippingFake.get_independent(), shipping)
