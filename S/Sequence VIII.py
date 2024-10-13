"""Sequence VIII"""
def main(n):
    """main"""
    for i in range(1,n+1):
        a = 1
        for j in range(1,n+1):
            if j<= n-i:
                print("  ",end = " ")
            else:
                print(f"{a:>02}",end = " ")
                a+=1
        print()
main(int(input()))
