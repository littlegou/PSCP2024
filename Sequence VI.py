"""Sequence VI"""
def main(n):
    """main"""
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print()
main(int(input()))
