import sys

input = sys.stdin.readline
n = int(input())
liquids = list(map(int, input().split()))

# 초기 포인터 설정
left, right = 0, n - 1
# 최적 쌍과 차이 저장
best_pair = (liquids[left], liquids[right])
best_diff = abs(sum(best_pair))

while left < right:
    current_sum = liquids[left] + liquids[right]
    current_diff = abs(current_sum)
    # 더 작은 차이를 찾으면 갱신
    if current_diff < best_diff:
        best_pair, best_diff = (liquids[left], liquids[right]), current_diff
        if current_diff == 0:
            break
    # boolean 값을 이용해 포인터 이동
    left += current_sum < 0
    right -= current_sum > 0

print(*best_pair)