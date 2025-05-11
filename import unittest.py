
import unittest
# Removed invalid import line
from cDrinkspr1 import Drink, Food, Order
`                       
class TestDrink(unittest.TestCase):
    def test_initialization(self):
        drink = Drink("medium")
        self.assertEqual(drink.get_base(), None)
        self.assertEqual(drink.get_flavors(), [])
        self.assertEqual(drink.get_total(), 1.75)

    def test_set_base(self):
        drink = Drink("small")
        drink.set_base("milk")
        self.assertEqual(drink.get_base(), "milk")
        with self.assertRaises(ValueError):
            drink.set_base("invalid_base")

    def test_add_flavor(self):
        drink = Drink("large")
        drink.add_flavor("vanilla")
        self.assertIn("vanilla", drink.get_flavors())
        self.assertEqual(drink.get_total(), 2.20)  # 2.05 + 0.15
        with self.assertRaises(ValueError):
            drink.add_flavor("invalid_flavor")

    def test_set_flavors(self):
        drink = Drink("small")
        drink.set_flavors(["vanilla", "coconut"])
        self.assertEqual(set(drink.get_flavors()), {"vanilla", "coconut"})
        self.assertEqual(drink.get_total(), 1.80)  # 1.50 + 0.15 * 2
        with self.assertRaises(ValueError):
            drink.set_flavors(["vanilla", "invalid_flavor"])

    def test_set_size(self):
        drink = Drink("small")
        drink.set_size("large")
        self.assertEqual(drink.get_total(), 2.05)
        with self.assertRaises(ValueError):
            drink.set_size("invalid_size")

    def test_str_representation(self):
        drink = Drink("medium")
        drink.set_base("coffee")
        drink.add_flavor("lemon")
        self.assertEqual(
            str(drink),
            "Drink: Size - medium, Base - coffee, Flavors - lemon, Cost: $1.90"
        )

class TestFood(unittest.TestCase):
    def test_initialization(self):
        food = Food("eggroll")
        self.assertEqual(food.get_type(), "eggroll")
        self.assertEqual(food.get_toppings(), [])
        self.assertEqual(food.get_total_price(), 2.30)

    def test_add_topping(self):
        food = Food("ice cream")
        food.add_topping("cherry")
        self.assertIn("cherry", food.get_toppings())
        self.assertEqual(food.get_total_price(), 2.30)  # 2.00 + 0.00
        with self.assertRaises(ValueError):
            food.add_topping("invalid_topping")

class TestOrder(unittest.TestCase):
    def test_add_item(self):
        order = Order()
        drink = Drink("small")
        food = Food("french fries")
        order.add_item(drink)
        order.add_item(food)
        self.assertEqual(len(order.get_items()), 2)

    def test_remove_item(self):
        order = Order()
        drink = Drink("small")
        food = Food("french fries")
        order.add_item(drink)
        order.add_item(food)
        order.remove_item(0)
        self.assertEqual(len(order.get_items()), 1)
        with self.assertRaises(IndexError):
            order.remove_item(5)

    def test_get_receipt(self):
        order = Order()
        drink = Drink("medium")
        drink.set_base("coffee")
        drink.add_flavor("lemon")
        food = Food("onion rings")
        food.add_topping("chili")
        order.add_item(drink)
        order.add_item(food)
        receipt = order.get_receipt()
        self.assertIn("Drink 1: Base - coffee, Flavors - lemon, Price: $1.90", receipt)
        self.assertIn("Food 2: Type - onion rings, Toppings - chili, Price: $1.85", receipt)

if __name__ == "__main__":
    unittest.main()
    