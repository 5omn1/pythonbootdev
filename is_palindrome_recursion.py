def main():
    def is_palindrome(word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return is_palindrome(word[1:-1])

    test_words = ["racecar", "hello", "level", "world", "madam"]
    for word in test_words:
        if is_palindrome(word):
            print(f'"{word}" is a palindrome.')
        else:
            print(f'"{word}" is not a palindrome.')


if __name__ == "__main__":
    main()
