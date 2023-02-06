cap, n, deliveries, pickups = 2, 7, [
    1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]


def solution(cap, n, deliveries, pickups):
    d, p = deliveries, pickups
    answer = 0
    point = [0, 0]
    fuel = 0

    def charge(index):
        nonlocal fuel, cap, point
        fuel += index+1
        print(fuel)
        point = [i+cap for i in point]
        return point

    for i in range(n-1, -1, -1):
        if d[i]:
            if not point[0]:
                charge(i)
            point[0] -= d[i]
            if point[0] < 0:
                while point[0] < 0:
                    charge(i)
        if p[i]:
            if not point[1]:
                charge(i)
            point[1] -= p[i]
            if point[1] < 0:
                while point[1] < 0:
                    charge(i)

    return answer


print(solution(cap, n, deliveries, pickups))
