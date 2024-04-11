"""
2N 정도로 풀릴 것 같음
1. A-Index와 B-Index로 분리해서 진행
2. A와 B 모두 오름차순으로 정렬 후 B-Index 0으로 초기화
3. 반복문
    3.1. 만약 B-Index가 범위 초과할 경우 Break
    3.2. a 원소와 b 원소 비교
    3.3. 만약 a 가 작다면 answer + 1 하고 A-Index증가
    3.4. 이기든 지든 B-Index 증가
"""
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    ai = 0
    bi = 0
    while ai < len(A) and bi < len(B):
        nowA, nowB = A[ai],B[bi]
        if nowA < nowB:
            answer += 1
            ai += 1
        bi += 1
        
    return answer