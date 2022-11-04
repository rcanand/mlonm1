import numpy as np


def numpy_distributions(size=10):
    # return dictionary of distributions
    d = {
        'beta': np.random.beta(10, 10, size),
        'binomial': np.random.binomial(10, 0.5, size),
        'chisquare': np.random.chisquare(10, size),
        'exponential': np.random.exponential(10, size),
        'gamma': np.random.gamma(10, 10, size),
        'geometric': np.random.geometric(0.3, size),
        'gumbel': np.random.gumbel(10, 10, size),
        'hypergeometric': np.random.hypergeometric(10, 10, 10, size),
        'laplace': np.random.laplace(10, 10, size),
        'logistic': np.random.logistic(10, 10, size),
        'lognormal': np.random.lognormal(10, 10, size),
        'logseries': np.random.logseries(0.5, size),
        'negative_binomial': np.random.negative_binomial(10, 0.3, size),
        'normal': np.random.normal(0, 1, size),
        'pareto': np.random.pareto(10, size),
        'poisson': np.random.poisson(10, size),
        'power': np.random.power(10, size),
        'rayleigh': np.random.rayleigh(10, size),
        'uniform': np.random.uniform(0, 1, size),
        'vonmises': np.random.vonmises(10, 10, size),
        'wald': np.random.wald(10, 10, size),
        'weibull': np.random.weibull(10, size),
        'zipf': np.random.zipf(10, size),
    }
    
    return d


# main
if __name__ == '__main__':
    # get numpy distributions
    d = numpy_distributions()
    print(d)
    
    # print distributions
    for k, v in d.items():
        print(k, v)


# # get a random number from every distribution in numpy
# print('beta:', np.random.beta(10, 10, 10))
# print('binomial:', np.random.binomial(10, 0.5, 10))
# print('chisquare:', np.random.chisquare(10, 10))
# print('exponential:', np.random.exponential(10, 10))
# print('gamma:', np.random.gamma(10, 10, 10))
# print('geometric:', np.random.geometric(0.3, 10))
# print('gumbel:', np.random.gumbel(10, 10, 10))
# print('hypergeometric:', np.random.hypergeometric(10, 10, 10, 10))
# print('laplace:', np.random.laplace(10, 10, 10))
# print('logistic:', np.random.logistic(10, 10, 10))
# print('lognormal:', np.random.lognormal(10, 10, 10))
# print('logseries:', np.random.logseries(0.5, 10))
# print('negative_binomial:', np.random.negative_binomial(10, 0.3, 10))
# print('normal:', np.random.normal(0, 1, 10))
# print('pareto:', np.random.pareto(10, 10))
# print('poisson:', np.random.poisson(10, 10))
# print('power:', np.random.power(10, 10))
# print('rayleigh:', np.random.rayleigh(10, 10))
# # print('rdist:', np.random.rdist(10, 10)) - should be scipy.stats.rdist
# # print('rice:', np.random.rice(10, 10)) - should be scipy.stats.rice
# # print('semicircular:', np.random.semicircular(10, 10)) - could be scipy.stats.semicircular
# # print('t:', np.random.t(10, 10)) - could be scipy.stats.t
# # print('triangular:', np.random.triangular(10, 10, 10, 10)) - could be scipy.stats.triangular
# # print('truncexpon:', np.random.truncexpon(10, 10, 10)) - could be scipy.stats.truncexpon
# # print('truncnorm:', np.random.truncnorm(10, 10, 10, 10)) - could be scipy.stats.truncnorm
# print('uniform:', np.random.uniform(0, 1, 10))
# print('vonmises:', np.random.vonmises(10, 10, 10))
# print('wald:', np.random.wald(10, 10, 10))
# # print('wavelet:', np.random.wavelet(10, 10, 10)) - could be scipy.stats.wavelet
# print('weibull:', np.random.weibull(10, 10))
# print('zipf:', np.random.zipf(10, 10))
