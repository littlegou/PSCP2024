"""Guess"""
def cal(n,lis):
    """cal"""
    ans = None
    if n[0] == ">" and n[2] == "YES":
        ans = [i for i in lis if i > int(n[1])]
    elif n[0] == ">" and n[2] == "NO":
        ans = [i for i in lis if i <= int(n[1])]
    if n[0] == ">=" and n[2] == "YES":
        ans = [i for i in lis if i >= int(n[1])]
    elif n[0] == ">=" and n[2] == "NO":
        ans = [i for i in lis if i < int(n[1])]
    elif n[0] == "<" and n[2] == "YES":
        ans = [i for i in lis if i < int(n[1])]
    elif n[0] == "<" and n[2] == "NO":
        ans = [i for i in lis if i >= int(n[1])]
    elif n[0] == "<=" and n[2] == "YES":
        ans = [i for i in lis if i <= int(n[1])]
    elif n[0] == "<=" and n[2] == "NO":
        ans = [i for i in lis if i > int(n[1])]
    elif n[0] == "=" and n[2] == "YES":
        ans = [int(n[1])]
    elif n[0] == "=" and n[2] == "NO":
        ans = [i for i in lis if i != int(n[1])]
    return ans
def main(n):
    """Guess"""
    lis = list(range(0,101))
    while n != "END":
        lis = cal(n.split(),lis)
        n = input()
    print(*lis)
main(input())
