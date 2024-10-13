"""Perfect City"""
import math
def main(xnow,ynow,x,y):
    """main"""
    ma_x = abs(math.ceil(max(xnow,x))-x) + abs(math.ceil(max(xnow,x))-xnow)
    ma_x1 = abs(math.ceil(min(xnow,x))-x) + abs(math.ceil(min(xnow,x))-xnow)
    mi_n = abs(math.floor(min(xnow,x))-x) + abs(math.floor(min(xnow,x))-xnow)
    mi_n1 = abs(math.floor(max(xnow,x))-x) + abs(math.floor(max(xnow,x))-xnow)
    max2 = abs(math.ceil(max(ynow,y))-y) + abs(math.ceil(max(ynow,y))-ynow)
    max3 = abs(math.ceil(min(ynow,y))-y) + abs(math.ceil(min(ynow,y))-ynow)
    min2 = abs(math.floor(min(ynow,x))-y) + abs(math.floor(min(ynow,y))-ynow)
    min3 = abs(math.floor(max(ynow,x))-y) + abs(math.floor(max(ynow,y))-ynow)
    ans = min(ma_x,mi_n,mi_n1,ma_x1)+  min(max2,min2,max3,min3)
    print(f"{ans:.2f}")
main(float(input()),float(input()),float(input()),float(input()))
