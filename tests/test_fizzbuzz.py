from coe_number.fizzbuzz import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_return_fizz(self):
        result = FizzBuzz(3)
        self.assertEqual(result, "Fizz", "3 should return 'Fizz'")

    def test_give_5_should_return_buzz(self):
        result = FizzBuzz(5)
        self.assertEqual(result, "Buzz", "5 should return 'Buzz'")

    def test_give_15_should_return_fizzbuzz(self):
        result = FizzBuzz(15)
        self.assertEqual(result, "FizzBuzz", "15 should return 'FizzBuzz'")

    def test_give_2_should_return_2(self):
        result = FizzBuzz(2)
        self.assertEqual(result, "2", "2 should return '2'")

    def test_give_0_should_return_fizzbuzz(self):
        result = FizzBuzz(0)
        self.assertEqual(result, "FizzBuzz", "0 is divisible by 3 and 5")

    def test_give_negative_15_should_return_fizzbuzz(self):
        result = FizzBuzz(-15)
        self.assertEqual(result, "FizzBuzz", "-15 should return 'FizzBuzz'")