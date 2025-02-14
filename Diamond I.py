"""Diamond I"""
def main(m,n):
    """main"""
    mlis = []
    for i in range(m):
        mlis.append(input().split())
    ans = 0
    realans = 0
    for i in range(n):
        for j in range(m):
            ans += int(mlis[j][i])
        if not realans or realans<ans:
            realans = ans
        ans = 0
    print(realans)
main(int(input()),int(input()))
