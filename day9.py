import numpy as np
nrs = np.loadtxt('day9.txt')

def xmas(nrs, n_preamble=25):
    preamble = nrs[np.arange(n_preamble)]
    possible_sums = make_sums(preamble)
    is_valid = np.zeros(nrs.shape[0], dtype=bool)
    N_iters = nrs.shape[0]-n_preamble
    cur_index = n_preamble
    cur_number = nrs[cur_index]
    while N_iters > 1:
        if cur_number in possible_sums:
            is_valid[cur_index] = True

        preamble = np.array(list(preamble[1:])+[cur_number])
        possible_sums = make_sums(preamble)
        cur_index = cur_index+1
        cur_number = nrs[cur_index]
        N_iters -= 1
    return(is_valid)


def make_sums(preamble):
    x, y = np.meshgrid(preamble, preamble)
    preamble_sum = x+y
    inds = np.triu_indices(len(preamble), k=1)
    return preamble_sum[inds]

#print(nrs[-1])
test = xmas(nrs)
#print(np.sum(test))
inds_false = np.where(~test)[0]
print(inds_false)
first_number = np.min(inds_false[inds_false > 24])
print(nrs[first_number]) # be careful that the float with .0 will not be accepted

def get_contig(nrs, inv_number):
    contigs = []
    cur_index = 0
    cur_number = nrs[cur_index]
    inds = np.arange(len(nrs))
    cur_sum = 0
    for idx, i in enumerate(nrs):
        running_sum, contig = run_sum(nrs, idx, inv_number)
        if running_sum == inv_number:
            contigs.append(contig)

    return(contigs)

def run_sum(nrs, idx, max_val):
    idx_range = np.arange(len(nrs))[idx:]
    running_sum = 0
    contig = []
    for i in idx_range:
        if running_sum >= max_val:
            break
        contig.append(nrs[i])
        running_sum += nrs[i]
    return(running_sum, contig)

contigs_test = get_contig(nrs, nrs[first_number])
test_sum = [sum(i) for i in contigs_test]
print(contigs_test)
print(test_sum)
print(min(contigs_test[0]+max(contigs_test[0])))
