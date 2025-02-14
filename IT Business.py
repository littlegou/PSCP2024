"""IT Business"""
def main(bank,cash,n):
    """main"""
    err = 0
    while n != "end":
        hm = ""
        todo = ""
        todo = n[0]
        hm = n[2:]
        if todo == "D":
            if cash - float(hm)>=0:
                cash -= float(hm)
                bank += float(hm)
                err = 0
            else:
                err += 1
        elif todo == "W":
            if bank - float(hm)>=0:
                bank -= float(hm)
                cash += float(hm)
                err = 0
            else:
                err += 1
        else:
            err += 1
        if err>=3:
            break
        n = input()
    print(f"{bank:.2f}")
    print(f"{cash:.2f}")
main(float(input()),float(input()),input())
