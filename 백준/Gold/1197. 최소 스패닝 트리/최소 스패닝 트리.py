import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)] 
in_graph = [False]*(V+1)

for _ in range(E) :
    v1, v2, weight = map(int, input().split())
    graph[v1].append((weight, v2))
    graph[v2].append((weight, v1))

node_cnt = 0 
weight_sum = 0


edge_heap = [(0,1)] 
while node_cnt < V :
    w, node = heapq.heappop(edge_heap)
    if in_graph[node] :
        continue

    in_graph[node] = True
    node_cnt += 1
    weight_sum += w

    for edge in graph[node] :
        heapq.heappush(edge_heap, edge)

print(weight_sum)