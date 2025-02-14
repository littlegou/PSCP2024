"""[Mock Midterm 2022] Volleyball"""
def sco(a,b,se,seta,setb):
    """main"""
    if a > b:
        print(f"Set {se}: A ({a}) | B ({b})")
        return seta+1,setb,se+1,0,0
    if b > a:
        print(f"Set {se}: A ({a}) | B ({b})")
        return seta,setb+1,se+1,0,0
    return None
def winner(seta,setb):
    """win"""
    if seta == 3:
        print(f"A won 3:{setb} set")
        return 1
    if setb == 3:
        print(f"B won 3:{seta} set")
        return 1
    return 0
def last(a,b,seta,setb,se):
    """last"""
    if seta == 3:
        print(f"A won 3:{setb} set")
    elif setb == 3:
        print(f"B won 3:{seta} set")
    else:
        if not a and not b:
            print(f"Set {se}: A (0) | B (0)")
        else:
            print(f"Set {se}: A ({a}) | B ({b})")
        print("The game has not finished yet.")
def main(s):
    """main"""
    a = 0
    b = 0
    se_t = 1
    seta = 0
    setb = 0
    for i in s:
        if i == "A":
            a += 1
        elif i == "B":
            b += 1
        if se_t < 5 and ((a == 25 and b<=23) or (b == 25 and a <= 23)):
            seta,setb,se_t,a,b = sco(a,b,se_t,seta,setb)
            yo = winner(seta,setb)
            if yo:
                return
        elif se_t < 5 and (a >=24 and b>=24 and abs(a-b) == 2):
            seta,setb,se_t,a,b = sco(a,b,se_t,seta,setb)
            yo = winner(seta,setb)
            if yo:
                return
        elif se_t == 5 and ((a == 15 and b<=13) or (b == 15 and a <= 13)):
            seta,setb,se_t,a,b = sco(a,b,se_t,seta,setb)
            yo = winner(seta,setb)
            if yo:
                return
        elif se_t == 5 and (a >=14 and b>=14 and abs(a-b) == 2):
            seta,setb,se_t,a,b = sco(a,b,se_t,seta,setb)
            yo = winner(seta,setb)
            if yo:
                return
    last(a,b,seta,setb,se_t)
main(input())
