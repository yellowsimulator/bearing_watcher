from demodulation import get_envelope_spectrum
from demodulation import get_peak, get_fft, get_cheby_band_pass_filtered_signal

import matplotlib.pyplot as plt
from glob import glob
import pandas as pd
import numpy as np

files = glob('vibration/*.parquet')
file = files[0]
df = pd.read_parquet(file)
data = df['sample'].values


def detect_rpm(input_signal: np.ndarray, 
               rpm_range: list = [32, 35],
               sampling_freq: int=20000):
    """
    Implemeting order tracking in order to estimate the RPM.

    Parameters:
    -----------
        input_signal: input signal
        rpm_range: range of RPM to be searched
        sampling_freq: sampling frequency, Hz
        error_threshold: threshold for the error in Hz

    Returns:
    --------
    rpm_freq: frequency of fault
    """
    low_cut, high_cut = rpm_range
    band_passed_signal = get_cheby_band_pass_filtered_signal(input_signal, low_cut,
                         high_cut, sampling_freq, order=5)

    _, freq, amps = get_fft(band_passed_signal)
    min_diff_idx = np.argmax(amps[:100])
    rpm_freq = freq[min_diff_idx]
    print(rpm_freq)
    plt.plot(freq[:100], amps[:100])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Detected RPM in Hz')
    plt.show()


detect_rpm(data)