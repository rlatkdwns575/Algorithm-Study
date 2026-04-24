# 수열과 구간 쿼리 4

## 문제 설명

정수 배열 `arr`와 2차원 정수 배열 `queries`이 주어집니다. `queries`의 원소는 각각 하나의 query를 나타내며, `[s, e, k]` 꼴입니다.

각 query마다 순서대로 `s ≤ i ≤ e`인 모든 `i`에 대해 `i`가 `k`의 배수이면 `arr[i]`에 1을 더합니다.

위 규칙에 따라 `queries`를 처리한 이후의 `arr`를 return 하는 `solution` 함수를 완성해 주세요.

## 제한사항

- `1 ≤ arr`의 길이 `≤ 1,000`
- `0 ≤ arr`의 원소 `≤ 1,000,000`
- `1 ≤ queries`의 길이 `≤ 1,000`
- `0 ≤ s ≤ e < arr`의 길이
- `0 ≤ k ≤ 5`

## 입출력 예

| arr | queries | result |
|---|---|---|
| `[0, 1, 2, 4, 3]` | `[[0, 4, 1], [0, 3, 2], [0, 3, 3]]` | `[3, 2, 4, 6, 4]` |

## 입출력 예 설명

### 입출력 예 #1

각 쿼리에 따라 `arr`가 다음과 같이 변합니다.

| arr |
|---|
| `[0, 1, 2, 4, 3]` |
| `[1, 2, 3, 5, 4]` |
| `[2, 2, 4, 5, 4]` |
| `[3, 2, 4, 6, 4]` |

따라서 `[3, 2, 4, 6, 4]`를 return 합니다.

## 문제 풀이

이 문제는 각 쿼리마다 주어진 구간 `[s, e]`를 확인하면서, 인덱스 `i`가 `k`의 배수인지 검사한 뒤 조건을 만족하면 해당 위치의 값을 1 증가시키는 문제입니다.

먼저 원본 배열 `arr`를 그대로 수정하지 않고 작업하기 위해 `Arrays.copyOf()`를 사용하여 복사 배열 `answer`를 만듭니다.

```java
int[] answer = Arrays.copyOf(arr, arr.length);
```

그 다음 `queries`를 하나씩 순회하면서 각 쿼리의 값을 꺼냅니다.

- `s` : 시작 인덱스
- `e` : 끝 인덱스
- `k` : 배수 조건

이후 `i`를 `s`부터 `e`까지 반복하면서 `i % k == 0`인지 확인합니다.  
현재 인덱스가 `k`의 배수라면 `answer[i]`에 1을 더합니다.

즉, 한 쿼리마다 다음 과정을 수행합니다.

- 구간 `[s, e]`를 순회
- 각 인덱스 `i`가 `k`의 배수인지 확인
- 배수이면 `answer[i] += 1`

이 작업을 모든 쿼리에 대해 순서대로 반복하면 최종 배열을 구할 수 있습니다.

## 풀이 코드

```java
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        
        for (int[] rule : queries) {
            int s = rule[0], e = rule[1], k = rule[2];
            
            for (int i = s; i <= e; i++) {
                if (i % k == 0) {
                    answer[i] += 1;
                }
            }
        }
        
        return answer;
    }
}
```
