"""FibonacciRecursionV2"""
def fib(n):
    """fib"""
    dic = {0:0,1:1}
    if not n:
        return dic.get(n)
    ans = fib(n-1) + fib(n-2)
    dic.update({n:ans})
    return ans
def main(n):
    """main"""
    print(fib(n))
main(int(input()))
