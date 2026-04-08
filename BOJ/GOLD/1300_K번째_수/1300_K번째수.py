"""
1300번 K번째 수 (골드 1)
input:
    n 배열의 크기 
    k 구해야 하는 인덱스
output:
    bk B[k]의 값
"""
n = int(input())
k = int(input())

ans = 0
left, right = 0, k
while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid// i, n)
    
    if cnt >= k:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)