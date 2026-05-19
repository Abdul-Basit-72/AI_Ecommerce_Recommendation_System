import unittest

def check_product_name(name):
    return len(name) > 0

def add_numbers(a, b):
    return a + b


class TestFunctions(unittest.TestCase):

    def test_product_name(self):
        self.assertTrue(check_product_name("iphone"))

    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()