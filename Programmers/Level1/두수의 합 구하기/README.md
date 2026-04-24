# 두 수의 합 구하기

## 문제 설명

정수 `num1`과 `num2`가 주어질 때,  
두 수의 합을 return하는 문제입니다.

## 제한 사항

- `-50,000 ≤ num1 ≤ 50,000`
- `-50,000 ≤ num2 ≤ 50,000`

## 입출력 예

| num1 | num2 | result |
|---|---|---|
| 2 | 3 | 5 |
| 100 | 2 | 102 |

## 문제 풀이

두 정수 `num1`과 `num2`를 더한 값을 그대로 반환하면 됩니다.

### 사용된 연산자 정리

- `+`
  - 두 수를 더하는 산술 연산자입니다.

## 풀이 코드

```java
class Solution {
    public int solution(int num1, int num2) {
        return num1 + num2;
    }
}
