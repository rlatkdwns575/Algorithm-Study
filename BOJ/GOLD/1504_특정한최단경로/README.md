# 1504번 특정한 최단 경로 (골드 4)

## 1. 문제
방향성이 없는 그래프가 주어진다. 
세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 
그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 
하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 
1번 정점에서 N번 정점으로 이동할 때, 
주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

## 2. 입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 

둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, 
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 

다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 
임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

## 3. 출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 
그러한 경로가 없을 때에는 -1을 출력한다.

## 4. 문제 풀이
해당 문제는 가중치가 있는 그래프의 최단경로 문제이므로,
다익스트라(Dijkstra) 알고리즘으로 풀어야 한다.
다익스트라 알고리즘은 
1. 출발노드를 기준으로 각 노드의 최소비용을 저장
2. 방문하지 않은 노드 중 가장 비용이 적은 노드부터 이동
3. 만약 해당 경로를 통해 도착한 노드까지의 비용이 저장된 최소비용보다 작을 경우 최소비용 갱신
4. 2,3번 반복

- 간선 정보 저장 : 각각의 노드 번호의 인덱스에 연결 간선과 길이를 튜플로 저장
- 다익스트라 알고리즘 : 최소큐를 통해 저장된 경로들 중 가장 짧은 (가까운) 경로의 노드부터 탐색
- 노드 최단거리 저장 : 리스트에 float('inf') X (n+1) 로 각각의 노드까지의 거리 초기화

## >>>코드

```python
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
```

## 5. 문제 링크
https://www.acmicpc.net/problem/1504
