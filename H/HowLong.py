"""HowLong"""
def main(x):
    """main"""
    coun = 0
    if x<0:
        x = abs(x)
    for i in str(x):
        if i == "-":
            pass
        coun += 1
    print(coun)
main(int(input()))
