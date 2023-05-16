import os
import numpy as np


def get_ims_data(experiment_number: int, bearing_number: int):
    """Return the data for a given experiment and bearing number.

    Note: The data is from the IMS bearing dataset.
    and it used to test this module.

    Parameters
    ----------
    experiment_number : The experiment number.
    bearing_number : The bearing number.

    Returns
    -------
    bearing_data : The data for the given experiment
                   and bearing number.
    """
    data_path = os.path.join('..', 'data', 'ims')
    experiment_number = 2
    file_mane = f'test{experiment_number}.npz'
    file_path = os.path.join(data_path, file_mane)
    data_object = np.load(file_path)
    data = data_object['data']
    bearing_data = data[..., bearing_number]
    return bearing_data