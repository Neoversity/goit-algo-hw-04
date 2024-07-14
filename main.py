import timeit
import random


# Реалізація алгоритму сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Злиття двох половин
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Додавання залишків лівої половини
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Додавання залишків правої половини
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Реалізація алгоритму сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Пересування елементів масиву, що більші за ключ
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Функція для заміру часу виконання алгоритму сортування
def measure_time(sort_function, data):
    return timeit.repeat(lambda: sort_function(data.copy()), repeat=3, number=1)


# Функція для генерації різних наборів даних
def generate_data(size):
    random_data = random.sample(range(size * 10), size)
    sorted_data = sorted(random_data)
    partially_sorted_data = sorted_data[: size // 2] + random.sample(
        range(size * 10), size // 2
    )
    reversed_data = sorted_data[::-1]
    return random_data, sorted_data, partially_sorted_data, reversed_data


def main():
    data_sizes = [100, 1000, 5000, 10000]
    results = {}

    for size in data_sizes:
        random_data, sorted_data, partially_sorted_data, reversed_data = generate_data(
            size
        )
        datasets = {
            "random": random_data,
            "sorted": sorted_data,
            "partially_sorted": partially_sorted_data,
            "reversed": reversed_data,
        }

        results[size] = {}
        for dataset_name, data in datasets.items():
            results[size][dataset_name] = {
                "merge_sort": measure_time(merge_sort, data),
                "insertion_sort": measure_time(insertion_sort, data),
                "timsort": measure_time(sorted, data),
            }

    # Виведення результатів
    for size, result in results.items():
        print(f"Data size: {size}")
        for dataset_name, times in result.items():
            print(f"Dataset: {dataset_name}")
            for sort_type, sort_times in times.items():
                print(f" {sort_type}: {min(sort_times)} seconds")


if __name__ == "__main__":
    main()
