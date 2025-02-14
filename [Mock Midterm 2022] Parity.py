"""Parity"""
def main(bina,ev):
    """Parity"""
    even = 0
    odd = 0
    for i in bina:
        if not int(i)%2:
            even += 1
        else:
            odd += 1
    if ev == "Even":
        if not odd%2:
            bina += "0"
        else:
            bina += "1"
    else:
        if not odd%2:
            bina += "1"
        else:
            bina += "0"
    print(bina)
main(input(),input())
