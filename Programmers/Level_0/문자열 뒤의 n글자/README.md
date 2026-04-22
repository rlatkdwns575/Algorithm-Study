# 문자열의 뒤의 n글자

## 문제 설명

문자열 `my_string`과 정수 `n`이 매개변수로 주어질 때, `my_string`의 뒤의 `n`글자로 이루어진 문자열을 return 하는 `solution` 함수를 작성해 주세요.

## 제한사항

- `my_string`은 숫자와 알파벳으로 이루어져 있습니다.
- `1 ≤ my_string`의 길이 `≤ 1,000`
- `1 ≤ n ≤ my_string`의 길이

## 입출력 예

| my_string | n | result |
|---|---:|---|
| `"ProgrammerS123"` | 11 | `"grammerS123"` |
| `"He110W0r1d"` | 5 | `"W0r1d"` |

## 입출력 예 설명

### 입출력 예 #1

예제 1번의 `my_string`에서 뒤의 11글자는 `"grammerS123"`이므로 이 문자열을 return 합니다.

### 입출력 예 #2

예제 2번의 `my_string`에서 뒤의 5글자는 `"W0r1d"`이므로 이 문자열을 return 합니다.

## 문제 풀이

이 문제는 문자열의 **뒤에서부터 n개의 문자만 잘라서 반환**하면 되는 문제입니다.

문자열의 길이를 `length()`로 구할 수 있으므로, 뒤의 `n`글자가 시작되는 위치는 다음과 같이 구할 수 있습니다.

```java
my_string.length() - n
```

자바의 `substring()`은 시작 인덱스부터 문자열 끝까지 잘라낼 수 있으므로, 시작 위치를 `my_string.length() - n`으로 지정하면 원하는 답을 바로 구할 수 있습니다.

즉, 뒤의 `n`글자는 아래와 같이 구할 수 있습니다.

```java
my_string.substring(my_string.length() - n)
```

또한 반복문을 사용해서 뒤의 문자들을 하나씩 이어 붙이는 방식으로도 구현할 수 있습니다. 다만 이 문제에서는 `substring()`을 사용하는 풀이가 더 간단하고 직관적입니다.

## 풀이 코드 1

```java
class Solution {
    public String solution(String my_string, int n) {
        return my_string.substring(my_string.length() - n);
    }
}
```

## 풀이 코드 2

```java
class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int l = my_string.length();
        
        for (int i = l - n; i < l; i++) {
            answer += my_string.charAt(i);
        }
        
        return answer;
    }
}
```
