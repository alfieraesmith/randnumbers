import unittest
from randomnumbers import NormalDistribution, BinomialDistribution, PoissonDistribution
import numpy as np


class TestNormalDistribution(unittest.TestCase):

    def setUp(self):
        self.normal_distribution = NormalDistribution(mean=5, sd=1)

    def tearDown(self):
        self.normal_distribution = None

    def test_draw_output_size(self):
        normal_sample = self.normal_distribution.draw(size=10)
        self.assertIs(len(normal_sample), 10)

    def test_draw_output_type(self):
        normal_sample = self.normal_distribution.draw(size=10)
        self.assertIsInstance(normal_sample, np.array(1).__class__)

    def test_draw_state_update(self):
        normal_sample = self.normal_distribution.draw(size=10)
        self.assertIs(self.normal_distribution.current_sample, normal_sample)

    def test_draw_output_digits(self):
        normal_sample = self.normal_distribution.draw(size=10, digits=8)
        rounded_normal_sample = [round(value, 5) for value in normal_sample]

        # If samples are already rounded to 5 dp, then lists should be the same
        self.assertAlmostEqual(sum(normal_sample), sum(rounded_normal_sample), places=3)

    def test_distribution_mean(self):
        normal_sample = self.normal_distribution.draw(size=10000000)
        self.assertAlmostEqual(np.mean(normal_sample), 5, places=3)

    # please see ReadMe.MD for why there is no test_summarise method


class TestBinomialDistribution(unittest.TestCase):

    def setUp(self):
        self.binomial_distribution = BinomialDistribution(p=0.3, n=100)

    def tearDown(self):
        self.binomial_distribution = None

    def test_draw_output_size(self):
        normal_sample = self.binomial_distribution.draw(size=10)
        self.assertIs(len(normal_sample), 10)

    def test_draw_output_type(self):
        normal_sample = self.binomial_distribution.draw(size=10)
        self.assertIsInstance(normal_sample, np.array(1).__class__)

    def test_draw_state_update(self):
        normal_sample = self.binomial_distribution.draw(size=10)
        self.assertIs(self.binomial_distribution.current_sample, normal_sample)

    def test_draw_output_digits(self):
        normal_sample = self.binomial_distribution.draw(size=10, digits=8)
        rounded_normal_sample = [round(value, 5) for value in normal_sample]

        # If samples are already rounded to 5 dp, then lists should be the same
        # almost equal to deal with any floating point issues
        self.assertAlmostEqual(sum(normal_sample), sum(rounded_normal_sample), places=3)


class TestPoissonDistribution(unittest.TestCase):

    def setUp(self):
        self.poisson_distribution = PoissonDistribution(mean=5, sd=1)

    def tearDown(self):
        self.poisson_distribution = None

    def test_draw_output_size(self):
        normal_sample = self.poisson_distribution.draw(size=10)
        self.assertIs(len(normal_sample), 10)

    def test_draw_output_type(self):
        normal_sample = self.poisson_distribution.draw(size=10)
        self.assertIsInstance(normal_sample, np.array(1).__class__)

    def test_draw_state_update(self):
        normal_sample = self.poisson_distribution.draw(size=10)
        self.assertIs(self.poisson_distribution.current_sample, normal_sample)

    def test_draw_output_digits(self):
        normal_sample = self.poisson_distribution.draw(size=10, digits=8)
        rounded_normal_sample = [round(value, 5) for value in normal_sample]

        # If samples are already rounded to 5 dp, then lists should be the same
        self.assertAlmostEqual(sum(normal_sample), sum(rounded_normal_sample), places=3)


if __name__ == '__main__':
    unittest.main()
