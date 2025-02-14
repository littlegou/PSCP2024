"""CircularPrime"""
def prime(n):
    """prime"""
    a = 0
    for i in range(2,int(n**0.5)):
        if not n % i and n != i or not n % 5:
            a = 1
    if not a:
        return n
    return 0
def prime8(n):
    """."""
    lis = [2,3,5,7]
    ans = 0
    for i in lis:
        if i <= n:
            ans += i
    return ans
def main(n):
    """main"""
    lisans = []
    for i in range(2,n+1):
        a = 0
        for j in range(2,int(i**0.5)):
            if not i % j and i != j or not i % 5:
                a = 1
        if not a:
            c = 0
            ax = i
            for _ in range(len(str(i))):
                ax = str(ax)[1:]+str(ax)[0]
                if prime(int(ax)):
                    c+= 1
            if c == len(str(i)):
                lisans.append(i)
    if n <=8:
        print(prime8(n))
    else:
        print(sum(lisans)-27)
main(int(input()))
