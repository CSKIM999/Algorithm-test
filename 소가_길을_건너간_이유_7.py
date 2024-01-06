from collections import deque

n,t = list(map(int,input().split()))
table = []
for i in range(n):
    table.append(list(map(int,input().split())))

hist = [[1e9 for _ in range(n)] for _ in range(n)]
hist[0][0] = 0

# direction setting
d3 = set()
for i in range(-3,1):
    v = 3+i
    d3.add((i,v))
    d3.add((i,-v))
    d3.add((-i,v))
    d3.add((-i,-v))
d3 = list(d3)
d3.sort()
d = [[-1,0],[0,-1],[0,1],[1,0]]

q = deque()
q.append([0,0,0])

def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def getNew(x,y,i,l):
    if l == 1:
        nx,ny = x+d[i][0],y+d[i][1]
    else:
        nx,ny = x+d3[i][0],y+d3[i][1]
    if check(nx,ny):
        return [nx,ny]
    else:
        return False


while q:
    x,y,v = q.popleft()
    for i in range(12):
        if i < 4:
            new = getNew(x,y,i,1)
            if new:
                nx,ny = new
                nv = table[nx][ny] + v + 3*t
                if nv < hist[nx][ny]:
                    hist[nx][ny] = nv
                    q.append([nx,ny,nv])

        new = getNew(x,y,i,3)
        if new:
            nx,ny = new
            if [nx,ny] == [2,2]:
                pass
            nv = table[nx][ny] + v + 3*t
            if nv < hist[nx][ny]:
                hist[nx][ny] = nv
                q.append([nx,ny,nv])
    
                

result = [hist[-1][-3]+2*t,hist[-2][-2]+2*t,hist[-3][-1]+2*t,hist[-1][-2]+t,hist[-2][-1]+t,hist[-1][-1]]
print(min(result))

# # 배송 상세 데이터 받아오는 코드 
# fetch(testURI,{
#   method: 'GET', // 또는 'POST', 'PUT', 'DELETE' 등
#   headers: {
#     'Content-Type': 'application/json',
#     // 필요한 경우 다른 헤더들도 추가할 수 있습니다.
#   },
#   // body: JSON.stringify(data), // POST나 PUT 요청의 경우 데이터를 포함할 수 있습니다.
# }).then(res => res.json()).then(data=> console.log(data))


# #보니까 payload의 객체 dlvNo 가 배송번호
# const getDetailURI = (num) => {
#     return `https://po.oliveyoung.co.kr/admin/delivery/delivery.getOrderDeliveryGoods.do?pDlvNo=${num}&pDtlSctCd=&&_=1704437327045`
# }
# const getThisDetail = async (num) => {
#     return await fetch(getDetailURI(num),{
#   method: 'GET', 
#     'Content-Type': 'application/json',
#   }).then(res => res.json()).then(data=> console.log(data))}

