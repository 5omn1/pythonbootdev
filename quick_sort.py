def main():
    def quick_sort(nums, low, high):
         if low < high:
            p = partition(nums, low, high)
            quick_sort(nums, low, p - 1)
            quick_sort(nums, p + 1, high)

    def partition(nums, low, high):
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1


    tests = [
        [9, 3, 7, 1, 8, 2, 5],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [4, 2, 4, 4, 1, 2, 4],
        [42],
        [2, 1],
        [-3, 10, 0, -7, 5, 2],
    ]

    for arr in tests:
        quick_sort(arr, 0, len(arr) - 1)
        print(arr)


if __name__ == "__main__":
    main()
