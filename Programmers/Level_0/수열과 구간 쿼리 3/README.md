# 수열과 구간 쿼리 3

## 문제 설명

정수 배열 `arr`와 2차원 정수 배열 `queries`이 주어집니다. `queries`의 원소는 각각 하나의 query를 나타내며, `[i, j]` 꼴입니다.

각 query마다 순서대로 `arr[i]`의 값과 `arr[j]`의 값을 서로 바꿉니다.

위 규칙에 따라 `queries`를 처리한 이후의 `arr`를 return 하는 `solution` 함수를 완성해 주세요.

## 제한사항

- `1 ≤ arr`의 길이 `≤ 1,000`
- `0 ≤ arr`의 원소 `≤ 1,000,000`
- `1 ≤ queries`의 길이 `≤ 1,000`
- `0 ≤ i < j < arr`의 길이

## 입출력 예

| arr | queries | result |
|---|---|---|
| `[0, 1, 2, 3, 4]` | `[[0, 3], [1, 2], [1, 4]]` | `[3, 4, 1, 0, 2]` |

## 입출력 예 설명

### 입출력 예 #1

각 쿼리에 따라 `arr`가 다음과 같이 변합니다.

| arr |
|---|
| `[0, 1, 2, 3, 4]` |
| `[3, 1, 2, 0, 4]` |
| `[3, 2, 1, 0, 4]` |
| `[3, 4, 1, 0, 2]` |

따라서 `[3, 4, 1, 0, 2]`를 return 합니다.

## 문제 풀이

이 문제는 `queries`에 들어 있는 각 구간 정보를 순서대로 확인하면서, 해당 인덱스의 두 원소를 서로 바꾸는 문제입니다.

각 query는 `[i, j]` 형태로 주어지므로,  
현재 query에서 `i = query[0]`, `j = query[1]`로 꺼낸 뒤 `arr[i]`와 `arr[j]`를 swap 하면 됩니다.

원소를 서로 바꿀 때는 임시 변수 `temp`를 사용합니다.

```java
int temp = answer[i];
answer[i] = answer[j];
answer[j] = temp;
```

또한 문제에서는 원본 배열 `arr`를 직접 수정해도 되지만, 현재 코드는 `Arrays.copyOf()`를 사용해 `arr`를 복사한 뒤 `answer`에서 작업하고 있습니다.

```java
int[] answer = Arrays.copyOf(arr, arr.length);
```

이렇게 하면 원본 배열은 유지한 채 복사본만 변경할 수 있습니다.

즉, 전체 과정은 다음과 같습니다.

1. `arr`를 복사해 `answer` 배열 생성
2. `queries`를 하나씩 순회
3. 각 query의 두 인덱스를 구함
4. 해당 위치의 값을 서로 교환
5. 모든 query 처리 후 `answer` 반환

## 풀이 코드

```java
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);

        for (int[] query : queries) {
            int i = query[0];
            int j = query[1];

            int temp = answer[i];
            answer[i] = answer[j];
            answer[j] = temp;
        }

        return answer;
    }
}
```
