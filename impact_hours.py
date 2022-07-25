import os
import re
from pathlib import Path


def _get_files(filepath: str):
    """
    This function reads an input file and converts each set of numbers(start and end time) in the file as a sublist,
    sorts the list based on start time and calculates the total time covered in the input file.

    :param filepath: path to access the input file
    :return: start and end shifts parsed as list
    """
    with open(filepath, 'r') as reader:
        data = [x.rstrip('\n').split(" ") for x in reader.readlines()]
        list = [[int(i) for i in sublist] for sublist in data]
        list.pop(0)
        list = sorted(list)
        total_hours = (list[-1][-1] - list[0][0])
        return list, total_hours


def impact_factor(filepath):
    """
    This function takes the sorted list of starting and ending time of each lifeguard shift and iterates over each shift
    to find the impact factor of the life guard that has maximum overlap hours and minimum number of solo hours during
    the pool duty and calculates the hours that can still be covered if that pool guard is fired.

    :param filepath: path to access the input file
    :return: the hours that can be covered
    """
    # get the list of shift timings and total hours during the shift
    list, total_hours = _get_files(filepath)

    unique_hours = []  # empty list to store the non-overlapping hours(impact hours) of each pool guard

    # iterate over the list of shift timings and append the impact hours
    for i in range(len(list)):
        if i == 0:
            curr = list[i]
            next = list[i + 1]
            impact = (curr[1] - curr[0]) - (curr[1] - next[0])
            unique_hours.append(impact)

        elif i == len(list) - 1:
            prev = list[i - 1]
            curr = list[i]
            impact = (curr[1] - curr[0]) - (prev[1] - curr[0])
            unique_hours.append(impact)

        else:
            prev = list[i - 1]
            curr = list[i]
            next = list[i + 1]
            impact = (curr[1] - curr[0]) - (prev[1] - curr[0]) - (curr[1] - next[0])
            unique_hours.append(impact)

    # calculate the hours that can be covered after removing one lifeguard with minimum impact
    hours_covered = (total_hours - min(unique_hours))

    print(hours_covered)

    return hours_covered


if __name__ == '__main__':
    # Path to input file
    directory = 'CMU MSSM Summer Programming Assignments'
    files = Path(directory).glob('*')
    for file in files:
        num = int(re.search("\d+", str(file))[0])

        # apply the function get the hours covered
        hours_covered = impact_factor(file)

        # write the results to output directory
        with open(f'output/{num}.out', 'w') as output:
            output.write(str(hours_covered))
            output.close()
