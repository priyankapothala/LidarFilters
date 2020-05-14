import numpy as np


class RangeFilter:
    def __init__(self, range_min=0.03, range_max=50):
        """
        Construstor for initializing the range filter object
        """
        self.__range_min = range_min
        self.__range_max = range_max
        self.__check_range()

    def __check_range(self):
        """Checks if the range_min and range_max values are valid
        Raises ValueError
        """
        if self.__range_min < 0:
            error_msg = "Min range cannot be less than 0"
            raise ValueError(error_msg)
        elif self.__range_max < 0:
            error_msg = "Max range cannot be less than 0"
            raise ValueError(error_msg)
        elif self.__range_max <= self.__range_min:
            error_msg = "Max range cannot be lesser than Min range"
            raise ValueError(error_msg)

    def update(self, arr):
        """
        Input: Array of measurements

        Replaces the array values less than range_min with range_min and 
        the values greater than range_max with range_max
        """
        return [self.__range_min if i < self.__range_min else self.__range_max if i > self.__range_max else i for i in arr]


class TemporalMedianFilter:
    __history = []  # array to store previous D scans

    def __init__(self, D=3):
        """
        Input: D(# previous scans to consider)
        Creates a TemporalMedianFilter object
        """
        self.__D = D
        self.__is_valid()

    def __is_valid(self):
        """Checks if the # previous scans D is valid
        Raises ValueError
        """
        if not isinstance(self.__D, int):
            error_msg = "D has to be a valid integer >= 0"
            raise ValueError(error_msg)

        if self.__D < 0:
            error_msg = "D cannot be less than 0"
            raise ValueError(error_msg)

    def update(self, arr):
        """
        Input: Array of measurements
        Returns the median of the current and previous D scan
        """

        # If the history is empty return the input array
        if len(self.__history) == 0:
            # save the length of measurements in N
            self.__N = len(arr)
            self.__history = np.array([arr])
            return arr

        if self.__N != len(arr):
            error_msg = "Inconsistent length of measurements in current scan"
            raise ValueError(error_msg)

        # If the history contains more scans than D, remove the oldest entry
        if len(self.__history) > self.__D:
            self.__history = np.delete(self.__history, (0), axis=0)

        # Add the new entry to history
        self.__history = np.append(self.__history, [arr], axis=0)

        # Calculate the median of the previou scans and the current scan
        return [np.median(self.__history[:, i]) for i in range(len(arr))]
