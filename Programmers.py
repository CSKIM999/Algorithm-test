from itertools import combinations

data = [['O',0],['1',1],['2',2],['3',3],['4',4]]
hist = []
# for i in range(4): # 입는 의상의 개수
#     temp = []
#     for j in range(total): # 경우의 수 따지기
#         temp.append(j)
#         if len(temp) != i:
#             for k in range(total):
#                 pass10
#         hist = hist + temp
#         temp = []
for time in range(1,6):
    time_hist = []
    temp = list(combinations(data,time))
    for i in temp:
        check = set()
        for j in i:
            check.add(j[1])
        if len(check) == time:
            hist.append(i)
            time_hist.append(i)
    print()
    print(f'time hist : {time_hist}')
    print()

print(len(hist))