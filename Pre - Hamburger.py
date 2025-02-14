"""Pre - Hamburger"""
def main(left,right):
    """main"""
    l = left*"|"
    r = right*"|"
    p = ((left+right)*2)*"*"
    print(f"{l}{p}{r}")
main(int(input()),int(input()))
