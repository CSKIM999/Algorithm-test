from lib import xprint,Prepare_Coding_Test
beta = Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q4195
#######  TODAY  #######
##### 2022. 07. 29 #####
GIVEN ) 어떤 사이트의 친구관계가 생긴 순서대로 주어질 때 
        두 사람의 친구네트워크에 몇명이 있는지 구하라
INPUT ) 첫째 줄에 테스트케이스의 수가 주어진다.
        각 TC 첫째 줄에는 관계의 수 F 가 주어지며, 이 값은 100,000 이하의 자연수이다.
        다음 F 개의 줄에 친구관계가 생긴 순서대로 주어진다. 친구관계는 두개의 아이디로 이루어지며
        알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.
OUTPUT) 친구관계가 입력될 때 마다, 친구네트워크에 몇명이 존재하는지 구하는 프로그램을 작성하라
Approach )  매 입력마다 친구네트워크를 출력해야함. 따라서 메모이제이션이 필수적일듯 함.
            찾지말고 이름, 인덱스를 딕셔너리 관리하고 리스트 길이로 출력하자
'''
'''
tc = int(input())
for _ in range(tc):
    F = int(input())
    nameTag = {}
    dic = {}
    group = []
    index = 0
    for x in range(F):
        I = []
        get = list(input().split())

        # 네임택 반환
        for i in range(2):
            try:
                I.append(nameTag[get[i]])
            except KeyError:
                nameTag[get[i]] = index
                I.append(nameTag[get[i]])
                index += 1
        
        I_A,I_B = I[0],I[1]
        flag= [0,0]

        # 그룹 인덱스 반환
        try:
            V_A = dic[I_A]
            flag[0] = 1
        except KeyError:
            pass
        try:
            V_B = dic[I_B]
            flag[1] = 1 
        except KeyError:
            pass
        
        #공간복잡도가 불안하지만 2차원행렬로 참조 사용해보자
        if flag == [1,1]: # 둘 다 그룹이 있을때
            if V_A != V_B:
                group[V_A] += group[V_B]
                group[V_A] = list(set(group[V_A]))
                group[V_B] = group[V_A]
                print(len(group[V_A]))
            else:
                print(len(group[V_A]))
        elif flag == [1,0]: # A만 있을때
            dic[I_B] = V_A
            group[V_A].append(I_B)
            print(len(group[V_A]))
        elif flag == [0,1]: #B 만 있을때
            dic[I_A] = V_B
            group[V_B].append(I_A)
            print(len(group[V_B]))
        else: # 둘 다 없을때
            l = len(group)
            dic[I_A],dic[I_B] = l,l
            group.append([I_A,I_B])
            print(len(group[l])) 

1회차 . . . 시간초과 실패 딱히 시간복잡도를 줄일 여지는 없어보임
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x,y):
    if x==y:
        return value[x]
    x,y = min(x,y),max(x,y)
    if tree[x] > tree[y]:
        parent[y] = x
        value[x] += value[y]
        return value[x]
    else:
        if tree[x] == tree[y]:
            tree[x] +=1
            parent[y] = x
            value[x] += value[y]
            return value[x]
        parent[x] = y
        value[y] +=  value[x]
        return value[y]


tc = int(input())
for _ in range(tc):
    parent = []
    F = int(input())
    nameTag = {}
    value = []
    tree = []
    index = 0
    for x in range(F):
        I = []
        get = list(input().split())

        # 네임택 반환
        for i in range(2):
            try:
                I.append(nameTag[get[i]])
            except KeyError:
                nameTag[get[i]] = index
                I.append(nameTag[get[i]])
                parent.append(index)
                value.append(1)
                tree.append(0)
                index += 1
        
        a,b = find(I[0]),find(I[1])
        print(union(a,b))



'''
3트 솔브
union 메서드의 line 98 else 문에서 내생각엔 parent를 먼저 대입해서 이사단이난듯
'''