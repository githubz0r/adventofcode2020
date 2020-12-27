import numpy as np 
strs = np.genfromtxt('day5.txt', dtype='str')

def binary_read(strng, N=128):
    rows = np.arange(N)
    cols = np.arange(8)
    for i in strng:
        if i == 'F':
            middle = int(len(rows)/2)
            rows = rows[0:middle] # remember indexing is excluding last val
        elif i == 'B':
            middle = int(len(rows)/2)
            rows = rows[middle:]
        elif i == 'R':
            mid_col = int(len(cols)/2)
            cols = cols[mid_col:]
        elif i == 'L':
            mid_col = int(len(cols)/2)
            cols = cols[0:mid_col]
        #print(rows.shape)
    return(rows, cols)

def seat_id(rowcol_tuple):
    seat_id = rowcol_tuple[0]*8 + rowcol_tuple[1]
    return(seat_id)

seat_ids = [seat_id(binary_read(i)) for i in strs]
seat_ids = np.concatenate(seat_ids, axis=0)
print(np.max(seat_ids))

def check_seat(seat_id):
    is_seat = False
    global seat_ids
    if seat_id not in seat_ids:
        if seat_id+1 in seat_ids and seat_id-1 in seat_ids:
            is_seat = True
    return(is_seat)

id_range = np.arange(956)
seat_checks = [check_seat(i) for i in id_range]
print(np.sum(seat_checks*1))
print(np.where(seat_checks)[0:10])
