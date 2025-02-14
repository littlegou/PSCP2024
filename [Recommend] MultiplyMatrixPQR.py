"""[Recommend] MultiplyMatrixPQR"""
def main(p,q,r):
    """[Recommend] MultiplyMatrixPQR"""
    m1 = [[int(input()) for _ in range(q)] for _ in range(p)]
    m2 = [[int(input()) for _ in range(r)] for _ in range(q)]
    for i in range(p):
        for j in range(r):
            ans = 0
            for k in range(q):
                ans += m1[i][k] * m2[k][j]
            print(ans,end=" ")
        print()
main(int(input()),int(input()),int(input()))
