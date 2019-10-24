import unittest
import unitTest1


class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(unitTest1.add(10, 5), 15)
        self.assertEqual(unitTest1.add(1, -1), 0)
        self.assertEqual(unitTest1.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(unitTest1.subtract(10, 5), 5)
        self.assertEqual(unitTest1.subtract(1, -1), 2)
        self.assertEqual(unitTest1.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(unitTest1.multiply(10, 5), 50)
        self.assertEqual(unitTest1.multiply(1, -1), -1)
        self.assertEqual(unitTest1.multiply(-1, -1), 1)

    def test_devide(self):
        self.assertEqual(unitTest1.devide(10, 5), 2)
        self.assertEqual(unitTest1.devide(1, -1), -1)
        self.assertEqual(unitTest1.devide(-1, -1), 1)

        # self.assertRaises(ValueError,unitTest1.devide,10,0) #testing raises
        with self.assertRaises(ValueError):  # testing raises method 2
            unitTest1.devide(10, 0)


if __name__ == "__main__":
    unittest.main()
