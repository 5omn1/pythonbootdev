def main():
    def insertion_sort(nums):
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        return nums

    arr = [1, 7, 5, 3, 4, 9, 10, 15, 22, 24, 13, 14, 11]
    print(insertion_sort(arr))

if __name__ == "__main__":
    main()
