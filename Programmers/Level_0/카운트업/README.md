# 카운트 업

## 문제 설명

정수 `start_num`와 `end_num`가 주어질 때, `start_num`부터 `end_num`까지의 숫자를 차례로 담은 리스트를 return 하도록 `solution` 함수를 완성해주세요.

## 제한사항

- `0 ≤ start_num ≤ end_num ≤ 50`

## 입출력 예

| start_num | end_num | result |
|---|---|---|
| 3 | 10 | `[3, 4, 5, 6, 7, 8, 9, 10]` |

## 입출력 예 설명

### 입출력 예 #1

`3`부터 `10`까지의 숫자들을 담은 리스트 `[3, 4, 5, 6, 7, 8, 9, 10]`를 return 합니다.

## 문제 풀이

이 문제는 `start_num`부터 `end_num`까지의 정수를 순서대로 배열에 넣으면 되는 문제입니다.

먼저 `start_num`부터 `end_num`까지 총 몇 개의 숫자가 들어가는지 계산해서 배열의 크기를 정합니다.

```java
end_num - start_num + 1
```

예를 들어 `start_num = 3`, `end_num = 10`이면  
배열의 길이는 `10 - 3 + 1 = 8`이 됩니다.

그 다음 반복문을 돌면서 배열의 각 칸에 값을 채웁니다.  
인덱스 `i`가 0부터 시작하므로, 실제로 넣어야 할 값은 `start_num + i`가 됩니다.

즉,

- `answer[0] = start_num`
- `answer[1] = start_num + 1`
- `answer[2] = start_num + 2`

와 같은 방식으로 끝까지 채우면 됩니다.

현재 코드는 이 과정을 그대로 잘 구현한 정답 코드입니다.

## 풀이 코드

```java
class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[end_num - start_num + 1];
        
        for (int i = 0; i < end_num - start_num + 1; i++) {
            answer[i] = start_num + i;
        }
        
        return answer;
    }
}
```
