import numpy as np
import re
day2strings = []
with open('day2.txt') as input:
    lines = input.readlines()
    for line in lines:
        line = line.strip()
        line = line.split()
        for i, subline in enumerate(line):
            subline = subline.replace(':', '')
            #subline = subline.replace('-', ',')
            line[i] = subline
        day2strings.append(line)


def check_str(str_element):
    letter = str_element[1]
    nr_times = str_element[0].split('-')
    nr_times = [int(i) for i in nr_times]
    letter_count = 0
    is_valid = None
    for i in str_element[2]:
        if i==letter:
            letter_count += 1
    if letter_count >= nr_times[0] and letter_count <= nr_times[1]:
        is_valid = True
    else:
        is_valid = False
    return(is_valid)

check = check_str(day2strings[7])

strs_checked = [check_str(i) for i in day2strings]
strs_checked = np.array(strs_checked)
sum_valid = np.sum(strs_checked*1)
print(sum_valid)

def check_str2(str_element):
    letter = str_element[1]
    inds_to_match = str_element[0].split('-')
    inds_to_match = [int(i) for i in inds_to_match]
    string_ = str_element[2]
    letter_count = 0
    is_valid = None
    for ind in inds_to_match:
        ind = ind-1
        if string_[ind] == letter:
            letter_count += 1
    if letter_count ==1:
        is_valid = True
    else:
        is_valid = False
    return(is_valid)
strs_checked2 = np.array([check_str2(i) for i in day2strings])
sum_valid2 = np.sum(strs_checked2*1)
print(sum_valid2)
