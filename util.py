from trynumpy import numpy_distributions
from tryscipy import scipy_distributions


# get all distributions from numpy and scipy in a function
def distributions(size=10):
    npd = numpy_distributions(size)
    npd = {f'np_{k}': v for k, v in npd.items()}

    scipyd = scipy_distributions(size)
    scipyd = {f'scipy_stats_{k}': v for k, v in scipyd.items()}

    d = {**npd, **scipyd}

    # sort d by original key names (not np_ or scipy_stats_)
    d = {k: d[k] for k in sorted(d, key=lambda x: x.split('_')[-1])}

    return d
