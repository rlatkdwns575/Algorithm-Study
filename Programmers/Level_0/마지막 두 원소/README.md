# 마지막 두 원소

## 문제 설명

정수 리스트 `num_list`가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을, 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return 하도록 `solution` 함수를 완성해주세요.

## 제한사항

- `2 ≤ num_list`의 길이 `≤ 10`
- `1 ≤ num_list`의 원소 `≤ 9`

## 입출력 예

| num_list | result |
|---|---|
| `[2, 1, 6]` | `[2, 1, 6, 5]` |
| `[5, 2, 1, 7, 5]` | `[5, 2, 1, 7, 5, 10]` |

## 입출력 예 설명

### 입출력 예 #1

마지막 원소인 `6`이 그전 원소인 `1`보다 크기 때문에 `6 - 1`인 `5`를 추가해 return 합니다.

### 입출력 예 #2

마지막 원소인 `5`가 그전 원소인 `7`보다 크지 않기 때문에 `5`의 두 배인 `10`을 추가해 return 합니다.

## 문제 풀이

이 문제는 기존 배열의 마지막 두 원소를 비교한 뒤, 조건에 맞는 값을 하나 더 붙여 새로운 배열을 반환하면 되는 문제입니다.

먼저 기존 배열보다 길이가 1 큰 새로운 배열 `result`를 만듭니다.  
그 다음 반복문을 사용해 `num_list`의 기존 원소들을 `result`에 그대로 복사합니다.

이후 마지막 원소의 인덱스를 구합니다.

```java
int last_idx = num_list.length - 1;
```

그리고 다음 조건에 따라 새로 들어갈 값을 결정합니다.

- 마지막 원소가 그전 원소보다 크면  
  `마지막 원소 - 그전 원소`
- 그렇지 않으면  
  `마지막 원소 * 2`

마지막으로 계산한 값을 `result`의 마지막 칸에 넣고 반환하면 됩니다.

현재 코드는 이 과정을 그대로 잘 구현한 정답 코드입니다.

## 풀이 코드

```java
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] num_list) {
        int[] result = new int[num_list.length + 1];
        
        for (int i = 0; i < num_list.length; i++) {
            result[i] = num_list[i];
        }
        
        int last_idx = num_list.length - 1;
        
        if (num_list[last_idx] > num_list[last_idx - 1]) {
            result[last_idx + 1] = num_list[last_idx] - num_list[last_idx - 1];
        } else {
            result[last_idx + 1] = num_list[last_idx] * 2;
        }
        
        return result;
    }
}
```
