"""Scout"""
def cal(lis,p,q):
    """cal"""
    lis.sort()
    while sum(lis)>q:
        lis.pop()
    if len(lis)>p:
        return p
    return len(lis)
def main(s):
    """main"""
    for _ in range(s):
        a = input().split()
        p , q = int(a[1]) , int(a[2])
        lis = list(map(float,input().split()))
        print(cal(lis,p,q))
main(int(input()))
