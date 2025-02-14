"""Triangle I"""
def find(x,y,z):
    """find"""
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    return z
def main(a,b,c):
    """main"""
    lis = [a,b,c]
    lis.remove(find(a,b,c))
    oth = 0
    wtf = 0
    for i in lis:
        oth += i**2
    for j in lis:
        wtf += j
    if 0.01>= abs((find(a,b,c)**2) - oth) >= 0:
        if wtf>find(a,b,c):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main(float(input()),float(input()),float(input()))
