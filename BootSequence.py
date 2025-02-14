"""BootSequence"""
def main(x):
    """main"""
    i = 1
    while i<x:
        print(f"{i}_",end = "")
        i+=1
    print(x)
main(int(input()))
