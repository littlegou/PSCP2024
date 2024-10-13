"""[float(input()) 2024] 100 meters"""
def main():
    """main"""
    top1 = float(input())
    r1 = 1
    top2 = float(input())
    r2 = 2
    if top2<top1:
        top1,top2 = top2,top1
        r1,r2 = 2,1
    top3 = float(input())
    r3 = 3
    if top3 < top1:
        top1,top2,top3 = top3,top1,top2
        r1,r2,r3 = 3,r1,r2
    elif top3 < top2:
        top2,top3 = top3,top2
        r2,r3 = 3,r2
    for i in range(4,9):
        a = float(input())
        if a < top1:
            top1,top2,top3 = a,top1,top2
            r1,r2,r3 = i,r1,r2
        elif a < top2:
            top2,top3 = a,top2
            r2,r3 = i,r2
        elif a < top3:
            top3 = a
            r3 = i
    print(f"{r1} {r2} {r3}")
main()
