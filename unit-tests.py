import unittest
from task1 import binary_bubble_sort
from task2 import Fibonacci_再帰, Fibonacci_サイクル
from task3 import task三_二十五
from task4 import количество


class TestBinaryBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        binary_bubble_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = ['0b101']
        binary_bubble_sort(arr)
        self.assertEqual(arr, ['0b101'])

    def test_already_sorted(self):
        arr = ['0b1', '0b10', '0b11', '0b100']
        expected = ['0b1', '0b10', '0b11', '0b100']
        binary_bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_reverse_sorted(self):
        arr = ['0b100', '0b11', '0b10', '0b1']
        expected = ['0b1', '0b10', '0b11', '0b100']
        binary_bubble_sort(arr)
        self.assertEqual(arr, expected)

    def test_with_duplicates(self):
        arr = ['0b101', '0b10', '0b101', '0b1', '0b10']
        expected = ['0b1', '0b10', '0b10', '0b101', '0b101']
        binary_bubble_sort(arr)
        self.assertEqual(arr, expected)

class TestFibonacciRecursive(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(Fibonacci_再帰(0), 0)

    def test_first(self):
        self.assertEqual(Fibonacci_再帰(1), 1)

    def test_second(self):
        self.assertEqual(Fibonacci_再帰(2), 1)

    def test_fifth(self):
        self.assertEqual(Fibonacci_再帰(5), 5)

    def test_tenth(self):
        self.assertEqual(Fibonacci_再帰(10), 55)

class TestFibonacciCycle(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(Fibonacci_サイクル(0), 0)

    def test_first(self):
        self.assertEqual(Fibonacci_サイクル(1), 1)

    def test_second(self):
        self.assertEqual(Fibonacci_サイクル(2), 1)

    def test_fifth(self):
        self.assertEqual(Fibonacci_サイクル(5), 5)

    def test_tenth(self):
        self.assertEqual(Fibonacci_サイクル(10), 55)


class TestTask3(unittest.TestCase):
    def test_m0_n100(self):
        self.assertEqual(task三_二十五(0, 100), [])

    def test_m1_n20(self):
        self.assertEqual(task三_二十五(1, 20), [1, 10])

    def test_m4_n100(self):
        self.assertEqual(task三_二十五(4, 100), [2, 11, 20])

    def test_m9_n100(self):
        self.assertEqual(task三_二十五(9, 100), [3, 12, 21, 30])

    def test_m25_n1000(self):
        expected = [5, 14, 23, 32, 41, 50, 104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500]
        self.assertEqual(task三_二十五(25, 1000), expected)


class TestRainMarch(unittest.TestCase):
    def test_exactly_10(self):
        rain = [0]*10 + [1]*21
        self.assertTrue(количество(rain))

    def test_less_than_10(self):
        rain = [0]*5 + [2]*26
        self.assertFalse(количество(rain))

    def test_more_than_10(self):
        rain = [0]*15 + [3]*16
        self.assertFalse(количество(rain))

    def test_all_days_with_rain(self):
        rain = [5]*31
        self.assertFalse(количество(rain))

    def test_all_days_no_rain(self):
        rain = [0]*31
        self.assertFalse(количество(rain))


if __name__ == '__main__':
    unittest.main()