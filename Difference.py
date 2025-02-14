"""Difference"""
def main(n,m):
    """main"""
    a , b = set() , set()
    for _ in range(n):
        num = int(input())
        a.add(num)
    for _ in range(m):
        num = int(input())
        b.add(num)
    c = sorted(a-b)
    print(*c)
main(int(input()),int(input()))
