"""
17404번 RGB거리 2 (골드 4)
input :
    n 집의 개수
    r 빨간색 비용, g 초록색 비용, b 파란색 비용
output :
    min_cost 페인트 비용 최소값
"""

n = int(input())
paint = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
ans = INF
for i in range(3):
    DP = [[INF, INF, INF] for _ in range(n)]
    DP[0][i] = paint[0][i]

    for j in range(1, n):
        DP[j][0] = min(DP[j - 1][1], DP[j - 1][2]) + paint[j][0]
        DP[j][1] = min(DP[j - 1][2], DP[j - 1][0]) + paint[j][1]
        DP[j][2] = min(DP[j - 1][0], DP[j - 1][1]) + paint[j][2]

    for k in range(3):
        if i != k:
            ans = min(ans, DP[-1][k])

print(ans)