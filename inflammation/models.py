"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array.

    :param data: A 2D array with inflammation data (each row contains measurements for a single patient across all days)
    :returns: An array of mean values of measurements for each day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily maximum of a 2d inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimum of a 2d inflammation data array for each day.

    :param data: A 2D data array with inflammation data (each row contains measurements for a single patient across all days).
    """
    return np.min(data, axis=0)

def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2d array of inflammation data
    :type data: ndarray

    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('inflammation values should be non-negative')
    max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    return normalised

# TODO(lesson-design) Add Patient class


class Patient:
    def __init__(self, name, observations=None):
        self.name = name
        if observations is None:
            self.observations = []
        else:
            self.observations = observations

    def add_observation(self, infl_m):
        self.observations.append(infl_m)

    def display_patient(patient):
        """Display data for a single patient."""
        print(patient.name)
        print(patient.observations)

class Doctor:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.patients_name = []

    def add_patient(self, name, observations):
        new_patient = Patient(name,observations)

        self.patients.append(new_patient)
        self.patients_name.append(new_patient.name)
        return new_patient

    def __str__(self):
        return self.name

    def patient_list(self):
        return self.patients_name

# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
