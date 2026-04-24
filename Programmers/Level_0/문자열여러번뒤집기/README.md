# 문자열 여러 번 뒤집기

## 문제 설명

문자열 `my_string`과 2차원 정수 배열 `queries`가 주어집니다.

`queries`의 각 원소는 `[s, e]` 형태이며,  
이는 문자열의 인덱스 `s`부터 `e`까지의 구간을 뒤집으라는 의미입니다.

모든 쿼리를 순서대로 처리한 뒤의 문자열을 반환하는 문제입니다.

## 제한 사항

- `my_string`은 영소문자로만 이루어져 있습니다.
- `1 ≤ my_string의 길이 ≤ 1,000`
- `1 ≤ queries의 길이 ≤ 1,000`
- `queries[i] = [s, e]`
- `0 ≤ s ≤ e < my_string.length()`

## 입출력 예

| my_string | queries | result |
|---|---|---|
| "rermgorpsam" | [[2, 3], [0, 7], [5, 9], [6, 10]] | "programmers" |

## 문제 풀이

문자열은 직접 수정할 수 없기 때문에 먼저 `char[]` 배열로 변환합니다.

이후 각 쿼리마다 시작 인덱스 `s`와 끝 인덱스 `e`를 가져오고,  
양쪽 끝 문자를 서로 교환하면서 구간을 뒤집습니다.

예를 들어 `[s, e]` 구간을 뒤집을 때는 다음과 같이 처리합니다.

- `s` 위치 문자와 `e` 위치 문자를 교환
- `s + 1` 위치 문자와 `e - 1` 위치 문자를 교환
- 가운데까지 반복

구간 뒤집기가 모두 끝나면 `char[]` 배열을 다시 문자열로 변환해 반환합니다.

### 사용된 메서드 정리

- `toCharArray()`
  - 문자열을 문자 배열로 변환합니다.

- `new String(charArray)`
  - 문자 배열을 문자열로 변환합니다.

- 임시 변수 `temp`
  - 두 문자의 위치를 바꿀 때 사용합니다.

## 풀이 코드

```java
class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] answer = my_string.toCharArray();

        for (int[] rule : queries) {
            int s = rule[0];
            int e = rule[1];

            int p = (e - s) / 2;

            for (int i = 0; i <= p; i++) {
                char temp = answer[s + i];
                answer[s + i] = answer[e - i];
                answer[e - i] = temp;
            }
        }

        return new String(answer);
    }
}
