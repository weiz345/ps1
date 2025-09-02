class Solution:
    def fib_recursive(self, n):
        # helper recursive function for nth Fibonacci number
        def fib(k):
            if k == 0:
                return 0
            elif k == 1:
                return 1
            return fib(k - 1) + fib(k - 2)

        result = []
        for i in range(n):
            result.append(fib(i))
        return result

    def fib_iterative(self, n):
        result = []
        a, b = 0, 1
        for i in range(n):
            result.append(a)
            a, b = b, a + b
        return result
