"""[Recommend] PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def find(x,y,z):
    """find"""
    ma = 0
    me = 0
    mi = 0
    if x >= y >= z:
        ma,me,mi = x,y,z
    elif x >= z >= y:
        ma,me,mi = x,z,y
    elif y >= x >= z:
        ma,me,mi = y,x,z
    elif y >= z >= x:
        ma,me,mi = y,z,x
    elif z >= y >= x:
        ma,me,mi = z,y,x
    elif z >= x >= y:
        ma,me,mi = z,x,y
    return ma,me,mi
def main(w,a,b,c):
    """main"""
    maa,med,mi = find(a,b,c)
    if w == "Descend":
        print(f"{maa:.2f}, {med:.2f}, {mi:.2f}")
    else:
        print(f"{mi:.2f}, {med:.2f}, {maa:.2f}")
main(input(),float(input()),float(input()),float(input()))
