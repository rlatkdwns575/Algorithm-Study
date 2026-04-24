# 분수의 덧셈

## 문제 설명

두 분수 `numer1 / denom1`, `numer2 / denom2`가 주어집니다.

두 분수를 더한 값을 기약분수로 나타냈을 때,  
분자와 분모를 배열에 담아 return하는 문제입니다.

## 제한 사항

- `0 < numer1, denom1, numer2, denom2 < 1,000`

## 입출력 예

| numer1 | denom1 | numer2 | denom2 | result |
|---|---|---|---|---|
| 1 | 2 | 3 | 4 | [5, 4] |
| 9 | 2 | 1 | 3 | [29, 6] |

## 문제 풀이

분수의 덧셈은 분모를 통일한 뒤 분자를 더하는 방식으로 계산합니다.

`numer1 / denom1 + numer2 / denom2`는 다음과 같이 계산할 수 있습니다.

`(numer1 * denom2 + numer2 * denom1) / (denom1 * denom2)`

이렇게 구한 분자와 분모는 아직 약분되지 않은 상태일 수 있습니다.

따라서 분자와 분모의 최대공약수 `gcd`를 구한 뒤,  
분자와 분모를 각각 `gcd`로 나누어 기약분수로 만듭니다.

최대공약수는 유클리드 호제법을 사용했습니다.

유클리드 호제법은 두 수 `a`, `b`에 대해  
`gcd(a, b) = gcd(b, a % b)`를 반복하다가,  
`b`가 0이 되었을 때 `a`를 최대공약수로 반환하는 방식입니다.

## 사용된 문법 및 메서드 정리

- 배열 생성
  - `int[] answer = new int[2];`
  - 분자와 분모를 담을 크기 2의 배열을 생성합니다.

- 분수 덧셈 공식
  - 분자: `numer1 * denom2 + numer2 * denom1`
  - 분모: `denom1 * denom2`

- 재귀 함수
  - 함수 내부에서 자기 자신을 다시 호출하는 방식입니다.
  - 여기서는 최대공약수를 구하는 `gcd()` 함수에 사용했습니다.

- `%`
  - 나머지 연산자입니다.
  - 유클리드 호제법에서 `a % b`를 구할 때 사용합니다.

## 완성 코드

    class Solution {
        public int[] solution(int numer1, int denom1, int numer2, int denom2) {
            int[] answer = new int[2];

            int numer = numer1 * denom2 + numer2 * denom1;
            int denom = denom1 * denom2;
            int g = gcd(numer, denom);

            answer[0] = numer / g;
            answer[1] = denom / g;

            return answer;
        }

        private int gcd(int a, int b) {
            if (b == 0) {
                return a;
            }

            return gcd(b, a % b);
        }
    }

## 한줄 정리

분수 덧셈 후 분자와 분모의 최대공약수를 구해 나누면 기약분수로 만들 수 있습니다.
