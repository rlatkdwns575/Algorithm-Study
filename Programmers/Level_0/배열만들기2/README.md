# 배열 만들기 2

## 문제 설명

정수 `l`과 `r`이 주어졌을 때, `l` 이상 `r` 이하의 정수 중에서 숫자 `"0"`과 `"5"`로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 `solution` 함수를 완성해 주세요.

만약 그러한 정수가 없다면, `-1`이 담긴 배열을 return 합니다.

## 제한사항

- `1 ≤ l ≤ r ≤ 1,000,000`

## 입출력 예

| l | r | result |
|---|---|---|
| 5 | 555 | `[5, 50, 55, 500, 505, 550, 555]` |
| 10 | 20 | `[-1]` |

## 입출력 예 설명

### 입출력 예 #1

`5` 이상 `555` 이하의 `0`과 `5`로만 이루어진 정수는 작은 수부터 `5`, `50`, `55`, `500`, `505`, `550`, `555`가 있습니다. 따라서 `[5, 50, 55, 500, 505, 550, 555]`를 return 합니다.

### 입출력 예 #2

`10` 이상 `20` 이하이면서 `0`과 `5`로만 이루어진 정수는 없습니다. 따라서 `[-1]`을 return 합니다.

## 문제 풀이

이 문제는 `l`부터 `r`까지의 모든 수를 하나씩 확인하면서, 각 수가 **오직 0과 5로만 이루어져 있는지** 검사하면 되는 문제입니다.

먼저 조건을 만족하는 수들을 저장하기 위해 `ArrayList<Integer>`를 사용합니다.

```java
ArrayList<Integer> list = new ArrayList<>();
```

그 다음 `l`부터 `r`까지 반복하면서 현재 수 `i`를 검사합니다.  
각 수를 `num`에 저장한 뒤, 자릿수를 하나씩 확인하기 위해 `while (num > 0)` 반복문을 사용합니다.

```java
int temp = num % 10;
```

이 코드는 현재 수의 마지막 자릿수를 구하는 부분입니다.  
이 자릿수가 `0`도 아니고 `5`도 아니라면 조건을 만족하지 않는 수이므로 `flag = false`로 바꾸고 반복을 중단합니다.

반대로 모든 자릿수가 끝까지 `0` 또는 `5`라면 `flag`는 계속 `true`로 유지되고, 그 수는 조건에 맞는 수이므로 리스트에 추가합니다.

```java
if (flag) {
    list.add(i);
}
```

모든 수를 확인한 뒤에도 리스트가 비어 있다면, 조건에 맞는 수가 하나도 없다는 뜻이므로 `[-1]`을 반환합니다.

```java
if (list.isEmpty()) {
    return new int[] {-1};
}
```

리스트에 값이 들어 있다면, 마지막에는 `ArrayList`의 값을 일반 배열 `int[]`로 옮겨 담아 반환합니다.

현재 코드는 이 과정을 그대로 잘 구현한 정답 코드입니다.

## 풀이 코드

```java
import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = l; i <= r; i++) {
            int num = i;
            boolean flag = true;

            while (num > 0) {
                int temp = num % 10;

                if (temp != 0 && temp != 5) {
                    flag = false;
                    break;
                }

                num /= 10;
            }

            if (flag) {
                list.add(i);
            }
        }

        if (list.isEmpty()) {
            return new int[] {-1};
        }

        int[] answer = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
```
