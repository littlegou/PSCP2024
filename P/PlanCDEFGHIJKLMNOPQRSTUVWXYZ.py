"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def find(x,y,z):
    """find"""
    if x > y:
        if x > z:
            high = x
            if y > z:
                medi = y
                less = z
            else:
                medi = z
                less = y
        else:
            high = z
            medi = x
            less = y
    else:
        if y > z:
            high = y
            if x > z:
                medi = x
                less = z
            else:
                medi = z
                less = x
        else:
            high = z
            medi = y
            less = x
    return high,medi,less
def main(sor,num1,num2,num3):
    """main"""
    a,b,c = find(num1,num2,num3)
    if sor == "Descend":
        print(f"{a:.2f}, {b:.2f}, {c:.2f}")
    else:
        print(f"{c:.2f}, {b:.2f}, {a:.2f}")
main(input(),float(input()),float(input()),float(input()))
