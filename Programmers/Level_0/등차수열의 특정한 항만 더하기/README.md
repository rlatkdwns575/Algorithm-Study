# 등차수열의 특정한 항만 더하기

## 문제 설명

두 정수 `a`, `d`와 길이가 `n`인 boolean 배열 `included`가 주어집니다. 첫째항이 `a`, 공차가 `d`인 등차수열에서 `included[i]`가 `i + 1`항을 의미할 때, 이 등차수열의 1항부터 n항까지 `included`가 `true`인 항들만 더한 값을 return 하는 `solution` 함수를 작성해 주세요.

## 제한사항

- `1 ≤ a ≤ 100`
- `1 ≤ d ≤ 100`
- `1 ≤ included`의 길이 `≤ 100`
- `included`에는 `true`가 적어도 하나 존재합니다.

## 입출력 예

| a | d | included | result |
|---|---|---|---:|
| 3 | 4 | `[true, false, false, true, true]` | 37 |
| 7 | 1 | `[false, false, false, true, false, false, false]` | 10 |

## 입출력 예 설명

### 입출력 예 #1

예제 1번은 `a`와 `d`가 각각 3, 4이고 `included`의 길이가 5입니다. 이를 표로 나타내면 다음과 같습니다.

| 1항 | 2항 | 3항 | 4항 | 5항 |
|---|---|---|---|---|
| 3 | 7 | 11 | 15 | 19 |

| included |
|---|
| true, false, false, true, true |

따라서 `true`에 해당하는 1항, 4항, 5항을 더한 `3 + 15 + 19 = 37`을 return 합니다.

### 입출력 예 #2

예제 2번은 `a`와 `d`가 각각 7, 1이고 `included`의 길이가 7입니다. 이를 표로 나타내면 다음과 같습니다.

| 1항 | 2항 | 3항 | 4항 | 5항 | 6항 | 7항 |
|---|---|---|---|---|---|---|
| 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| included |
|---|
| false, false, false, true, false, false, false |

따라서 4항만 `true`이므로 `10`을 return 합니다.

## 문제 풀이

이 문제는 첫째항이 `a`, 공차가 `d`인 등차수열을 만들고, 그중에서 `included` 배열에서 `true`로 표시된 항들만 골라 더하면 되는 문제입니다.

등차수열의 `i + 1`번째 항은 다음과 같이 구할 수 있습니다.

```java
a + d * i
```

여기서 배열의 인덱스 `i`는 0부터 시작하므로,  
`included[0]`은 1항, `included[1]`은 2항, `included[2]`는 3항을 의미합니다.

따라서 `for`문으로 `included` 배열을 처음부터 끝까지 확인하면서, 현재 값이 `true`이면 해당 항의 값을 구해서 `answer`에 더하면 됩니다.

즉,

- `included[i] == true` 이면 `a + d * i`를 더함
- `included[i] == false` 이면 넘어감

이 방식으로 등차수열 전체를 따로 배열로 만들지 않고도 바로 합을 구할 수 있습니다.

## 풀이 코드

```java
class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        
        for (int i = 0; i < included.length; i++) {
            if (included[i]) {
                answer += (a + d * i);
            }
        }
        
        return answer;
    }
}
```
