patterns = []
with open('day3.txt') as input:
    lines = input.readlines()
    for line in lines:
        line = line.strip()
        patterns.append(line)

N = len(patterns[0])






def count_trees(patterns, step, skip = 1, pat_len = N):
    n_trees = 0
    cur_index = 0

    def traverse_patterns(pattern, index, pat_len=N):
        if index+1 > N:
            index = index - N
        value = pattern[index]
        if value == "#":
            nonlocal n_trees
            n_trees += 1
        return index+step

    for i in patterns[0::skip]:
        new_index = traverse_patterns(i, cur_index)
        cur_index = new_index
    return(n_trees)


steps = [1, 3, 5, 7, 1]
skips = [1, 1, 1, 1, 2]

tree_prod = 1
for i, j in zip(steps, skips):
    print(count_trees(patterns, i, j))
    tree_prod *= count_trees(patterns, i, j)
print(tree_prod)

