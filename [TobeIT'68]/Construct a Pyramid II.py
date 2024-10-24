"""Pyramid I"""
def main(n,m):
    """main"""
    n = n*2-1
    for i in range(1,n+1,2):
        a = ("*"*i)
        print(f"{a:^{n}}"*m)
main(int(input()),int(input()))
