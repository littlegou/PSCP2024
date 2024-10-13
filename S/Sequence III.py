"""Sequence III"""
def main(x):
    """main"""
    for i in range(2,x+2):
        for j in range(i,i+x):
            print(j,end = " ")
        print()
main(int(input()))
