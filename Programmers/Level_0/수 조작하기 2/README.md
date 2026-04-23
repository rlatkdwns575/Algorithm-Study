# 수 조작하기 2

## 문제 설명

정수 배열 `numLog`가 주어집니다. 처음에 `numLog[0]`에서부터 시작해 `"w"`, `"a"`, `"s"`, `"d"`로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

- `"w"` : 수에 1을 더한다.
- `"s"` : 수에 1을 뺀다.
- `"d"` : 수에 10을 더한다.
- `"a"` : 수에 10을 뺀다.

그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 `numLog`입니다. 즉, `numLog[i]`는 `numLog[0]`로부터 총 `i`번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 `numLog`에 대해 조작을 위해 입력받은 문자열을 return 하는 `solution` 함수를 완성해 주세요.

## 제한사항

- `2 ≤ numLog`의 길이 `≤ 100,000`
- `-100,000 ≤ numLog[0] ≤ 100,000`
- `1 ≤ i ≤ numLog`의 길이인 모든 `i`에 대해 `|numLog[i] - numLog[i - 1]|`의 값은 `1` 또는 `10`입니다.

## 입출력 예

| numLog | result |
|---|---|
| `[0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]` | `"wsdawsdassw"` |

## 입출력 예 설명

### 입출력 예 #1

`result`인 `"wsdawsdassw"`를 따라 `numLog[0]`에서부터 시작해 조작을 하면 `numLog`의 값과 순서대로 일치합니다. 따라서 `"wsdawsdassw"`를 return 합니다.

## 문제 풀이

이 문제는 현재 값과 이전 값의 차이를 구해서, 그 차이에 맞는 조작 문자를 찾아 이어 붙이면 되는 문제입니다.

`numLog[i]`는 `numLog[0]`에서부터 i번 조작한 결과이므로, 인접한 두 값의 차이를 보면 어떤 조작이 이루어졌는지 알 수 있습니다.

차이는 다음과 같이 대응됩니다.

- `1`이면 `"w"`
- `-1`이면 `"s"`
- `10`이면 `"d"`
- `-10`이면 `"a"`

따라서 배열의 두 번째 원소부터 끝까지 반복하면서, 현재 값과 이전 값의 차이 `diff`를 구합니다.

```java
int diff = numLog[i] - numLog[i - 1];
```

그리고 `diff`의 값에 따라 알맞은 문자를 `answer` 뒤에 붙이면 됩니다.

이 문제는 바로 이전 문제인 **수 조작하기 1**의 반대 과정이라고 볼 수 있습니다.  
수 조작하기 1에서는 문자열을 보고 숫자를 변화시켰다면, 이 문제에서는 기록된 숫자의 변화를 보고 문자열을 복원하는 방식입니다.

## 풀이 코드

```java
class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        
        for (int i = 1; i < numLog.length; i++) {
            int diff = numLog[i] - numLog[i - 1];
            
            if (diff == 1) {
                answer += 'w';
            } else if (diff == -1) {
                answer += 's';
            } else if (diff == 10) {
                answer += 'd';
            } else if (diff == -10) {
                answer += 'a';
            }
        }
        
        return answer;
    }
}
```
