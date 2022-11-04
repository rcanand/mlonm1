import scipy
import scipy.stats

# get all scipy stats distributions in a function
def scipy_distributions(size=10):
    # return dictionary of distributions
    d = {
        'beta': scipy.stats.beta.rvs(10, 10, size=size),
        'bernoulli': scipy.stats.bernoulli.rvs(0.5, size=size),
        'binom': scipy.stats.binom.rvs(10, 0.5, size=size),
        'chi2': scipy.stats.chi2.rvs(10, size=size),
        'expon': scipy.stats.expon.rvs(10, size=size),
        'gamma': scipy.stats.gamma.rvs(10, 10, size=size),
        'geom': scipy.stats.geom.rvs(0.3, size=size),
        'gumbel_l': scipy.stats.gumbel_l.rvs(10, 10, size=size),
        'hypergeom': scipy.stats.hypergeom.rvs(10, 10, 10, size=size),
        'laplace': scipy.stats.laplace.rvs(10, 10, size=size),
        'logistic': scipy.stats.logistic.rvs(10, 10, size=size),
        'lognorm': scipy.stats.lognorm.rvs(10, 10, size=size),
        'logser': scipy.stats.logser.rvs(0.5, size=size),
        'nbinom': scipy.stats.nbinom.rvs(10, 0.3, size=size),
        'norm': scipy.stats.norm.rvs(0, 1, size=size),
        'pareto': scipy.stats.pareto.rvs(10, size=size),
        'poisson': scipy.stats.poisson.rvs(10, size=size),
        'powerlaw': scipy.stats.powerlaw.rvs(10, size=size),
        'rayleigh': scipy.stats.rayleigh.rvs(10, size=size),
        'uniform': scipy.stats.uniform.rvs(0, 1, size=size),
        'vonmises': scipy.stats.vonmises.rvs(10, 10, size=size),
        'wald': scipy.stats.wald.rvs(10, 10, size=size),
        'weibull_min': scipy.stats.weibull_min.rvs(10, size=size),
        'zipf': scipy.stats.zipf.rvs(10, size=size),
    }
    
    return d


# main
if __name__ == '__main__':
    # get distributions
    d = scipy_distributions()
    print(d)
    
    # print distributions
    for k, v in d.items():
        print(k, v)