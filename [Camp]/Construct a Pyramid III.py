"""Construct a Pyramid III"""
import math
def main(n,m):
    """main"""
    lis = []
    for i in range(1,math.ceil(m/2)+1):
        lis.append(n*2**i-1)
        z = i
    lis.extend(lis[::-1])
    lis.remove(max(lis))
    anslis = []
    for j in range(int((n*(2**z))/2)):
        smlis = []
        for i in lis:
            a = "*"*(i-j*2)
            smlis.append(f"{a:^{i}}")
        anslis.append(smlis)
    for i in anslis[::-1]:
        print("".join(i))
main(int(input()),int(input()))
