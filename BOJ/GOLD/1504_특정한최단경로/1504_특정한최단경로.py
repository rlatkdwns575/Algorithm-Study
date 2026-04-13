"""
1504번 특정한 최단 경로
입력 : n (정점 수), e (간선 수)  
a, b (연결된 정점) c (두 정점 사이 거리)
v1, v2 (반드시 거쳐야하는 정점 2개)
출력 : min_dist (최단 경로 길이)
>> 1번 정점에서 v1, v2 정점을 거쳐 n번 정점까지 도달하는 최단거리
"""
import heapq

n, e = map(int, input().split())
path = list([] for _ in range(n+1))
for _ in range(e):
    a, b, c = map(int, input().split())
    path[a].append((b, c))
    path[b].append((a, c))
    
v1, v2 = map(int, input().split())

def min_dist(start, end):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))
    
    while heap:
        cur_dist, cur = heapq.heappop(heap)
        
        if cur_dist > dist[cur]:
            continue
        
        for next_node, w in path[cur]:
            if dist[next_node] > cur_dist + w:
                dist[next_node] = cur_dist + w
                heapq.heappush(heap, (dist[next_node], next_node))
    
    return dist[end]
            
# 경로 1 : 1 > v1 > v2 > n
path1 = min_dist(1, v1) + min_dist(v1, v2) + min_dist(v2, n)
# 경로 2 : 1 > v2 > v1 > n
path2 = min_dist(1, v2) + min_dist(v2, v1) + min_dist(v1, n)

answer = min(path1, path2)
if answer == float('inf'):
    print(-1)
else:
    print(answer)