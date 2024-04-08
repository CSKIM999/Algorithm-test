import heapq
class hq:
    def __init__(self):
        self.queue = []
    
    
    def push(self,value):
        return heapq.heappush(self.queue,value)
    
    def pop(self):
        return heapq.heappop(self.queue)

def solution(operations):
    answer = []
    minQ = hq()
    maxQ = hq()
    hist = set()
    counter = 0
    for string in operations:
        a,b = string.split()
        b = int(b)
        if a == "I":
            maxQ.push([-b,counter])
            minQ.push([b,counter])
            counter += 1
        else:
            if b == 1:
                while maxQ.queue:
                    v, i = maxQ.pop()
                    if i not in hist:
                        hist.add(i)
                        break
            else:
                while minQ.queue:
                    v, i = minQ.pop()
                    if i not in hist:
                        hist.add(i)
                        break
                        

    answer = [None,None]
    if maxQ.queue:
        while maxQ.queue:
            v, i = maxQ.pop()
            if i not in hist:
                answer[0] = -v
                break
    if answer[0] == None:
        answer[0] = 0
    if minQ.queue:
        while minQ.queue:
            v, i = minQ.pop()
            if i not in hist:
                answer[1] = v
                break
    if answer[1] == None:
        answer[1] = 0
    return answer