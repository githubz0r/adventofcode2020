import numpy as np
import functools
numbers = np.loadtxt('day1.txt', dtype=int)
sum_to_2020 = []
for i,j in enumerate(numbers):
    for k,l in enumerate(numbers):
        for z,x in enumerate(numbers):
            if i > k and k > z:
                if j+l+x == 2020:
                    nr_inds = [i, k, z]
                    sum_to_2020.append(nr_inds)
print(sum_to_2020)
def calc_prod(ind_sublist, nr_list=numbers):
    extracted_nrs = [nr_list[i] for i in ind_sublist]
    prod = functools.reduce(lambda x,y: x*y, extracted_nrs)
    return(prod)
products = [calc_prod(subl) for subl in sum_to_2020]
print(products, 
    numbers[sum_to_2020[0][0]]*numbers[sum_to_2020[0][1]]*numbers[sum_to_2020[0][2]])