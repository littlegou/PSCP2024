"""Counting Stars"""
def main(x):
    """main"""
    a = x
    comet = 0
    gong = 0
    conste = 0
    l = len(x)
    while x.find("~*") != -1 or x.find("*~") != -1 or x.find("*/") != -1 or x.find("**")!= -1:
        for i in range(l):
            if x[i:i+2] == "~*":
                x = x.replace("~*"," ",1)
                comet += 1
                break
            if x[i:i+2] == "*~":
                x = x.replace("*~"," ",1)
                comet += 1
                break
            if x[i:i+2] == "*/":
                x = x.replace("*/"," ",1)
                gong += 1
                break
            if x[i:i+2] == "**":
                x = x.replace("**"," ",1)
                conste += 1
                break
    if x == a:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {conste}\ncomet: {comet}\nshooting star: {gong}")
main(input())
