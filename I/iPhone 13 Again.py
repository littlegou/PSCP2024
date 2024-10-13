"""iPhone 13 Again"""
def mini(a,b):
    """mini"""
    if a == "iPhone 13 mini":
        if b == "128 GB":
            print(25900)
        elif b == "256 GB":
            print(29900)
        elif b == "512 GB":
            print(37900)
        else:
            print("Not Available")
    elif a == "iPhone 13":
        if b == "128 GB":
            print(29900)
        elif b == "256 GB":
            print(33900)
        elif b == "512 GB":
            print(41900)
        else:
            print("Not Available")
def promax(a,b):
    """promax"""
    if a == "iPhone 13 Pro":
        if b == "128 GB":
            print(38900)
        elif b == "256 GB":
            print(42900)
        elif b == "512 GB":
            print(50900)
        elif b == "1 TB":
            print(58900)
        else:
            print("Not Available")
    elif a == "iPhone 13 Pro Max":
        if b == "128 GB":
            print(42900)
        elif b == "256 GB":
            print(46900)
        elif b == "512 GB":
            print(54900)
        elif b == "1 TB":
            print(62900)
        else:
            print("Not Available")
def main():
    """main"""
    iphone = input()
    gbtb = input()
    if iphone in ("iPhone 13 mini","iPhone 13"):
        mini(iphone,gbtb)
    elif iphone in ("iPhone 13 Pro","iPhone 13 Pro Max"):
        promax(iphone,gbtb)
    else:
        print("Not Available")
main()
