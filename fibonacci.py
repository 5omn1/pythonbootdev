def main():
    def fib(n):
        if n < 2:
            return n
        a = 0
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    print(fib(5))
    print(fib(20))
if __name__ == "__main__":
    main()
