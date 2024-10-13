"""[Final 2021] DigitMatrix"""
from math import ceil
def num(a,b,c,d,e):
    """num"""
    ans = 0
    if a == "    *" and b == "    *" and c == "    *" and d == "    *" and e == "    *":
        ans = 1
    elif a == "*****" and b == "    *" and c == "*****" and e == "*****" and d == "*    ":
        ans = 2
    elif a == "*****" and c == "*****" and e == "*****" and b == "    *" and d == "    *":
        ans = 3
    elif a == "*   *" and b == "*   *" and c == "*****" and d == "    *" and e == "    *":
        ans = 4
    elif a == "*****" and c == "*****" and e == "*****" and d == "    *" and b == "*    ":
        ans = 5
    elif a == "*****" and c == "*****" and e == "*****" and d == "*   *" and b == "*    ":
        ans = 6
    elif a == "*****" and b == "    *" and c == "    *" and d == "    *" and e == "    *":
        ans = 7
    elif a == "*****" and c == "*****" and e == "*****" and d == "*   *" and b == "*   *":
        ans = 8
    elif a == "*****" and c == "*****" and e == "*****" and b == "*   *" and d == "    *":
        ans = 9
    return ans
def math(a,b,c,d,e):
    """math"""
    if (a == "  *  " and b == "  *  " and d == "  *  " and e == "  *  ") and c == "*****":
        return "+"
    if (a == "*   *" and e == "*   *") and (b == " * * " and d == " * * ") and c == "  *  ":
        return "*"
    if (a == "     " and b == "     " and d == "     " and e == "     ") and c == "*****":
        return "-"
    if (a == "  *  " and e == "  *  ") and (b == "     " and d == "     ") and c == "*****":
        return "/"
    return None
def main():
    """[Final 2021] DigitMatrix"""
    lis = [input(),input(),input(),input(),input()]
    l = num(lis[0][:5],lis[1][:5],lis[2][:5],lis[3][:5],lis[4][:5])
    r = num(lis[0][-5:],lis[1][-5:],lis[2][-5:],lis[3][-5:],lis[4][-5:])
    if math(lis[0][7:12],lis[1][7:12],lis[2][7:12],lis[3][7:12],lis[4][7:12]) == "+":
        print(l+r)
    elif math(lis[0][7:12],lis[1][7:12],lis[2][7:12],lis[3][7:12],lis[4][7:12]) == "-":
        print(l-r)
    elif math(lis[0][7:12],lis[1][7:12],lis[2][7:12],lis[3][7:12],lis[4][7:12]) == "*":
        print(ceil(l*r))
    elif math(lis[0][7:12],lis[1][7:12],lis[2][7:12],lis[3][7:12],lis[4][7:12]) == "/":
        print(ceil(l/r) if r else "Error")
main()
