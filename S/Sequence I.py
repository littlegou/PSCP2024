"""Sequence I"""
def main(n):
    """main"""
    for _ in range(n):
        for i in range(1,n+1):
            print(i,end=" ")
        print()
main(int(input()))
