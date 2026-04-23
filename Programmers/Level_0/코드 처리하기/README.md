# 코드 처리하기

## 문제 설명

문자열 `code`가 주어집니다.  
`code`를 앞에서부터 읽으면서 만약 문자가 `"1"`이면 `mode`를 바꿉니다. `mode`에 따라 `code`를 읽어가면서 문자열 `ret`을 만들어냅니다.

`mode`는 0과 1이 있으며, `idx`를 0부터 `code`의 길이 - 1까지 1씩 키워나가면서 `code[idx]`의 값에 따라 다음과 같이 행동합니다.

### mode가 0일 때

- `code[idx]`가 `"1"`이 아니면 `idx`가 짝수일 때만 `ret`의 맨 뒤에 `code[idx]`를 추가합니다.
- `code[idx]`가 `"1"`이면 `mode`를 0에서 1로 바꿉니다.

### mode가 1일 때

- `code[idx]`가 `"1"`이 아니면 `idx`가 홀수일 때만 `ret`의 맨 뒤에 `code[idx]`를 추가합니다.
- `code[idx]`가 `"1"`이면 `mode`를 1에서 0으로 바꿉니다.

문자열 `code`를 통해 만들어진 문자열 `ret`를 return 하는 `solution` 함수를 완성해 주세요.

단, 시작할 때 `mode`는 0이며, return 하려는 `ret`가 만약 빈 문자열이라면 대신 `"EMPTY"`를 return 합니다.

## 제한사항

- `1 ≤ code`의 길이 `≤ 100,000`
- `code`는 알파벳 소문자 또는 `"1"`로 이루어진 문자열입니다.

## 입출력 예

| code | result |
|---|---|
| `"abc1abc1abc"` | `"acbac"` |

## 입출력 예 설명

### 입출력 예 #1

`code`의 각 인덱스 `i`에 따라 다음과 같이 `mode`와 `ret`가 변합니다.

| i | code[i] | mode | ret |
|---|---|---|---|
| 0 | `"a"` | 0 | `"a"` |
| 1 | `"b"` | 0 | `"a"` |
| 2 | `"c"` | 0 | `"ac"` |
| 3 | `"1"` | 1 | `"ac"` |
| 4 | `"a"` | 1 | `"ac"` |
| 5 | `"b"` | 1 | `"acb"` |
| 6 | `"c"` | 1 | `"acb"` |
| 7 | `"1"` | 0 | `"acb"` |
| 8 | `"a"` | 0 | `"acba"` |
| 9 | `"b"` | 0 | `"acba"` |
| 10 | `"c"` | 0 | `"acbac"` |

따라서 `"acbac"`을 return 합니다.

## 문제 풀이

이 문제는 문자열을 처음부터 끝까지 순서대로 확인하면서, 현재 `mode` 값에 따라 문자를 골라 `ret`에 추가하는 시뮬레이션 문제입니다.

처음에는 `mode = 0`으로 시작합니다.  
문자를 하나씩 확인하다가 현재 문자가 `'1'`이면 문자를 추가하지 않고 `mode`만 바꿉니다.  
즉, `mode`가 0이면 1로, 1이면 0으로 전환됩니다.

그 외의 문자일 때는 현재 `mode`에 따라 추가 여부가 달라집니다.

- `mode == 0`이면 짝수 인덱스의 문자만 추가
- `mode == 1`이면 홀수 인덱스의 문자만 추가

따라서 반복문으로 `idx`를 0부터 끝까지 증가시키면서,

1. 현재 문자가 `'1'`인지 확인하고  
2. `'1'`이면 `mode`를 반전시키고  
3. `'1'`이 아니면 현재 `mode`와 `idx`의 홀짝을 비교해 `ret`에 추가하면 됩니다.

마지막에는 `ret`가 비어 있는지 확인해야 합니다.  
비어 있다면 문제 조건에 따라 `"EMPTY"`를 반환하고, 비어 있지 않다면 만들어진 문자열 `ret`를 그대로 반환하면 됩니다.

## 풀이 코드

```java
class Solution {
    public String solution(String code) {
        int mode = 0;
        String ret = "";

        for (int idx = 0; idx < code.length(); idx++) {
            if (code.charAt(idx) == '1') {
                mode = 1 - mode;
            } else if (mode == 0 && idx % 2 == 0) {
                ret += code.charAt(idx);
            } else if (mode == 1 && idx % 2 == 1) {
                ret += code.charAt(idx);
            }
        }

        if (ret.equals("")) {
            return "EMPTY";
        } else {
            return ret;
        }
    }
}
```
