# 1300번 K번쨰 수 (골드 1)

## 1. 문제
세준이는 크기가 N×N인 배열 A를 만들었다. 
배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. 
B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.

## 2. 입력
첫째 줄에 배열의 크기 N이 주어진다. 
N은 105보다 작거나 같은 자연수이다. 
둘째 줄에 k가 주어진다. 
k는 min(109, N2)보다 작거나 같은 자연수이다.

## 3. 출력
B[k]를 출력한다.

## 4. 문제 풀이
일단 그냥 직접 만들어서 해봤는데, 메모리 초과가 나온다.
해당 배열을 생성하면 안된다. 생성하지 않고, 해당 수를 도출해내야 한다.

## >>코드 1. 메모리 초과

```python
"""
3079번 입국심사 (골드 5)
input:
    n 배열의 크기 
    k 구해야 하는 인덱스
output:
    bk B[k]의 값
"""
n = int(input())
k = int(input())

arr = []
for i in range(1, n+1):
    for j in range(1, n+1):
        arr.append(i*j)

arr.sort()
print(arr[k])
```

<img width="609" height="195" alt="image" src="https://github.com/user-attachments/assets/d15788db-8980-4760-adcb-09ecfc61bc49" />

출처: https://edder773.tistory.com/38

해당 문제는 해당 숫자보다 작은 수의 개수를 구하는 규칙성을 찾아내야 풀 수 있는 문제이다.
예시를 보면 N * N 배열에서 특정 수보다 작거나 같은 수를 각각의 행마다 찾아낸다고 가정하자.

각각의 행에서 특정 수인 num = 20 보다 작거나 같은 수는
1행에서는 1~ 20인 1 ~ 20열까지 20개
2행에서는 2~ 20인 1 ~ 10열까지 10개
3행에서는 3~ 18인 1 ~ 6열까지 6개
...
20행에서는 20인 1열까지 1개
위의 분포를 나타내고 있다.

즉 각각의 행에서 작거나 같은 수는 num(기준값) // i (행 번호) 이다.
다만 이 중에는 num // i 가 N보다 큰 경우가 존재할 수 있기 때문에 최대 N까지만 나오도록,
min(num//i, N) 처리를 해줘야 할 필요가 있다.

예시로, 만약 N이 10인데 15를 찾는 경우 1행의 최대 개수는 10개이지만,
num // i는 15가 나와 버린다. 따라서 해당 처리가 필수이다.

 

뭔 이런 문제가 있나 싶긴한데, 이런 문제에 익숙해지면 규칙성을 찾기 쉽지 않을까.. 기대를 해본다.

## >>정답 코드

```python
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
```

## 5. 문제 링크
https://www.acmicpc.net/problem/1300
