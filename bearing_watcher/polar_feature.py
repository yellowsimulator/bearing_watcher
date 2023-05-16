import numpy as np

from demodulation import get_envelope_spectrum



def get_polar_feature(freqs: np.ndarray, amps: np.ndarray):
    """Returns the polar representation
       of a frequency spectrum for a vibration signal
    """

    freq, amplitude = get_envelope_spectrum(freqs, amps)
    angular_freq = [2*np.pi*f for f in freq[2:1000]]