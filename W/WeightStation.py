"""WeightStation"""
def main(avg,x,y,z):
    """main"""
    sumw = x+y+z
    allw = avg*4
    a = (allw)-sumw
    if (allw)/1000>15:
        print("Overweight")
    elif abs(avg-x)>avg/2 or abs(avg-y)>avg/2 or abs(avg-z)>avg/2 or abs(avg-a)>avg/2:
        print("Unbalance")
    else:
        print(f"Pass {a:.2f}")
main(float(input()),float(input()),float(input()),float(input()))
