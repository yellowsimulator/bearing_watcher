import scipy
from glob import glob
import pandas as pd
import numpy as np
from fitter import Fitter
from scipy.stats import norm
import re
import matplotlib.pyplot as plt
import pymc3 as pm

from demodulation import get_envelope_spectrum, get_peak



def signal_to_noise(a, axis=0, ddof=0):
    """
    The signal-to-noise ratio of the input data.

    Returns the signal-to-noise ratio of `a`, here defined as the mean
    divided by the standard deviation.

    Parameters
    ----------
    a : array_like
        An array_like object containing the sample data.
    axis : int or None, optional
        If axis is equal to None, the array is first ravel'd. If axis is an
        integer, this is the axis over which to operate. Default is 0.
    ddof : int, optional
        Degrees of freedom correction for standard deviation. Default is 0.

    Returns
    -------
    The signal noise ratio

    Notes
    -----
    This is not a robust statistic. and should not be used yet.
    Need to think about other robust way of calculating the signal to noise ratio.
    Used just for testing purposes.
    """
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return abs(np.where(sd == 0, 0, sd/m))


def bayasian_testing(data: list, alpha_prior: float, beta_prior: float):
    """Performs a bayesian hypothesis testing.

    - Likelihood: Bernoulli
    - Prior: Beta
    - Beta and Bernoulli are conjugate distributions

    Parameters:
    -----------
        data: the data to be tested
        alpha_prior: alpha prior
        beta_prior: beta prior

    Returns:
    --------
        None.
    """
    with pm.Model() as model:
        prior = pm.Beta('prior', alpha=alpha_prior, beta=beta_prior)
        likelihood = pm.Bernoulli('likelihood', p=prior, observed=data)
        trace = pm.sample(2000)
        pm.plot_posterior(trace)
        #plt.savefig(f'distribution/{k}.png')
        #plt.show()



if __name__=="__main__":
    ...
        