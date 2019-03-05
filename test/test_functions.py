import unittest
from randomnumbers.functions import get_random_numbers
import numpy as np


class TestGetRandomNumbers(unittest.TestCase):

    def test_output_size(self):
        normal_sample = get_random_numbers(distribution="normal", sample_size=10)
        binomial_sample = get_random_numbers(distribution="binomial", sample_size=10)
        poisson_sample = get_random_numbers(distribution="poisson", sample_size=10)

        self.assertIs(len(normal_sample), 10)
        self.assertIs(len(binomial_sample), 10)
        self.assertIs(len(poisson_sample), 10)

    def test_output_type(self):
        normal_sample = get_random_numbers(distribution="normal", sample_size=10)
        binomial_sample = get_random_numbers(distribution="binomial", sample_size=10)
        poisson_sample = get_random_numbers(distribution="poisson", sample_size=10)

        self.assertIsInstance(normal_sample, np.array(1).__class__)
        self.assertIsInstance(binomial_sample, np.array(1).__class__)
        self.assertIsInstance(poisson_sample, np.array(1).__class__)

    def test_output_decimal_places(self):
        normal_sample = get_random_numbers(distribution="normal", sample_size=5, digits=5)
        binomial_sample = get_random_numbers(distribution="binomial", sample_size=5, digits=5)
        poisson_sample = get_random_numbers(distribution="poisson", sample_size=5, digits=5)

        rounded_normal_sample = [round(value, 5) for value in normal_sample]
        rounded_binomial_sample = [round(value, 5) for value in binomial_sample]
        rounded_poisson_sample = [round(value, 5) for value in poisson_sample]

        # If samples are already rounded to 5 dp, then lists should be the same
        self.assertEqual(sum(normal_sample), sum(rounded_normal_sample))
        self.assertEqual(sum(binomial_sample), sum(rounded_binomial_sample))
        self.assertEqual(sum(poisson_sample), sum(rounded_poisson_sample))

    def test_normal_mean(self):
        # if sample large enough, sample mean should approx equal distribution mean
        # increased allowed dp to 20 to prevent any rounding errors
        normal_sample = get_random_numbers(distribution="normal", sample_size=10000000, digits=10, mean=2)
        self.assertAlmostEqual(np.mean(normal_sample), 2, places=3)


if __name__ == '__main__':
    unittest.main()