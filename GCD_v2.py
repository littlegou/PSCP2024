"""GCD_v1"""
def main(n,m):
    """main"""
    while True:
        if not n or not m:
            print(max(n,m))
            break
        if n > m:
            n -= m
        elif n < m:
            m -= n
        else:
            print(m)
            break
main(int(input()),int(input()))
