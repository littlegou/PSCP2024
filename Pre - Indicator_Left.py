"""Pre - Indicator_Left"""
import math
def main(k,n):
    """main"""
    half = math.floor(n/2)
    asd = half
    star = "*"*k
    while asd>0:
        yo = asd
        for j in range(half):
            if j!=yo-1:
                print(" ",end="")
            else:
                print(f" {star}")
                break
        asd -= 1
    print(star)
    for i in range(half):
        for j in range(i+1):
            if j!=i:
                print(" ",end="")
            else:
                print(f" {star}")
                break
main(int(input()),int(input()))
