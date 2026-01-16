import time


def main():
    def selection_sort(nums):
        n = len(nums)
        for i in range(n):
            smallest_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[smallest_idx]:
                    smallest_idx = j
            nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        return nums

    tests = [
        [64, 25, 12, 22, 11],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2],
        [7, 7, 7, 7],
        [42],
        [],
        [-10, 3, 0, -5, 8, 2],
    ]

    for arr in tests:
        data = arr.copy()
        start = time.perf_counter()
        selection_sort(data)
        end = time.perf_counter()

        print(f"Input size: {len(arr):2d} | Time: {(end - start):.8f} seconds")



if __name__ == "__main__":
    main()
