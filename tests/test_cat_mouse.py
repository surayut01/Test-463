from coe_number.cat_mouse import Cat_and_Mouse
import unittest

class CatMouseTest(unittest.TestCase):

    def test_cat_b(self):
        self.assertEqual(Cat_and_Mouse(1, 2, 3), "Cat B")
        self.assertEqual(Cat_and_Mouse(1, 5, 4), "Cat B")

    def test_mouse_c(self):
        self.assertEqual(Cat_and_Mouse(1, 3, 2), "Mouse C")
        self.assertEqual(Cat_and_Mouse(10, 20, 15), "Mouse C")
        self.assertEqual(Cat_and_Mouse(0, 0, 0), "Mouse C")
        self.assertEqual(Cat_and_Mouse(-5, -1, -3), "Mouse C")

    def test_cat_a(self):
        self.assertEqual(Cat_and_Mouse(4, 8, 5), "Cat A")

if __name__ == "__main__":
    unittest.main()
