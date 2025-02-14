"""Duplicate I"""
def main(m,n):
    """main"""
    set_m , set_n = set() , set()
    for _ in range(m):
        num = input()
        set_m.add(num)
    for _ in range(n):
        num = input()
        set_n.add(num)
    ans = set_m & set_n
    ans = sorted(ans,reverse=True)
    if not ans:
        print("Nope")
    else:
        print(*ans,sep="\n")
main(int(input()),int(input()))
