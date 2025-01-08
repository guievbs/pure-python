from typing import List

numbers: List[int] = range(1, 1001)


def binary_search(numbers: List[int], pick: int) -> int | None:
    if numbers is None:
        return None

    high: int = len(numbers) - 1
    low: int = 0
    steps: int = 0

    while low <= high:
        steps += 1
        mid: int = (high + low) // 2
        guess = numbers[mid]

        if guess == pick:
            return f"index: {mid}, total of steps: {steps}"
        if guess > pick:
            print("High")
            high = mid - 1
        else:
            print("Low")
            low = mid + 1

    return None


print(binary_search(numbers=numbers, pick=1))
print(binary_search(numbers=numbers, pick=558))
print(binary_search(numbers=numbers, pick=998))
print(binary_search(numbers=numbers, pick=-1))
