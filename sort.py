import random


def generate_array(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


def print_array(arr):
    parts = []
    for i in range(len(arr)):
        parts.append(f"[cell - {i},value - {arr[i]}]")
    print("{" + ",".join(parts) + "}")


def wrong_order(a, b, ascending):
    if ascending:
        return a > b
    return a < b


def bubble_sort(arr, ascending):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if wrong_order(arr[j], arr[j + 1], ascending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr, ascending):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and wrong_order(arr[j], key, ascending):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr, ascending):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if wrong_order(arr[best], arr[j], ascending):
                best = j
        arr[i], arr[best] = arr[best], arr[i]
    return arr


if __name__ == "__main__":
    numbers = generate_array(10, -20, 50)

    print("Початковий масив:")
    print_array(numbers)

    print("\nBubble sort (за зростанням):")
    print_array(bubble_sort(numbers, True))
    print("Bubble sort (за спаданням):")
    print_array(bubble_sort(numbers, False))

    print("\nInsertion sort (за зростанням):")
    print_array(insertion_sort(numbers, True))
    print("Insertion sort (за спаданням):")
    print_array(insertion_sort(numbers, False))

    print("\nSelection sort (за зростанням):")
    print_array(selection_sort(numbers, True))
    print("Selection sort (за спаданням):")
    print_array(selection_sort(numbers, False))