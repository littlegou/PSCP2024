"""Discount"""
from math import floor
def main(n):
    """Discount"""
    lis = []
    while n!="ENTER":
        lis.append(int(n))
        n = input()
    lis.sort()
    if len(lis)<=5:
        print(sum(lis))
    elif 6 <= len(lis) < 12:
        print(sum(lis[1:]))
    elif 20 > len(lis) >= 12:
        print(sum(lis[2:]))
    elif len(lis) == 20:
        print(sum(lis[4:]))
    else:
        print(sum(lis[(floor((len(lis)-20)/5)+4):]))
main(input())
