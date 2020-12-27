import numpy as np
import re
seats = np.loadtxt('day11.txt', dtype=str)

def convert_to_2d(arr_strings):
    return np.array([[j for j in i] for i in arr_strings])

seats = convert_to_2d(seats)

def process_seats(seats):
    seats_cp = seats.copy()
    N = seats.shape[0]
    M = seats.shape[1]
    for i in np.arange(N):
        row = seats[i, :]
        for idx, seat_state in enumerate(row):
            if seat_state == '.':
                continue
            adj_occ_count = 0
            adj_ids = get_adjacent_idx(i, idx, N, M)
            adj_seats = [seats[a_i[0], a_i[1]] for a_i in adj_ids]
            for adj_seat in adj_seats:
                if adj_seat == '#':
                    adj_occ_count += 1
            if seat_state == '#' and adj_occ_count >= 4:
                seats_cp[i, idx] = 'L'
            elif seat_state == 'L' and adj_occ_count < 1:
                seats_cp[i, idx] = '#'
    return(seats_cp)

def get_adjacent_idx(i, j, N, M, id_range=1):
    row_ids = np.arange(i-id_range, i+1+id_range)
    col_ids = np.arange(j-id_range, j+1+id_range)
    id_pairs = []
    for l in row_ids:
        for k in col_ids:
            id_pairs.append([l,k])
    mid_val = (len(id_pairs)-1)/2
    id_pairs.pop(int(mid_val))
    inds_to_keep = []
    for idx, pair in enumerate(id_pairs):
        if (pair[0] >= 0 and pair[0] < N) and (pair[1] >= 0 and pair[1] < M):
            inds_to_keep.append(idx)
    id_pairs = [id_pairs[i] for i in set(inds_to_keep)]
    return(id_pairs)


def seat_simulation(seat_arr):
    N_trues = seat_arr.shape[0]*seat_arr.shape[1]
    curr_arr = seat_arr
    iterations = 0
    continue_loop = True
    while continue_loop:
        new_arr = process_seats(curr_arr)
        if np.sum(new_arr==curr_arr) < N_trues:
            curr_arr = new_arr
            iterations += 1
        else:
            continue_loop = False
    return(curr_arr)

def count_seats(arr):
    arr_flat = arr.flatten()
    are_seats = arr_flat == '#'
    return np.sum(are_seats)

seat_automata = seat_simulation(seats)
print(count_seats(seat_automata))

### part 2 ###

def process_seats2(seats):
    seats_cp = seats.copy()
    N = seats.shape[0]
    M = seats.shape[1]
    for i in np.arange(N):
        row = seats[i, :]
        for j, seat_state in enumerate(row):
            if seat_state == '.':
                continue
            adj_loss_count = 0
            adj_loss_count += count_los_diagonal(seats, i, j)
            adj_loss_count += count_los_diag_opp(seats, i, j)
            adj_loss_count += count_los_vertical(seats, i, j)
            adj_loss_count += count_los_horizontal(seats, i, j)
            if seat_state == '#' and adj_loss_count >= 5:
                seats_cp[i, j] = 'L'
            elif seat_state == 'L' and adj_loss_count < 1:
                seats_cp[i, j] = '#'
    seats_joined = ["".join(seats_cp[i]) for i in range(N)]
    return(seats_cp)

def seat_simulation2(seat_arr):
    N_trues = seat_arr.shape[0]*seat_arr.shape[1]
    curr_arr = seat_arr
    iterations = 0
    continue_loop = True
    while continue_loop:
        new_arr = process_seats2(curr_arr)
        if np.sum(new_arr==curr_arr) < N_trues:
            curr_arr = new_arr
            iterations += 1
        else:
            continue_loop = False
    return(curr_arr)

def count_los_diagonal(seats, i,j):
    N, M = seats.shape
    ind_pairs_lower = []
    i_loop = i
    j_loop = j
    while i_loop > 0 and j_loop > 0:
        ind_pairs_lower.append([i_loop-1, j_loop-1])
        i_loop -= 1
        j_loop -= 1
    ind_pairs_upper = []
    i_loop = i
    j_loop = j
    while i_loop < N-1 and j_loop < M-1:
        ind_pairs_upper.append([i_loop+1, j_loop+1])
        i_loop += 1
        j_loop += 1
    seat_vecs = []
    ind_pairs = [ind_pairs_lower, ind_pairs_upper]
    for subl in ind_pairs:
        seat_vec = []
        for pair in subl:
            seat_vec.append(seats[pair[0], pair[1]])
        seat_vec = "".join(seat_vec)
        seat_vecs.append(seat_vec)
    seat_vecs[0] = seat_vecs[0]
    hash_count = 0
    for sub_vec in seat_vecs:
        if re.match('^\.*#+', sub_vec):
            hash_count += 1
    return hash_count

def count_los_diag_opp(seats, i,j):
    N, M = seats.shape
    seats_mirrored = np.fliplr(seats)
    j = M-1-j # mirror j as well
    ind_pairs_lower = []
    i_loop = i
    j_loop = j
    while i_loop > 0 and j_loop > 0:
        ind_pairs_lower.append([i_loop-1, j_loop-1])
        i_loop -= 1
        j_loop -= 1
    ind_pairs_upper = []
    i_loop = i
    j_loop = j
    while i_loop < N-1 and j_loop < M-1:
        ind_pairs_upper.append([i_loop+1, j_loop+1])
        i_loop += 1
        j_loop += 1
    seat_vecs = []
    ind_pairs = [ind_pairs_lower, ind_pairs_upper]
    for subl in ind_pairs:
        seat_vec = []
        for pair in subl:
            seat_vec.append(seats_mirrored[pair[0], pair[1]])
        seat_vec = "".join(seat_vec)
        seat_vecs.append(seat_vec)
    seat_vecs[0] = seat_vecs[0]
    hash_count = 0
    for sub_vec in seat_vecs:
        if re.match('^\.*#+', sub_vec):
            hash_count += 1
    return hash_count

def count_los_vertical(seats, i,j):
    N, M = seats.shape
    ind_pairs = [[g, j] for g in np.arange(N)]
    seat_vec = []
    for pair in ind_pairs:
        if pair[0] == i and pair[1] == j:
            seat_vec.append('S')
        else:
            seat_vec.append(seats[pair[0], pair[1]])
    seat_vec_join = "".join(seat_vec)
    seat_vec = seat_vec_join.split('S')
    seat_vec = [s for s in seat_vec]
    seat_vec[0] = seat_vec[0][::-1] # re-orient to perspective of point
    hash_count = 0
    for sub_vec in seat_vec:
        if re.match('^\.*#+', sub_vec):
            hash_count += 1
    return hash_count

def count_los_horizontal(seats, i,j):
    N, M = seats.shape
    ind_pairs = [[i, g] for g in np.arange(M)]
    seat_vec = []
    for pair in ind_pairs:
        if pair[0] == i and pair[1] == j:
            seat_vec.append('S')
        else:
            seat_vec.append(seats[pair[0], pair[1]])
    seat_vec_join = "".join(seat_vec)
    seat_vec = seat_vec_join.split('S')
    seat_vec = [s for s in seat_vec]
    seat_vec[0] = seat_vec[0][::-1]
    hash_count = 0
    for sub_vec in seat_vec:
        if re.match('^\.*#+', sub_vec): # check if there's an occupied seat
            hash_count += 1
    return hash_count



seat_automata2 = seat_simulation2(seats)
print(count_seats(seat_automata2))
