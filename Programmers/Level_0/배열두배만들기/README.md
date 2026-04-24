# 배열 두배 만들기

## 문제 설명

정수 배열 `numbers`가 매개변수로 주어집니다.

`numbers`의 각 원소를 2배한 원소를 가진 배열을 return하는 문제입니다.

## 제한 사항

- `-10,000 ≤ numbers의 원소 ≤ 10,000`
- `1 ≤ numbers의 길이 ≤ 1,000`

## 입출력 예

| numbers | result |
|---|---|
| [1, 2, 3, 4, 5] | [2, 4, 6, 8, 10] |
| [1, 2, 100, -99, 1, 2, 3] | [2, 4, 200, -198, 2, 4, 6] |

## 문제 풀이

이 문제는 배열의 모든 원소를 하나씩 확인하면서 2를 곱한 값을 새로운 배열에 저장하면 됩니다.

가장 기본적인 방법은 `for문`을 사용하는 것입니다.

배열의 길이만큼 반복하면서 `numbers[i] * 2` 값을 `answer[i]`에 저장하면 됩니다.

또 다른 방법으로는 Java의 `Stream`을 사용할 수 있습니다.

`Arrays.stream(numbers)`로 배열을 스트림으로 변환한 뒤,
`map()`을 이용해 각 원소에 2를 곱하고,
마지막에 `toArray()`로 다시 배열로 변환합니다.

다만 단순 반복 작업에서는 `Stream`보다 `for문`이 성능상 더 안정적입니다.

Stream은 내부적으로 스트림 객체 생성, 람다 함수 호출, 중간 연산 파이프라인 처리, 최종 연산 수행 과정이 추가되기 때문입니다.

반대로 `filter`, `map`, `sorted`처럼 여러 데이터 처리 단계가 이어지는 경우에는 Stream이 코드를 더 간결하게 만들 수 있습니다.

## 사용된 문법 및 메서드 정리

- `for문`
  - 배열의 인덱스를 직접 순회할 때 사용합니다.
  - 단순 반복에서는 가장 빠르고 안정적인 방식입니다.

- `numbers.length`
  - 배열의 길이를 구합니다.

- `Arrays.stream(numbers)`
  - 배열을 스트림으로 변환합니다.
  - `numbers`가 `int[]`이므로 반환 타입은 `IntStream`입니다.

- `map(i -> i * 2)`
  - 스트림의 각 원소를 변환합니다.
  - 여기서는 각 원소에 2를 곱합니다.

- `toArray()`
  - 스트림 처리 결과를 다시 배열로 변환합니다.

## Stream과 IntStream의 차이

`Stream<Integer>`는 객체 스트림입니다.

즉, `Integer` 객체를 다룹니다.

반면 `IntStream`은 기본형 `int` 전용 스트림입니다.

`int` 값을 그대로 다루기 때문에 박싱과 언박싱이 줄어듭니다.

`Arrays.stream(numbers)`에서 `numbers`가 `int[]`이면 결과는 `IntStream`입니다.

따라서 숫자 배열을 처리할 때는 일반 객체 스트림보다 효율적입니다.

## 완성 코드

### 코드 1: for문 방식

    class Solution {
        public int[] solution(int[] numbers) {
            int[] answer = new int[numbers.length];
            
            for (int i = 0; i < numbers.length; i++) {
                answer[i] = numbers[i] * 2;
            }

            return answer;
        }
    }

### 코드 2: Stream 방식

    import java.util.Arrays;

    class Solution {
        public int[] solution(int[] numbers) {
            return Arrays.stream(numbers)
                         .map(i -> i * 2)
                         .toArray();
        }
    }

## 한줄 정리

단순 배열 반복은 `for문`이 가장 안정적이고, 여러 변환 과정이 이어질 때는 `Stream`을 사용하면 코드가 간결해집니다.
