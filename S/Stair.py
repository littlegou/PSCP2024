"""Stair"""
def main(y,n):
    """main"""
    a = 0
    count = 0
    ch = 0
    for _ in range(n):
        x = int(input())
        if x>y:
            ch += 1
        elif x+a<=y:
            if ch>0:
                pass
            else:
                ch = 0
            a += x
        else:
            count += 1
            a = x
            if ch>0:
                pass
            else:
                ch = 0
    if a <= y:
        count+=1
    if a > y or not count or ch > 0:
        print("NO")
    else:
        print(count)
main(int(input()),int(input()))
