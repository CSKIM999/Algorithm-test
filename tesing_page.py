from itertools import combinations
data_list = [
    [0,1,2,3,4,5],
    [1,0,2,3,4,5],
    [1,2,0,3,4,5],
    [1,2,3,0,4,5],
    [1,2,3,4,0,5],
    [1,2,3,4,5,0]
]

# sum_list = [sum(i) + sum(j) for i, j in zip(data_list, zip(*data_list))]
sum_list = [i for i in zip(data_list)]
print(sum_list)

# a = 10 // 2 - 3
# b = [i for i in combinations(sum_list,3)]
# print(b)