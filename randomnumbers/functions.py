import numpy as np
import logging
from randomnumbers.constants import normal, binomial, poisson, default_digits


def get_random_numbers(sample_size, distribution, digits=default_digits, **kwargs):
    """
    Finds and returns an array of numbers of length "sample size" taken from
    *distribution" at random. Additional key values for generating a specific distribution
    can be supplied to constrain pool of random numbers selected from.

    :param sample_size:  int, how many numbers to return, equivalent to length of array [] to return
    :param digits: int, the number of decimal places allowed for returned random values.
    :param distribution: str, "poisson", name of probability distribution used to select numbers.
    :param kwargs: keyword arguments passed to and parsed by number generator helper functions.
                   each number generator looks for the key values relevant to its distribution (mean, p, n, lambda)
    :return: array of random integers, e.g. [1, 6, 3, 5], of length sampl_size.
    """
    if distribution.lower() in normal:
        return numbers_from_normal_dist(sample_size, digits, **kwargs)
    elif distribution.lower() in binomial:
        return numbers_from_binomial_dist(sample_size, digits, **kwargs)
    elif distribution.lower() in poisson:
        return numbers_from_poisson_dist(sample_size, digits, **kwargs)
    else:
        logging.error("Distribution {} is not currently supported"
                      "Please supply either: normal, poisson or binomial".format(distribution))
        return []


def numbers_from_normal_dist(sample_size, digits, **kwargs):
    """
    Generate a normal distribution and retrieve "sample_size" values, at random,
    from said distribution.
    If "mean" or "sd"/"spread" supplied as kwargs, normal distribution will
    be generated using this mean and/or standard deviation

    :param sample_size: integer, number of values from normal distribution to return.
    :param digits: integer, max number of decimal places for returned values
    :param kwargs: key-value dict, only "mean"/"sd"/"spread" currently searched for.
    :return: array of ints, [1, 2,3,4] drawn at random from normal dist.
    """
    if kwargs.get("mean", None) is not None:
        mean = kwargs.get("mean")
    else:
        mean = 0

    if kwargs.get("sd", None) is not None:
        sd = kwargs.get("sd")
    elif kwargs.get("spread", None) is not None:
        sd = kwargs.get("spread")
    else:
        sd = 2

    return np.around(np.random.normal(mean, sd, sample_size), digits)


def numbers_from_binomial_dist(sample_size, digits, **kwargs):
    """
    Generate a binomial distribution and retrieve "sample_size" values, at random,
    from said distribution.
    If "prob"/"p" or "n/"trials" supplied in kwargs, binomial distribution will
    be generated using this probability of X and/or number of trials.

    :param sample_size: integer, number of values from binomial distribution to return.
    :param digits: integer, max number of decimal places for returned values
    :param kwargs: key-value dict, only "prob/p/n/trials" currently searched for.
    :return: array of ints, [1, 2,3,4] drawn at random from binomial dist.
    """
    if kwargs.get("p") is not None:
        p = kwargs.get("p")
    elif kwargs.get("prob") is not None:
        p = kwargs.get("prob")
    else:
        p = 0.5

    if kwargs.get("n") is not None:
        n = kwargs.get("n")
    elif kwargs.get("trials") is not None:
        n = kwargs.get("trials")
    else:
        n = 50

    return np.around(np.random.binomial(n, p, sample_size), digits)


def numbers_from_poisson_dist(sample_size, digits, **kwargs):
    """
    Generate a poisson distribution and retrieve "sample_size" values, at random,
    from said distribution.
    If "lam"/"lambda" supplied in kwargs, poisson distribution will
    be generated using this value as the expected value of X within time period.

    :param sample_size: integer, number of values from poisson distribution to return.
    :param digits: integer, max number of decimal places for returned values
    :param kwargs: key-value dict, only "lam/lambda" currently searched for.
    :return: array of ints, [1, 2,3,4] drawn at random from poisson dist.
    """

    if kwargs.get("lam") is not None:
        lam = kwargs.get("lam")
    elif kwargs.get("lambda") is not None:
        lam = kwargs.get("lambda")
    else:
        lam = 3
    return np.around(np.random.poisson(lam, sample_size), digits)



