import unittest
import my_function_example

class Test(unittest.TestCase):

    # set up
    def setUp(self):
        #This is a setup function that gets run before each test, we won't use it.
        pass

    #tests
    def test_prime_1(self): #This is an individual test
        self.assertEqual(my_function_example.is_prime(2), True)
        self.assertEqual(my_function_example.is_prime(4), False)

    def test_prime_2(self):
        self.assertEqual(my_function_example.is_prime(7), True)
        self.assertEqual(my_function_example.is_prime(9), False)

    def test_even_1(self):
        self.assertEqual(my_function_example.is_even(1), False)
        self.assertEqual(my_function_example.is_even(2), True)

    # clean up
    def tearDown(self):
        #This is a teardown function that gets run after each test, we won't use it.
        pass

if __name__ == '__main__':
    unittest.main()
