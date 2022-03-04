'''
Given ) N 개의 물건이 각각 W 의 무게와 V 의 가치를 지닌다.
        준서는 최대 K 만큼의 무게를 들 수 있을 때 들 수 있는 기대가치값을 구하라
Input ) 첫째 줄에 물건의 수 N (1<= N <= 100) , 버티는 최대무게 K (1<= K <= 100,000) 이 주어진다
        둘째 줄부터 N 개의 줄에 거쳐 각 물건의 무게 W (1<= W <= 100,000) 와 해당 물건의 가치 V (0<= V <= 1,000) 가 주어진다
Output) 배낭에 넣을 수 있는 물건들의 최대 가치합을 구하라


Approach ) DP 로 구성해보자 필요한 모듈은?
            작은수부터 올라가는 방식 => 역순 sort
            dp 리스트 작성
            리스트에 모든 원소를 넣음
            i=1
            이후 i 이상의 인덱스 원소와 dp 리스트를 더해서 dp 리스트에 넣음
                만약 dp 리스트에 해당 숫자가 있다면 
'''
def xprint(a):
    for i in a:
        print(i)
N,K = 4,7
get = [
    [4, 7],
    [6 ,13],
    [4, 8],
    [3, 6],
    [5 ,12]
]
W = [0 for x in range (N+1)]
V = [0 for x in range (N+1)]
DP = [[0 for x in range(K+1)] for x in range (N+1)]
for x in range (1,N+1) :
    W[x],V[x] = get[x]

print(W,V)
for i in range (1,N+1) : #만족도인덱스
    for j in range (1,K+1) : #크기인덱스
        if j >= W[i] :
            print(f'i : {i} && j : {j}')
            print(f'V[i] : {V[i]} ***&*** DP[i][j-W[i]] : {DP[i][j-W[i]]} ***&*** DP[i-1][j] : {DP[i-1][j]}')
            DP[i][j] = max(V[i]+DP[i][j-W[i]],DP[i-1][j])
            print(f'{W} :: W')
            print(f'{V} :: V')
            xprint(DP)
            print()
        else :
            DP[i][j] = DP[i-1][j]
            

print(f'{W} :: W')
print(f'{V} :: V')
xprint(DP)