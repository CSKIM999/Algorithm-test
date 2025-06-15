import sys

input = sys.stdin.readline
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos_in = {v: i for i, v in enumerate(in_order)}

stack = [(0, n-1, 0, n-1)]
result = []
while stack:
    il, ir, pl, pr = stack.pop()
    if il > ir:
        continue

    root = post_order[pr]
    result.append(str(root))

    mid = pos_in[root]
    left_size = mid - il

    stack.append((mid+1, ir, pl+left_size, pr-1))
    stack.append((il, mid-1, pl, pl+left_size-1))

print(' '.join(result))