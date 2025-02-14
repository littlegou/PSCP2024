"""All_Primes"""
def main(n):
    """main"""
    count = 0
    for j in range(2,n+1):
        check = 0
        for i in range(2,j):
            if not j%i:
                check = 1
                break
        if not check:
            count += 1
    print(count)
main(int(input()))
