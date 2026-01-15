def main():
    def merge_sort(nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        first = merge_sort(nums[:mid])
        second = merge_sort(nums[mid:])
        return merge(first, second)

    def merge(first, second):
        final = []
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1
        while i < len(first):
            final.append(first[i])
            i += 1
        while j < len(second):
            final.append(second[j])
            j += 1
        return final

    arr = [1, 6, 200, 101, 324, 400, 4254, 11, 18, 24, 28]
    print(merge_sort(arr))


if __name__ == "__main__":
    main()
