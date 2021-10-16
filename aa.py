n,l = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

def disc(lst,L,count): #정제된 list 입력
    given = lst[:]
    used_index = []
    for i in range(len(given)-1):
        if given[i+1] - given[i] == 1:#i가 i+1 보다 작을때 // 오름 경사
            try:
                tmp = [i for i in range(i-L+1,i+1)]
                if max([given[i] for i in tmp]) != min([given[i] for i in tmp]): # L 범위 내의 수가 모두 같은 수가 아닐때
                    return count
                for i in tmp:
                    if i in used_index: #방문처리가 이미 된 칸일때
                        return count


                used_index += tmp

            except IndexError: #지도를 벗어날 때
                return count
        elif given[i+1] - given[i] == -1: #i+1 이 i 보다 작을때 // 내림 경사
            try:
                tmp = [i for i in range(i+1,i+L+1)] 
                if max([given[i] for i in tmp]) != min([given[i] for i in tmp]): # 다음 L 범위의 숫자가 모두 같은가?
                    return count
                
                used_index += tmp
                
            except IndexError: #인덱스에러가 일어나는가?
                return count
        elif given[i+1] - given[i] == 0:  #i 와 i+1 이 같을 때 // 평지
            continue
        else: #높이가 2 이상 차이나는 경우
            return count
    return count+1

for i in range(n):
    #행
    v = data[i][:]
    count = disc(v,l,count)
    #열
    h = [data[j][i] for j in range(n)]
    count = disc(h,l,count)
    
print(count)