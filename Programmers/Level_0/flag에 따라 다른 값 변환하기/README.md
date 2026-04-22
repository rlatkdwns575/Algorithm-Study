# flag에 따라 다른 값 반환하기

## 문제 설명

두 정수 `a`, `b`와 boolean 변수 `flag`가 매개변수로 주어질 때,  
`flag`가 `true`이면 `a + b`를, `false`이면 `a - b`를 return 하는 `solution` 함수를 작성해 주세요.

---

## 제한 사항

- `-1,000 ≤ a, b ≤ 1,000`

---

## 입출력 예

| a  | b | flag  | result |
|----|---|-------|--------|
| -4 | 7 | true  | 3      |
| -4 | 7 | false | -11    |

### 입출력 예 설명

#### 입출력 예 #1
예제 1번에서 `flag`가 `true`이므로 `a + b = (-4) + 7 = 3`을 return 합니다.

#### 입출력 예 #2
예제 2번에서 `flag`가 `false`이므로 `a - b = (-4) - 7 = -11`을 return 합니다.

---

## 문제 풀이

이 문제는 `flag`의 값에 따라 서로 다른 연산 결과를 반환하면 됩니다.

- `flag == true` 이면 `a + b`
- `flag == false` 이면 `a - b`

코드에서는 삼항 연산자를 사용하여 이를 한 줄로 간단하게 표현할 수 있습니다.

삼항 연산자의 형태는 다음과 같습니다.

```java
조건식 ? 참일 때 값 : 거짓일 때 값
```

---

## 정답 코드

```java
class Solution {
    public int solution(int a, int b, boolean flag) {
        return flag ? a + b : a - b;
    }
}
```
