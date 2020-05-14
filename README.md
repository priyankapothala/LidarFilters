# LIDAR Sensor

The LIDAR Sensor genererates scans at a certain rate and each scan is an array of length N of float values representing distance measurements. N is typically in the range of ~[200, 1000] measurements. Measured distances are typically in the range of [0.03,50] meteres. Each time a scan is received, it will be passed on to the filters.

## RangeFilter

### Usage

RangeFilter constructor takes range_min and range_max values as parameters. The default values for range_min and range_max are 0.03 and 50 respectively

```python
filter = RangeFilter(0.03,50)
```

### Description

- RangeFilter constructor checks if the range_min and range_max parameters are valid and creates an object. If the values are not valid it raises a *ValueError*
- The **update** method in RangeFilter takes a list of measurements as input and checks if all measurements are within the valid range
- It replaces all the values that are below range_min with range_min value and those above the range_max with range_max value
  
## TemporalMedianFilter

### Usage

TemporalMedianFilter constructor takes # previous scans D as parameter. The default value for D is 3.

```python
filter = TemporalMedianFilter(3)
```

### Description

- The TemporalMedianFilter return the median of the current and previous D scans
- TemporalMedianFilter constructor checks if the parameter D(# previous scans) is valid and creates the filter object
- The **update** method calculates the median of the current and previous D scans and returns the list of medians
- If D is 0, then the input scan is return
- __history array in the update method stores the previous D scans. If the array has more than D scans, then the oldest entry is removed
- If the no of scans in the entry is less then D, then the median of those scans and the current scan is returned
- update method also checks if the length of the scans are consistent

## Project Structure

```
LidarFilters
├── filters
    ├── __init__.py
    ├── filters.py
├── tests
    ├── __init__.py
    ├── test_range_filter.py
    ├── test_temporal_median_filter.py
```

- filters.py contains the code for Range and Temporal Median filters.
- test_range_filter.py contains the test cases for RangeFilter
- test_temporal_median_filter.py contains the test cases for TemporalMedianFilter

## Build instructions on Linux

Ensure that Python3 is installed on the system

### Setting up the python virtual env

```sh
$ cd LidarFilters
$ python3 -m venv filterenv
$ source filterenv/bin/activate
```

### Installing dependencies

```sh
$ pip install -r requirements.txt
```

### Running the tests

```sh
$ python -m unittest tests.test_range_filter
$ python -m unittest tests.test_temporal_median_filter
```
