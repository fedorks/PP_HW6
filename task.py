from typing import List

def binary_search(arr: List[int], number: int) -> int:

# Бинарный поиск элемента в отсортированном целочисленном массиве.

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    # На вход подаем целочисленный массив
    arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]

    print(f"Исходный массив: {arr}")
    number = int(input("Введите искомый элемент: "))
    result = binary_search(arr, number)

    if result == -1:
        print("Искомого элемента нет в массиве")
    else:
        print(f"Искомый элемент: {number} находится по индексу: {result}")

main()
