"""RockPaperScissor"""
def main():
    """main"""
    x = input()
    l = len(x)
    a = 0
    b = 0
    for i in range(0,l,2):
        q = x[i]+x[i+1]
        if q == "RP":
            b += 1
        elif q == "RS":
            a += 1
        elif q == "SP":
            a += 1
        elif q == "PR":
            a += 1
        elif q == "SR":
            b += 1
        elif q == "PS":
            b += 1
        else:
            pass
    if a>b:
        aa = f"{a}"+"-"+f"{b}"
        print(f"A win {aa}")
    elif b>a:
        aa = f"{b}"+"-"+f"{a}"
        print(f"B win {aa}")
    else:
        print(f"DRAW {a}")
main()
