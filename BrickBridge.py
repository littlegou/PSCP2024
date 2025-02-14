"""BrickBridge"""
def main(a,b,c):
    """main"""
    if b*5+a<c:
        print(-1)
    else:
        buse = c//5
        if buse>b:
            tt = buse-b
        else:
            tt = 0
        ause = c%5+tt*5
        if ause>a:
            print(-1)
        else:
            print(ause)
main(int(input()),int(input()),int(input()))
