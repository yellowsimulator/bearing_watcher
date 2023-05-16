
# Bearing fault detection module

# Install requirements
`pip3 install scipy ` <br>
`pip3 install numpy` <br>
`pip3 install matplotlib`

# Data
If you have received to ims.zip file do this: <br>
1 - creeate a folder called data in the folder bearing_watcher. <br>
2 - unzip the file ims.zip inside the data folder that you just created <br>
the file `test1.npz`, `test2.npz` and `test3.npz` contains data for
experiment 1, experiment 2 and experiment 3 for the IMS bearing data as multidimension data. <br>

## Access the data
1 - Access the multidimensional array in experiment 2 <br>
`import numpy as np` <br>
`data_object = np.load('test2.npz)`  <br>
`data_array = data_object['data']` <br>
`print(data_array.shape)`

2 - Access bearing data <br>
In experiment 2 we have 4 bearings. To access for example
bearing number 1 data you will run: <br>
`channel = 0` <br>
`bearing_data = data_array[..., channel]` <br>
`print(bearing_data.shape)` <br>

To access the sample 3 and plot you will write: <br>
`sample_number = 3` <br>
`sample_data = bearing_data[sample_number, ...]` <br>
`import matplotlib.pyplot as plt` <br>
`plt.plot(sample_data)` <br>
`plt.show()`



# Test some code.
To test the peak finder module, run the file test_peak_finder.py
