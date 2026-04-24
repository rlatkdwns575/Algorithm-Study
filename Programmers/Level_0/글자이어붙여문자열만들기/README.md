# 글자 이어 붙여 문자열 만들기

## 문제 설명

문자열 `my_string`과 정수 배열 `index_list`가 주어집니다.

`index_list`에 들어있는 인덱스에 해당하는 `my_string`의 문자들을  
순서대로 이어 붙여 새로운 문자열을 만드는 문제입니다.

## 제한 사항

- `1 ≤ my_string의 길이 ≤ 1,000`
- `my_string`은 영소문자로만 구성
- `1 ≤ index_list의 길이 ≤ 1,000`
- `0 ≤ index_list[i] < my_string.length`

## 입출력 예

| my_string | index_list | result |
|----------|------------|--------|
| "cvsgiorszzzmrpaqpe" | [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7] | "programmers" |
| "zpiaz" | [1, 2, 0, 0, 3] | "pizza" |

## 문제 풀이

문제 자체는 간단하게 인덱스를 순회하면서 해당 위치의 문자를 이어 붙이면 됩니다.

기존 코드처럼 `String`에 `+=`을 사용하는 방식도 동작은 하지만,  
자바에서는 문자열이 불변 객체이기 때문에 매번 새로운 객체가 생성됩니다.

즉, 반복문에서 `+=`을 계속 사용하면 성능이 비효율적입니다.

따라서 문자열을 이어 붙일 때는 `StringBuilder`를 사용하는 것이 정석입니다.

### 사용된 메서드 정리

- `charAt(index)`
  - 문자열에서 특정 인덱스의 문자를 가져옵니다.

- `StringBuilder.append()`
  - 문자열을 효율적으로 이어 붙입니다.

- `StringBuilder.toString()`
  - 최종 결과를 문자열로 변환합니다.

## 풀이 코드

```java
class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder sb = new StringBuilder();

        for (int idx : index_list) {
            sb.append(my_string.charAt(idx));
        }

        return sb.toString();
    }
}
