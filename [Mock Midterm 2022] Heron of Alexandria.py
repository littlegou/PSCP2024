"""Heron of Alexandria"""
import math
def main(a,b,c):
    """main"""
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"{area:.3f}")
main(float(input()),float(input()),float(input()))
