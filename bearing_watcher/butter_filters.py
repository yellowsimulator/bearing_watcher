import scipy
import numpy as np
import matplotlib.pyplot as plt

def butter_band_pass_coefficient(low_cut: float, high_cut: float,
                                 fs: float, order: int=5) -> np.ndarray:
    """Returns Butterworth bandpass filter coefficients.

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
    nyq = 0.5 * fs
    low = low_cut / nyq
    high = high_cut / nyq
    sos = scipy.signal.butter(N=order, Wn=[low, high],
          analog=False, btype='band', output='sos')
    return sos


def butter_low_pass_coefficient(low_cut: float, fs: float,
                                order: int=5) -> np.ndarray:
    """Returns Butterworth lowpass filter coefficients.

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
    nyq = 0.5 * fs
    low = low_cut / nyq
    sos = scipy.signal.butter(N=order, Wn=low,
          analog=False, btype='low', output='sos')
    return sos


def butter_high_pass_coefficient(high_cut: float, fs: float,
                                 order: int=5) -> np.ndarray:
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
    nyq = 0.5 * fs
    high = high_cut / nyq
    sos = scipy.signal.butter(N=order,Wn=high,
          analog=False, btype='high', output='sos')
    return sos


def get_butter_band_pass_filtered_signal(input_signal: np.ndarray,
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
    >>> filtered_signal = get_butter_band_pass_filtered_signal(input_signal,
    >>>                                        low_cut, high_cut, fs, order)
    """
    sos = butter_band_pass_coefficient(low_cut, high_cut, fs, order=order)
    filtered_signal = scipy.signal.sosfilt(sos, input_signal)
    return filtered_signal


def get_butter_low_pass_filtered_signal(input_signal: np.ndarray,
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
    >>> filtered_signal = get_low_pass_filtered_signal(input_signal, low_cut, fs, order)
    """
    sos = butter_low_pass_coefficient(low_cut, fs, order=order)
    filtered_signal = scipy.signal.sosfilt(sos, input_signal)
    return filtered_signal


def get_butter_high_pass_filtered_signal(input_signal: np.ndarray,
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
    >>> filtered_signal = get_butter_high_pass_filtered_signal(input_signal, high_cut, fs, order)
    """
    sos = butter_high_pass_coefficient(high_cut, fs, order=order)
    filtered_signal = scipy.signal.sosfilt(sos, input_signal)
    return filtered_signal


if __name__ == '__main__':
    fs = 5000.0
    low_cut = 500.0
    high_cut = 1250.0
    for order in [2, 3, 14, 15, 20]:
        sos = butter_band_pass_coefficient(low_cut, high_cut, fs=fs, order=order)
        w, h = scipy.signal.sosfreqz(sos, worN=2000)
        plt.plot(w, abs(h), label=f"order = {order}" )
    plt.legend(loc='best')
    plt.show()
