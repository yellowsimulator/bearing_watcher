import scipy
import numpy as np
from scipy.signal import butter, sosfilt, sosfreqz, sosfiltfilt
import matplotlib.pyplot as plt

def cheby_band_pass(low_cut: float, high_cut: float,
                    fs: float, order: int=5) -> np.ndarray:
    """Returns Chebycheve bandpass filter coefficients.

    Parameters
    ----------
    lowcut : Lower cutoff frequency. Hz
    highcut : Upper cutoff frequency. Hz
    fs : Sampling frequency. Hz
    order : optional. Order of the filter. Default is 5.

    Returns
    -------
    sos : ndarray
        Second-order sections representation of the filter.
    """
    # nyq = 0.5 * fs
    # low = low_cut / nyq
    # high = high_cut / nyq
    sos = scipy.signal.cheby1(N=order, rp=1, Wn=[low_cut, high_cut],
          analog=False, btype='band', output='sos', fs=fs)
    return sos


def cheby_low_pass(low_cut: float, fs: float, order: int=5) -> np.ndarray:
    """Returns lowpass filter coefficients.

    Parameters
    ----------
    lowcut : Lower cutoff frequency. Hz
    fs : Sampling frequency. Hz
    order : optional. Order of the filter. Default is 5.

    Returns
    -------
    sos : ndarray
        Second-order sections representation of the filter.
    """
    # nyq = 0.5 * fs
    # low = low_cut / nyq
    sos = scipy.signal.cheby1(N=order, rp=1, Wn=low_cut,
          analog=False, btype='low', output='sos', fs=fs)
    return sos


def cheby_high_pass(high_cut: float, fs: float, order: int=5) -> np.ndarray:
    """Returns highpass filter coefficients.

    Parameters
    ----------
    lowcut : Lower cutoff frequency. Hz
    fs : Sampling frequency. Hz
    order : optional. Order of the filter. Default is 5.

    Returns
    -------
    sos : ndarray
        Second-order sections representation of the filter.
    """
    sos = scipy.signal.cheby1(N=order, rp=1, Wn=high_cut, btype='hp',
          fs=fs, output='sos')
    return sos


def get_cheby_band_pass_filtered_signal(input_signal: np.ndarray,
                                        low_cut: float, high_cut: float,
                                        fs, order=5) -> np.ndarray:
    """
    Applies bandpass filter to input signal.

    Parameters
    ----------
    input_signal : Input signal.
    low_cut : Lower cutoff frequency. Hz
    high_cut : Upper cutoff frequency. Hz
    fs : Sampling frequency. Hz
    order : optional. Order of the filter. Default is 5.

    Returns
    -------
    filtered_signal : ndarray
        Filtered signal.

    Usage
    -----
    >>> from filters import get_band_pass_filtered_signal
    >>> fs = 1000
    >>> low_cut = 10
    >>> high_cut = 100
    >>> order = 5
    >>> t = np.linspace(0, 1, fs, endpoint=False)
    >>> input_signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
    >>> filtered_signal = get_cheby_band_pass_filtered_signal(input_signal, low_cut, high_cut, fs, order)
    """
    sos = cheby_band_pass(low_cut, high_cut, fs, order=order)
    filtered_signal = sosfilt(sos, input_signal)
    return filtered_signal


def get_cheby_low_pass_filtered_signal(input_signal: np.ndarray,
                                       low_cut: float,
                                       fs, order=5) -> np.ndarray:
    """
    Applies lowpass filter to input signal.

    Parameters
    ----------
    input_signal : Input signal.
    low_cut : Lower cutoff frequency. Hz
    fs : Sampling frequency. Hz
    order : optional. Order of the filter. Default is 5.

    Returns
    -------
    filtered_signal : ndarray
        Filtered signal.

    Usage
    -----
    >>> from filters import get_low_pass_filtered_signal
    >>> fs = 1000
    >>> low_cut = 10
    >>> order = 5
    >>> t = np.linspace(0, 1, fs, endpoint=False)
    >>> input_signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
    >>> filtered_signal = get_cheby_low_pass_filtered_signal(input_signal, low_cut, fs, order)
    """
    sos = cheby_low_pass(low_cut, fs, order=order)
    filtered_signal = sosfilt(sos, input_signal)
    return filtered_signal


def get_cheby_high_pass_filtered_signal(input_signal: np.ndarray,
                                        high_cut: float,
                                        fs, order=5) -> np.ndarray:
    """
    Applies highpass filter to input signal.

    Parameters
    ----------
    input_signal : Input signal.
    high_cut : Upper cutoff frequency. Hz
    fs : Sampling frequency. Hz
    order : optional. Order of the filter. Default is 5.

    Returns
    -------
    filtered_signal : ndarray
        Filtered signal.

    Usage
    -----
    >>> from filters import get_high_pass_filtered_signal
    >>> fs = 1000
    >>> high_cut = 100
    >>> order = 5
    >>> t = np.linspace(0, 1, fs, endpoint=False)
    >>> input_signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
    >>> filtered_signal = get_cheby_high_pass_filtered_signal(input_signal, high_cut, fs, order)
    """
    sos = cheby_high_pass(high_cut, fs, order=order)
    filtered_signal = sosfilt(sos, input_signal)
    return filtered_signal


if __name__ == '__main__':
    fs = 5000.0
    low_cut = 500.0
    high_cut = 1250.0
    for order in [2, 3, 14, 15, 20]:
        sos = cheby_band_pass(low_cut, high_cut, fs=fs, order=order)
        w, h = sosfreqz(sos, worN=2000)
        plt.plot(w, abs(h), label=f"order = {order}" )
    plt.legend(loc='best')
    plt.show()
