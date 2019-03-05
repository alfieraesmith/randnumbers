from randomnumbers import NormalDistribution, BinomialDistribution, PoissonDistribution

# example of generating numbers from the Normal distribution using the NormalDistribution class
normal_distribution = NormalDistribution(mean=3, sd=3)
normal_numbers = normal_distribution.draw(sample_size=10)
normal_summary = normal_distribution.summarise()

# example of generating numbers from the Binomial distribution using the BinomialDistribution class
binomial_distribution = BinomialDistribution(n=10, p=0.1)
binomial_numbers = binomial_distribution.draw(sample_size=10)
binomial_summary = binomial_distribution.summarise()

# example of generating numbers from the Poisson distribution using the PoissonDistribution class
poisson_distribution = PoissonDistribution(lam=5)
poisson_numbers = poisson_distribution.draw(sample_size=10)
poisson_summary = poisson_distribution.summarise()
