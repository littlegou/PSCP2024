"""MAC"""
def one(le,sent):
    """one"""
    if sent[5] == "-" and sent[8] == "-" and sent[11] == "-" and sent[14] == "-":
        for i in range(le):
            if i not in (2,5,8,11,14):
                if sent[i].isnumeric() or 65 <= ord(sent[i]) <= 70 or 97 <= ord(sent[i]) <= 102:
                    pass
                else:
                    print("ERROR")
                    return
        print("VALID 1")
    else:
        print("ERROR")
def two(le,sent):
    """two"""
    if sent[5] == ":" and sent[8] == ":" and sent[11] == ":" and sent[14] == ":":
        for i in range(le):
            if i not in (2,5,8,11,14):
                if sent[i].isnumeric() or 65 <= ord(sent[i]) <= 70 or 97 <= ord(sent[i]) <= 102:
                    pass
                else:
                    print("ERROR")
                    return
        print("VALID 2")
    else:
        print("ERROR")
def thr(le,sent):
    """thr"""
    if sent[9] == ".":
        for i in range(le):
            if i not in (4,9):
                if sent[i].isnumeric() or 65 <= ord(sent[i]) <= 70 or 97 <= ord(sent[i]) <= 102:
                    pass
                else:
                    print("ERROR")
                    return
        print("VALID 3")
    else:
        print("ERROR")
def main(sen):
    """main"""
    l = len(sen)
    if l<2:
        print("ERROR")
    elif l == 17 and sen[2] == "-":
        one(l,sen)
    elif l == 17 and sen[2] == ":":
        two(l,sen)
    elif l<4:
        print("ERROR")
    elif l == 14 and sen[4] == ".":
        thr(l,sen)
    else:
        print("ERROR")
main(input())
