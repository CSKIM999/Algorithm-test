import math
def solution(fees, records):
    n = len(records)
    data = {}
    time = []
    for i in range(n):
        m = len(data)
        t,n,io = records[i].split(' ')
        if n not in data:
            data[n] = [m,True]
            time.append([t,0])
        elif data[n][1] == True and io == 'OUT':
            ih,im = map(int,time[data[n][0]][0].split(':'))
            oh,om = map(int,t.split(':'))
            tim,tom = (ih*60)+im,(oh*60)+om
            time[data[n][0]][1] += tom - tim
            data[n][1] = False
        elif data[n][1] == False and io == 'IN':
            time[data[n][0]][0] = t
            data[n][1] = True
            
    for i in data:
        index = data[i][0]
        if data[i][1] == True:
            ih,im = map(int,time[index][0].split(':'))
            oh,om = 23,59
            tim,tom = (ih*60)+im,(oh*60)+om
            time[index][1] += tom-tim
            time[index][0] =i
            data[n][1] = False
        else:
            time[index][0] = i
    result = []
    time.sort()
    
    for i,j in time:
        if j>fees[0]:
            fee = (math.ceil((j-fees[0])/fees[2]))*fees[3]
            result.append((fees[1]+fee))
        else:
            result.append(fees[1])   
    result = []
    return result

fees = [1, 461, 1, 10]
records =  ["00:00 1234 IN"]

print(solution(fees,records))