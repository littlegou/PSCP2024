"""ScaledMatrix"""
def main(m,n):
    """main"""
    lis = [float(input()) for _ in range(m*n)]
    c = 1
    for i in lis:
        print(f"{(i+abs(min(lis)))/(abs(max(lis)) + abs(min(lis))):.2f}",end = " ")
        if c < n:
            c += 1
        else:
            print()
            c = 1
main(int(input()),int(input()))
