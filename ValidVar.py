"""ValidVar"""
def check(a):
    """check"""
    if a in ("if","else","elif","while","for"):
        return 1
    if a in ("return","is","in","and","or","from",'as'):
        return 1
    if a in ("pass","not","def","None","True","False","continue","break"):
        return 1
    return 0
def check2(a):
    """check"""
    for i in a.strip():
        if not (i.isalnum() or i == "_"):
            return 1
    return 0
def main(n):
    """main"""
    for _ in range(n):
        x = input()
        if x[0].isnumeric():
            print("Invalid")
        elif check(x.strip()) == 1:
            print("Invalid")
        elif check2(x.strip()) == 1:
            print("Invalid")
        else:
            print("Valid")
main(int(input()))
#isidentifier ez