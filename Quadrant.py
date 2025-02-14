"""Quadrant"""
def main(x,y):
    """main"""
    if not x and y:
        print("Y")
    elif x and not y:
        print("X")
    elif x>0 and y>0:
        print("Q1")
    elif x>0>y:
        print("Q4")
    elif x<0 and y<0:
        print("Q3")
    elif x<0<y:
        print("Q2")
    elif not x and not y:
        print("O")
main(int(input()),int(input()))
