# ---------------------------------------------------------
#                          NOTES
# ---------------------------------------------------------
"""
Dieter Steinhauser
10/10/2022

Helper methods for various repeated functions
"""
# ---------------------------------------------------------
#                         INCLUDES
# ---------------------------------------------------------
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import csv
import os
import statistics as stat
from scipy.stats import kurtosis, skew, sem

# ---------------------------------------------------------
#                    METHODS
# ---------------------------------------------------------
current_dir = Path(os.path.dirname(__file__))
homework_dir = current_dir.parent



def read_csv_data(filepath):
    """
    reads and parses the csv data of the file.

    :param filepath: Path object to the csv file.
    :type filepath: path
    :return: Parsed csv data.
    :rtype: dict
    """
    index = 1
    return_dict = {}

    with open(str(filepath), newline='') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            try:
                return_dict[index] = [float(value) for value in row]
            except:
                return_dict[index] = row

            index += 1

    return return_dict


def read_txt_data(filepath):
    """
    Reads the text file lines

    :param filepath: path to the file being read
    :type filepath: str
    :return: list of lines read from the file
    :rtype: list
    """
    
    with open(filepath) as f:
        lines = f.readlines()

    return lines



def hamming_distance(int1, int2):
    """Method for calculating the hamming distance between two integers"""
    xor_num = int1 ^ int2
    bin_string = bin(xor_num).lstrip('0b').count('1')
    distance = bin_string
    return distance


def summary(data_list):
    """
    generate the five number summary of a dataset.

    Lower, Q1, Median, Q3, Upper

    :param data_list:
    :type data_list: list
    :return: Five number summary
    :rtype: dict
    """
    return_dict = dict()
    return_dict['lower_bound'] = min(data_list)
    return_dict['lower_quartile'] = np.quantile(data_list, 0.25)
    return_dict['median'] = stat.median(data_list)
    return_dict['upper_quartile'] = np.quantile(data_list, 0.75)
    return_dict['upper_bound'] = max(data_list)
    return return_dict


def describe(data_list):
    """
    Describes the dataset, returns a dictionary of useful statistics.

    Mean, Standard Deviation, Median, Minimum, Maximum, Skew, Kurtosis, Standard Error

    :param data_list:
    :type data_list: list
    :return: Five number summary
    :rtype: dict
    """
    return_dict = dict()
    return_dict['mean'] = stat.mean(data_list)
    return_dict['standard_deviation'] = stat.stdev(data_list)
    return_dict['median'] = stat.median(data_list)
    return_dict['mode'] = stat.mode(data_list)
    return_dict['minimum'] = min(data_list)
    return_dict['maximum'] = max(data_list)
    return_dict['skew'] = skew(data_list)
    return_dict['kurtosis'] = kurtosis(data_list)
    return_dict['standard_error'] = sem(data_list)
    return return_dict

