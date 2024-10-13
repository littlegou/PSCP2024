"""Bubble"""
def check(a):
    """ch"""
    if a[3] == "O" or a[3] == "|":
        o = 2
    elif a[2] == "O" or a[2] == "|":
        o = 1
    elif a[1] == "O" or a[1] == "|":
        o = 0
    elif a[3] != " ":
        o = 2
    elif a[2] != " ":
        o = 1
    elif a[1] != " ":
        o = 0
    else:
        o = -1
    return o
def small(a,b):
    """small"""
    if a.rstrip() != "|":
        how = len(a.rstrip())
        print("IMPOSSIBLE")
        print(how)
    else:
        print("POSSIBLE")
        print(b)
def main(bubb):
    """main"""
    count = 1
    bubble = bubb[1:]+"  "
    l = len(bubb[1:])
    yo = 0
    for _ in range(l):
        if yo>0:
            bubble = bubble[1:]
            yo -= 1
        elif bubble[0] == "o":
            if bubble[1] == " ":
                bubble = bubble[1:]
                break
            bubble = bubble[1:]
            count += 1
        elif bubble[0] == "O":
            yo = check(bubble)
            if yo == -1:
                bubble = bubble[1:]
                break
            bubble = bubble[1:]
            count += 1
        elif bubble[0] == "|":
            break
    small(bubble,count)
main(input())
