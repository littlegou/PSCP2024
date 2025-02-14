"""Sequence X"""
def main(n):
    """main"""
    for i in range(1,n+1):
        a = 1
        for j in range(1,n+i):
            if j<= n-i:
                print("  ",end = " ")
            else:
                if j<=n:
                    print(f"{a:>02}",end = " ")
                    if a+1<= i:
                        a += 1
                else:
                    a -= 1
                    print(f"{a:>02}",end = " ")
        print()
    for i in range(n-1,0,-1):
        a = 1
        for j in range(1,n+i):
            if j<= n-i:
                print("  ",end = " ")
            else:
                if j<=n:
                    print(f"{a:>02}",end = " ")
                    if a+1<= i:
                        a += 1
                else:
                    a -= 1
                    print(f"{a:>02}",end = " ")
        print()
main(int(input()))
