import numpy as np
import functools
questions = []
with open('day6.txt') as input:
    cur_qu = []
    lines = input.readlines()
    for line in lines:
        if line =='\n':
            questions.append(cur_qu)
            cur_qu = []
        elif line == lines[-1]: # no newline at end
            line = line.strip()
            cur_qu += line.split()
            questions.append(cur_qu)
        else:
            line = line.strip()
            cur_qu += line.split() # adding to the list, not str itself

strs_conc = [functools.reduce(lambda x,y: x+y, i) for i in questions]
strs_uniq = [set(i) for i in strs_conc]

sum_lens = sum([len(i) for i in strs_uniq])
print(sum_lens)

def check_in_all(strings):
    strings_conc = functools.reduce(lambda x,y: x+y, strings)
    strings_unique = set(strings_conc)
    N = len(strings)
    counters_all = 0
    for i in strings_unique:
        counter = 0
        for substr in strings:
            if i in substr:
                counter += 1
        if counter/N == 1:
            counters_all += 1
    return(counters_all)

check_all_grps = [check_in_all(i) for i in questions]
print(sum(check_all_grps))
