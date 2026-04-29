# 뒤집힌 문자열

## 문제 설명

문자열 `my_string`이 매개변수로 주어집니다. `my_string`을 거꾸로 뒤집은 문자열을 return 하도록 `solution` 함수를 완성해주세요.

## 제한사항

- `1 ≤ my_string`의 길이 `≤ 1,000`

## 입출력 예

| my_string | return |
|---|---|
| `"jaron"` | `"noraj"` |
| `"bread"` | `"daerb"` |

## 입출력 예 설명

### 입출력 예 #1

`my_string`이 `"jaron"`이므로 거꾸로 뒤집은 `"noraj"`를 return 합니다.

### 입출력 예 #2

`my_string`이 `"bread"`이므로 거꾸로 뒤집은 `"daerb"`를 return 합니다.

## 문제 풀이

이 문제는 주어진 문자열을 앞뒤 순서를 반대로 뒤집어서 반환하면 되는 문제입니다.

현재 코드는 자바의 `StringBuilder`를 사용해 문자열을 뒤집고 있습니다.

먼저 `StringBuilder` 객체를 만든 뒤, `append()`로 `my_string`을 넣습니다.

```java
StringBuilder sb = new StringBuilder();
sb.append(my_string);
```

그 다음 `reverse()` 메서드를 호출하면 문자열의 순서가 반대로 뒤집힙니다.

```java
sb.reverse();
```

마지막으로 `StringBuilder`는 문자열 객체가 아니므로, `toString()`을 사용해 다시 `String`으로 변환하여 반환하면 됩니다.

이 방법은 직접 반복문으로 문자를 거꾸로 붙이는 것보다 코드가 더 간단하고, 자바에서 문자열 뒤집기에 자주 사용하는 대표적인 방식입니다.

## 풀이 코드

```java
import java.util.*;

class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        sb.append(my_string);
        sb.reverse();

        return sb.toString();
    }
}
```
