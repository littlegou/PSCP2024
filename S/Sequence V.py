"""Sequence V"""
def main(n):
    """main"""
    line = n//7
    if n%7>0:
        line += 1
    i = 0
    while i <line:
        j = 0
        while j<7:
            if n>=1:
                print(n,end=" ")
                n-=1
            else:
                break
            j+=1
        print()
        i+=1
main(int(input()))
