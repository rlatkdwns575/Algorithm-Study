# 수 조작하기 1

## 문제 설명

정수 `n`과 문자열 `control`이 주어집니다. `control`은 `"w"`, `"a"`, `"s"`, `"d"`의 4개의 문자로 이루어져 있으며, `control`의 앞에서부터 순서대로 문자에 따라 `n`의 값을 바꿉니다.

- `"w"` : `n`이 1 커집니다.
- `"s"` : `n`이 1 작아집니다.
- `"d"` : `n`이 10 커집니다.
- `"a"` : `n`이 10 작아집니다.

위 규칙에 따라 `n`을 바꿨을 때 가장 마지막에 나오는 `n`의 값을 return 하는 `solution` 함수를 완성해 주세요.

## 제한사항

- `-100,000 ≤ n ≤ 100,000`
- `1 ≤ control`의 길이 `≤ 100,000`
- `control`은 알파벳 소문자 `"w"`, `"a"`, `"s"`, `"d"`로 이루어진 문자열입니다.

## 입출력 예

| n | control | result |
|---|---|---:|
| 0 | `"wsdawsdassw"` | -1 |

## 입출력 예 설명

### 입출력 예 #1

수 `n`은 `control`에 따라 다음과 같은 순서로 변하게 됩니다.

`0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1`

따라서 `-1`을 return 합니다.

## 문제 풀이

이 문제는 문자열 `control`을 앞에서부터 하나씩 확인하면서, 각 문자에 맞게 정수 `n`의 값을 바꾸면 되는 문제입니다.

문자별 동작은 다음과 같습니다.

- `'w'`이면 현재 값에 `1`을 더함
- `'s'`이면 현재 값에 `1`을 뺌
- `'d'`이면 현재 값에 `10`을 더함
- `'a'`이면 현재 값에 `10`을 뺌

코드에서는 처음 값 `n`을 `answer`에 저장한 뒤, `control.toCharArray()`를 사용해 문자열을 문자 배열로 바꾸고 반복문으로 하나씩 확인합니다.

그리고 `switch`문을 사용해 각 문자에 따라 처리합니다.

- `case 'w'` : `answer += 1`
- `case 's'` : `answer -= 1`
- `case 'd'` : `answer += 10`
- `case 'a'` : `answer -= 10`

이 과정을 문자열 끝까지 반복하면 최종적으로 바뀐 값이 `answer`에 남게 되고, 이를 그대로 반환하면 됩니다.

이 문제는 조건문을 여러 번 쓰는 방법도 있지만, 입력 문자의 종류가 정해져 있으므로 `switch`문을 사용하면 각 경우를 깔끔하게 구분할 수 있습니다.

## 풀이 코드

```java
class Solution { 
    public int solution(int n, String control) {
        int answer = n;

        for (char ch : control.toCharArray()) {
            switch (ch) {
                case 'w': answer += 1; break;
                case 's': answer -= 1; break;
                case 'd': answer += 10; break;
                case 'a': answer -= 10; break;
                default: break;
            }
        }

        return answer;
    }
}
```
