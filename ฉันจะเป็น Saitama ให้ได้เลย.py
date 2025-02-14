"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    aa = int(input())
    bb = int(input())
    cc = int(input())
    dd = int(input())
    day = 0
    if math.ceil(a/aa) > day:
        day = math.ceil(a/aa)
    if math.ceil(b/bb) > day:
        day = math.ceil(b/bb)
    if math.ceil(c/dd) > day:
        day = math.ceil(c/dd)
    if math.ceil(d/cc) > day:
        day = math.ceil(d/cc)
    print(math.ceil(day))
main()
