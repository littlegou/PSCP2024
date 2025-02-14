"""MultiplyMatrixPQR"""
def main(p,q,r):
    """main"""
    a = []
    b = []
    for i in range(p):
        lis = []
        for j in range(q):
            lis.append(int(input()))
        a.append(lis)
    for i in range(q):
        lis = []
        for j in range(r):
            lis.append(int(input()))
        b.append(lis)
    lisans = []
    for i in range(p):
        lans = []
        for k in range(r):
            ans = 0
            for j in range(q):
                ans += (a[i][j])*(b[j][k])
            lans.append(ans)
        lisans.append(lans)
    for i in lisans:
        print(*i)
main(int(input()),int(input()),int(input()))
