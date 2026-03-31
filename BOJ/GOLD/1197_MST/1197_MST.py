"""
1197번 최소 스패닝 트리 (골드 4)
input :
    v 정점의 개수, e 간선의 개수
    a, b, c 간선의 연결점과 가중치
output :
    w 스패닝 트리의 가중치
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(e)]

edge.sort(key=lambda x: x[-1])
group = [i for i in range(v + 1)]


def find(num):
    if num != group[num]:
        group[num] = find(group[num])
    return group[num]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        group[b] = a


length = 0
for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        length += c

print(length)