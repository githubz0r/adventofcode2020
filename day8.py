import numpy as np
instructions = []
with open ('day8.txt') as input:
    lines = input.readlines()
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.split()
        line[1] = int(line[1])
        instructions.append(line)



def carry_instruction(instructions, index):
    unique_indices = []
    accumulator = 0
    no_2nd = True
    while no_2nd:
        if index > len(instructions)-1:
            break
        else:
            instruct = instructions[index]
        if index in unique_indices:
            no_2nd = False

        else:
            unique_indices.append(index)
        if instruct[0] == 'nop':
            index += 1
        elif instruct[0] == 'acc':
            accumulator += instruct[1]
            index +=1
        elif instruct[0] == 'jmp':
            index += instruct[1]
    return accumulator, no_2nd

print(carry_instruction(instructions, 0))

def check_jmp_nop(instruction_list, index):
    instructions_list_cp = instruction_list.copy() # otherwise changing will change the original list
    cur_instruc = instructions_list_cp[index].copy()
    if cur_instruc[0] == 'jmp':
        new_instruc = ['nop', cur_instruc[1]]
    elif cur_instruc[0] == 'nop':
        new_instruc = ['jmp', cur_instruc[1]]
    else:
        new_instruc = cur_instruc
    instructions_list_cp[index] = new_instruc
    acc, did_break = carry_instruction(instructions_list_cp, 0) # set proper index for the whole program i.e.  0
    is_terminator = False
    if did_break == True:
        is_terminator = True
    return acc, is_terminator

#print(instructions[3])
check_instructions = [check_jmp_nop(instructions, i) for i in range(len(instructions))]
#print(instructions[3])
did_terminate = np.array([i[1] for i in check_instructions])
acc_value = np.array([i[0] for i in check_instructions])

print(acc_value[did_terminate])


