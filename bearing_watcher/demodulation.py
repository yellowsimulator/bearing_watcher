import numpy as np
from typing import Union
from scipy.fftpack import hilbert
from scipy.signal import butter, lfilter
from scipy import signal
import scipy
from scipy import integrate
import matplotlib.pyplot as plt
from cheby_filters import get_cheby_band_pass_filtered_signal
from cheby_filters import get_cheby_low_pass_filtered_signal


def get_signal_envelop(input_signal: np.ndarray) -> np.ndarray:
    """Returns the envelop of a signal.

    Parameters:
    -----------
    input_signal: input signal to be enveloped

    Returns:
    --------
    envelop: envelop of the input signal

    Usage:
    ------
    >>> envelop = get_signal_envelop(input_signal)
    """
    hilbert_transform = scipy.signal.hilbert(input_signal)
    envelop = np.sqrt(input_signal**2 +
              hilbert_transform**2)
    return envelop


def get_fft(input_signal: np.ndarray) -> Union[np.ndarray, np.ndarray]:
    """Returns the frequency and the FFT amplitude of a signal.

    Parameters:
    -----------
    signal: input signal

    Returns:
    --------
    frequency: Frequencies of the FFT
    amplitudes: Amplitudes of the FFT

    Usage:
    ------
    >>> frequency, amplitudes = get_fft(input_signal)
    """
    signal_fft = scipy.fftpack.fft(input_signal)
    N = len(input_signal)
    frequencies = np.fft.fftfreq(N, d=1./N)
    frequencies_resized = frequencies[: N//2]
    amplitude = (np.abs(signal_fft[: N//2]) / N)
    return signal_fft, frequencies_resized, amplitude


def get_envelope_spectrum(input_signal: np.ndarray,
                          sampling_freq: int=20000,
                          low_cut: int=2000,
                          high_cut: int=9900,
                          order: int=5) -> Union[np.ndarray, np.ndarray]:
    """Returns the envelope spectrum of a signal.
    Performs:
    1 - band pass filter
    2 - Hilbert transform to get the envelop
    3 - low pass filter
    4 - FFT

    Parameters:
    -----------
    input_signal: input signal
    sampling_freq: sampling frequency, Hz
    low_cut: low cutoff frequency, Hz
    high_cut: high cutoff frequency, Hz
    order: order of the filter

    Returns:
    --------
    frequency: Frequencies of the FFT
    amplitudes: Amplitudes of the FFT

    Usage:
    ------
    >>> frequency, amplitudes = get_envelope_spectrum(input_signal) # default values
    """
    band_passed_signal = get_cheby_band_pass_filtered_signal(input_signal, low_cut,
                         high_cut, sampling_freq, order)
    envelop = get_signal_envelop(band_passed_signal)
    low_passed_signal = get_cheby_low_pass_filtered_signal(envelop, low_cut, sampling_freq, order)
    _, freq, amplitude = get_fft(low_passed_signal)
    return freq, amplitude


def get_fault_amplitude(freqs: np.ndarray,
                        amps: np.ndarray,
                        fault_freq: float,
                        error_threshold: float):
    """
    Returns the amplitude of the fault frequency.

    Parameters:
    ----------
    freqs: Frequency spectrum
    amps: corrsponding amplitudes
    ffault_freqt: theoretical fault frequency
    error_threshold: threshold for the error in Hz

    Returns:
    ----------
    fault_freq: frequency of fault
    fault_amplitude: amplitude of fault frequency
    """
    differences = np.abs(freqs - fault_freq)
    min_diff_idx = np.argmin(differences)
    if differences[min_diff_idx] <= error_threshold:
        return freqs[min_diff_idx], amps[min_diff_idx]
    return None


if __name__ == '__main__':
    ...


