from randomnumbers import get_random_numbers

# example of generating numbers from the Normal distribution
normal_numbers_1 = get_random_numbers(sample_size=5, distribution="normal")
# increase sample size. Use a Normal dist with a larger mean and sd (default is mean=0, sd=2)
normal_numbers_2 = get_random_numbers(sample_size=10, distribution="normal", mean=3, sd=3)
# give me numbers to one decimal place
normal_numbers_3 = get_random_numbers(sample_size=10, digits=1, distribution="normal", mean=3, sd=3)

# example of generating numbers from the Binomial distribution
binomial_numbers_1 = get_random_numbers(sample_size=5, distribution="binomial")
# increase sample size. Use a Binomial dist with less trials for a less probable event (default is n=30, p=0.5)
binomial_numbers_2 = get_random_numbers(sample_size=10, distribution="binomial", n=10, p=0.1)
# give me numbers to one decimal place
binomial_numbers_3 = get_random_numbers(sample_size=10, digits=1, distribution="binomial", n=10, p=0.1)


# example for generating numbers from the Poisson distribution
poisson_numbers_1 = get_random_numbers(sample_size=5, distribution="poisson")
# increase sample size. Use a Poisson distribution with a larger expected events (default is lam=3)
poisson_numbers_2 = get_random_numbers(sample_size=10, distribution="poisson", lam=5)

