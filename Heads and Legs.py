"""Heads and Legs"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    rab = (b-2*a)/2
    if int(rab) == rab and int(rab)>=0 and int(a-rab)>=0:
        print(int(rab),int(a-rab))
    else:
        print("Impossible")
main()
