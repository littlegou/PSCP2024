"""diamond"""
def main(n):
    """main"""
    for i in range(int(-(n/2-0.5)),int(n/2+0.5)):
        for j in range(int(-(n/2-0.5)),int(n/2+0.5)):
            if not i:
                print("*",end = "")
            elif abs(j) == abs((n/2-0.5)-abs(i)):
                print("*",end = "")
            else:
                print(" ",end = "")
        print()
main(int(input()))
