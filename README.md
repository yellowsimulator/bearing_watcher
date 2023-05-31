 This is a set of modules for vibration analysis. The main modules:

```
from bearing_watcher.demodulation import get_envelope_spectrum
```

```
from bearing_watcher.demodulation import get_peak
```

usage:

```
frequency, amplitudes = get_envelop_spectrum(input_signal,
                                              sampling_freq=20000,
                                              low_cut=2000,
                                              high_cut=9900,
                                              order=5)
```

For bearing fault detection you want to find the amplitude of a given fault (BPFO, BPFI, ...). for this purpose call

```
fault_frequency = 234.6 #BPFO
error_threshold = 0.5 # Hz
fault_freq, fault_amp = get_peak(frequency,
                                            ampplitude,
                                            fault_freq,
                                            error_threshold)
```

I've added a Dash app for you to experiment with. Please install the required dependencies and execute the 'app.py' file. The parquet files include vibration samples derived from a run to-failure experiment,which resulted in an outer race defect in the bearing after approximately the 537th sample.
