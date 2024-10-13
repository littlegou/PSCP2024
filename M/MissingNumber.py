"""MissingNumber"""
def main(n,num):
    """main"""
    set_a , set_b = set() , set()
    while num:
        set_a.add(num)
        num = int(input())
    for i in range(1,n+1):
        set_b.add(i)
    ans = sorted(set_b-set_a)
    print(*ans,sep="\n")
main(int(input()),int(input()))
