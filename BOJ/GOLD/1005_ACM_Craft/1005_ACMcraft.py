'''
1005번 ACM Craft (골드 3)
input : 
    t 테스트 케이스
    n 건물의 수, k 건물 규칙의 수
    time 각 건물당 건설에 걸리는 시간
    x, y 건설 순서
    w 건설해야하는 건물 번호
output :
    min_time 건설 완료하는데 드는 최소 시간
'''
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    # 진입 차수 및 그래프 저장
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    # 도착지점
    w = int(input())

    # 해당 노드에 도달하는데까지 필요한 시간
    dp = [0] * (n + 1)

    # 위상정렬 시작
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        now = queue.popleft()

        for next_node in graph[now]:
            dp[next_node] = max(dp[next_node], dp[now] + time[next_node])
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    print(dp[w])