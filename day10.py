import numpy as np
adapters = np.loadtxt('day10.txt')
adapters = np.sort(adapters)

diffs = {}

diff_outlet = adapters[0]-0
diffs[diff_outlet]=1

for i in range(len(adapters)-1):
    diff = adapters[i+1] - adapters[i]
    if diff not in diffs.keys():
        diffs[diff] = 1
    else:
        diffs[diff] += 1
diffs[3] += 1 # final adapter to device's inbuilt adapter
print(len(adapters))
print(diffs[1]*diffs[3])

diffs_list = ['1']+[str(int(adapters[i+1]-adapters[i])) for i in range(len(adapters)-1)]
runs_of_1 = "".join(diffs_list).split('3')
runs_of_1 = [len(i)+1 for i in runs_of_1]
runs_of_1 = np.array(runs_of_1)
unique_runs, run_counts = np.unique(runs_of_1, return_counts=True)
tribonacci_map = {1:1, 2:1, 3:2, 4:4, 5:7}
tribonacci_runs = [tribonacci_map[i] for i in unique_runs]
combs = [i**j for i,j in zip(tribonacci_runs, run_counts)]
from functools import reduce
combs_total = reduce(lambda x,y: x*y, combs)
print(combs)
print(combs_total)