"""Pre - Blackjack"""
def tu(a,b):
    """tul"""
    an = 0
    count = 0
    if a == "A":
        count += 1
    elif a in ('J', 'K', 'Q'):
        an += 10
    else:
        an += int(a)
    if b in ('J', 'K', 'Q'):
        an += 10
    elif b == "A":
        count += 1
    else:
        an += int(b)
    if count==2:
        an = 12
    elif count==1:
        if an+11<=21:
            an+=11
        else:
            an+=1
    return an
def check(a,b):
    """check"""
    if a==1:
        if b+11<=21:
            b+=11
        else:
            b+=1
    elif a==2:
        if b+12<=21:
            b+=12
        else:
            b+=2
    elif a==3:
        b = 13
    return b
def se(a,b,c):
    """set"""
    an = 0
    count = 0
    if a == "A":
        count += 1
    elif a in ('J', 'K', 'Q'):
        an += 10
    else:
        an += int(a)
    if b in ('J', 'K', 'Q'):
        an += 10
    elif b == "A":
        count += 1
    else:
        an += int(b)
    if c in ('J', 'K', 'Q'):
        an += 10
    elif c == "A":
        count += 1
    else:
        an += int(c)
    an = check(count,an)
    return an
def main(hm):
    """main"""
    if hm == 2:
        x = input()
        y = input()
        print(tu(x,y))
    elif hm == 3:
        x = input()
        y = input()
        z = input()
        print(se(x,y,z))
main(int(input()))
