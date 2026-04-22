# 문자열 바꿔서 찾기

## 문제 설명

문자 `"A"`와 `"B"`로 이루어진 문자열 `myString`과 `pat`가 주어집니다. `myString`의 `"A"`를 `"B"`로, `"B"`를 `"A"`로 바꾼 문자열의 연속하는 부분 문자열 중 `pat`이 있으면 `1`을, 아니면 `0`을 return 하는 `solution` 함수를 완성하세요.

## 제한사항

- `1 ≤ myString`의 길이 `≤ 100`
- `1 ≤ pat`의 길이 `≤ 10`
- `myString`과 `pat`는 문자 `"A"`와 `"B"`로만 이루어진 문자열입니다.

## 입출력 예

| myString | pat | result |
|---|---|---:|
| `"ABBAA"` | `"AABB"` | 1 |
| `"ABAB"` | `"ABAB"` | 0 |

## 입출력 예 설명

### 입출력 예 #1

`"ABBAA"`에서 `"A"`와 `"B"`를 서로 바꾸면 `"BAABB"`입니다. 여기에는 부분 문자열 `"AABB"`가 있기 때문에 `1`을 return 합니다.

### 입출력 예 #2

`"ABAB"`에서 `"A"`와 `"B"`를 서로 바꾸면 `"BABA"`입니다. 여기에는 부분 문자열 `"ABAB"`가 없기 때문에 `0`을 return 합니다.

## 문제 풀이

이 문제는 먼저 문자열 `myString` 안의 모든 `"A"`를 `"B"`로, `"B"`를 `"A"`로 바꾼 뒤, 바뀐 문자열 안에 `pat`이 부분 문자열로 존재하는지 확인하면 됩니다.

첫 번째 방법은 문자열을 문자 하나씩 순회하면서 직접 바꾼 결과 문자열을 만드는 방식입니다. 각 문자를 확인해서 현재 문자가 `'A'`이면 `'B'`를 붙이고, `'B'`이면 `'A'`를 붙이면 뒤바뀐 문자열을 만들 수 있습니다. 이후 `contains()`를 사용해 `pat`이 포함되어 있는지 검사하면 됩니다.

두 번째 방법은 문자열 치환 메서드를 활용하는 것입니다. 다만 `"A"`를 바로 `"B"`로 바꾸고 다시 `"B"`를 `"A"`로 바꾸면 처음 바뀐 값까지 함께 바뀌는 문제가 생길 수 있으므로, 중간에 소문자 `"a"` 같은 임시 문자를 거쳐 순서대로 치환해야 합니다. 예를 들어 `"A" → "a"`, `"B" → "A"`, `"a" → "B"` 순서로 바꾸면 원하는 결과를 얻을 수 있습니다.

두 방법 모두 정답이지만, 첫 번째 방법은 동작 원리를 직접 확인하기 좋고, 두 번째 방법은 코드가 더 짧고 간단하다는 장점이 있습니다.

## 풀이 코드 1

```java
class Solution {
    public int solution(String myString, String pat) {
        String result = "";
        for (char c : myString.toCharArray()) {
            if (c == 'A') {
                result += 'B';
            } else if (c == 'B') {
                result += 'A';
            }
        }
        return result.contains(pat) ? 1 : 0;
    }
}
```

## 풀이 코드 2

```java
class Solution {
    public int solution(String myString, String pat) {
        myString = myString.replace("A", "a").replace("B", "A").replace("a", "B");
        return myString.contains(pat) ? 1 : 0;
    }
}
```
