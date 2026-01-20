def main():
    def is_balanced(str):
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in str:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack

    print(is_balanced(""))          # True
    print(is_balanced("()"))        # True
    print(is_balanced("("))         # False
    print(is_balanced(")"))         # False

    print(is_balanced("()()"))      # True
    print(is_balanced("(())"))      # True
    print(is_balanced("(()"))       # False
    print(is_balanced("())"))       # False

    print(is_balanced(")("))        # False
    print(is_balanced("())(()"))    # False

    print(is_balanced("a(b)c"))     # True
    print(is_balanced("a(b))c"))    # False


if __name__ == "__main__":
    main()
