def main():
    def find_longest_word(document, longest_word=""):
        if len(document) == 0:
            return longest_word
        words = document.split(maxsplit=1)
        if len(words) < 1:
            return longest_word
        first_word = words[0]
        if len(first_word) >= len(longest_word):
            longest_word = first_word
        if len(words) < 2:
            return longest_word
        return find_longest_word(words[1], longest_word)

    test1_input = ""
    test2_input = "How are you ?"
    test3_input = "The quick brown fox jumped over the lazy dog"
    print(find_longest_word(test1_input))  # Expected output: ""
    print(find_longest_word(test2_input))  # Expected output: "you"
    print(find_longest_word(test3_input))  # Expected output: "jumped"


if __name__ == "__main__":
    main()
