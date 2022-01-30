table = [[i*2 for i in range(1,21)] + [0,0,0,0,0]]
table.append([10,13,16,19,25,30,35,40,0,0,0,0,0])
table.append([20,22,24,25,30,35,40,0,0,0,0,0])
table.append([30,28,27,26,25,30,35,40,0,0,0,0,0])
P = [[(i*0)+1 for i in j] for j in table] #position
nodes = [0,0]*4

turn = [1, 2, 3, 4, 1 ,2, 3, 4, 1, 2]

def move(point):
    Glist = []
    for node in nodes:
        a,b = node
        if P[a][b]:
            
            Glist.append([table[a][b+point],node])


    return Glist



print(table)