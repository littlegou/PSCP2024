"""Restaurant"""
def main(a,b,c,d):
    """main"""
    if a + d<b:
        new = a+d
    else:
        new = (a + d)*(1-(c/100))
    x = a - new
    sam = new - (a*(1-(c/100)))
    if not x or not c or not d:
        print("Yes")
    elif a == b:
        if sam>0:
            print(f"No {sam:.3f}")
        elif sam<0:
            print(f"Yes {abs(sam):.3f}")
        else:
            print("Yes")
    elif x == a:
        print("Yes")
    elif x>0:
        print(f"Yes {x:.3f}")
    elif x<0:
        print(f"No {abs(x):.3f}")
main(float(input()),float(input()),float(input()),float(input()))
