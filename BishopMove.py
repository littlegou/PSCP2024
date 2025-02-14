"""BishopMove"""
def main(_,__):
    """BishopMove"""
    bix,biy,xx,yy,ch = int(input()),int(input()),int(input()),int(input()),int(input())
    wx,wy = int(input()),int(input())
    if abs(abs(bix)-abs(wx)) != abs(abs(biy)-abs(wy)):
        print("No")
    else:
        a = (wx <= xx <= bix) and (wy <= yy <= biy)
        b = (wx <= xx <= bix) and (wy >= yy >= biy)
        c = (wx >= xx >= bix) and (wy <= yy <= biy)
        d = (wx >= xx >= bix) and (wy >= yy >= biy)
        if (wx == xx and yy == wy and ch == 1) or (bix == wx and biy == wy):
            print("Yes")
        elif a or b or c or d:
            print("No")
        else:
            print("Yes")
main(int(input()),int(input()))
