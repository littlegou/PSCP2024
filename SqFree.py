"""SqFree"""
import math
def main(n):
    """main"""
    lis = list(range(1, n + 1))
    for i in range(2,math.ceil(n**0.5)+1):
        for j in lis:
            if not j % (i**2):
                lis.remove(j)
    print(len(lis))
main(int(input()))
