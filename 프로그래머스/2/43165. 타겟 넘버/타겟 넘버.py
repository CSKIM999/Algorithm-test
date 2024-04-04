def solution(numbers, target):
    answer = 0
    nl = len(numbers)
    def dfs(index,value):
        nonlocal answer,target
        if index == nl:
            if value == target:
                answer += 1
            return
        new = numbers[index]
        dfs(index+1,value + new)
        dfs(index+1,value - new)
    dfs(0,0)
    return answer