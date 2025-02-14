"""Sequence XII"""
def main(n):
    """main"""
    lis = []
    for i in range(1,n+1):
        a = n-i+1
        oth = []
        cn = 0
        for _ in range(1,n+1):
            if a == n:
                cn+=1
            if a<n and cn<1:
                oth.append(a)
                a += 1
            elif a>=i:
                oth.append(a)
                a -= 1
            elif a<n and cn>=1:
                oth.append(a)
                a += 1
        lis.append(oth)
    newlis = []
    you = len(lis)
    for h in range(you):
        a = lis[h]
        newlis.append(a + a[-2::-1])
    for x in newlis:
        for v in x:
            print(f"{int(v):>02} ",end="")
        print()
    for x in newlis[-2::-1]:
        for v in x:
            print(f"{int(v):>02} ",end="")
        print()
main(int(input()))
