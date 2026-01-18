def main():
    def powerset(input):
        if not input:
            return [[]]

        all_subsets = [[]]

        for element in input:
            new_subsets = []

            for subset in all_subsets:
                new_subset = subset + [element]
                new_subsets.append(new_subset)

            all_subsets.extend(new_subsets)

        return all_subsets

    test_input = [1,2,3,4]
    print(len(powerset(test_input)))


if __name__ == "__main__":
    main()
