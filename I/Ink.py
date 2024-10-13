"""Ink"""
import math
def main(n):
    """main"""
    for _ in range(int(n[1])):
        a = input().split()
        l = math.sqrt((int(a[0])**2)+(int(a[1])**2))
        area = 3.1416*l*l
        print(math.ceil(area/int(n[0])))
main(input().split())
