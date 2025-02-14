"""HW_DotE"""
import math
def cal(m,n):
    """cal"""
    return math.factorial(m)/(math.factorial(m-n)*math.factorial(n))
def main(n):
    """main"""
    if not n%2:
        ans = cal(n,int(n/2))
    else:
        ans = cal(n,math.ceil(n/2)) + cal(n,math.floor(n/2))
    print(int(ans))
main(int(input()))
