"""Sequence IX"""
def main(n):
    """main"""
    for i in range(1,n+1):
        a = 1
        b = i-1
        for j in range(1,n+i):
            if j<= n-i:
                print("  ",end = " ")
            else:
                if a<=i:
                    print(f"{a:>02}",end = " ")
                    a+=1
                else:
                    print(f"{b:>02}",end = " ")
                    b-=1
        print()
main(int(input()))
