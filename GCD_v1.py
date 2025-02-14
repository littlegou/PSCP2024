"""GCD_v1"""
def main(n,m):
    """main"""
    for i in range(min(n,m) if n and m else max(n,m),0,-1):
        if not n%i and not m%i:
            print(i)
            break
main(int(input()),int(input()))
