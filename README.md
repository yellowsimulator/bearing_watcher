 This is a set of modules for vibration analysis. the main modules:

```
from bearing_watcher.demodulation import get_envelope_spectrum
```

```
from bearing_watcher.demodulation import get_fault_amplitude
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
fault_freq, fault_amp = get_fault_amplitude(frequency,
                                            ampplitude,
                                            fault_freq,
                                            error_threshold)
```
