import sys
from bisect import bisect_left

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

# 1. 자료 구조 초기화
# ends: 길이별 부분 수열의 최소 마지막 값
# ends_idx: ends의 원소가 nums에서 위치한 인덱스
# prev: 복원을 위한 이전 인덱스
ends, ends_idx, prev = [], [], [-1] * N

# 2. ends 업데이트
for i, val in enumerate(nums):
    idx = bisect_left(ends, val)
    if idx == len(ends):
        ends.append(val)
        ends_idx.append(i)
    else:
        ends[idx] = val
        ends_idx[idx] = i
    if idx > 0:
        prev[i] = ends_idx[idx - 1]

# 3. LIS 복원
length = len(ends)
lis, cur = [], ends_idx[-1]
while cur != -1:
    lis.append(nums[cur])
    cur = prev[cur]
lis.reverse()

print(length)
print(*lis)