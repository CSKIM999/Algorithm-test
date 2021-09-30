dic = {'#':9,'.':0,'O':-1,'R':1,'B':2}
m = 3
data = ['#.ORB']
table = [list(map(lambda x : dic[x],[i for i in input()])) for _ in range(m)]
print(table)

7 7
#######
#RB...#
#####.#
#.....#
#.#####
#....O#
#######