"""[Recommend] Bubble"""
def checobig(sentence):
    """check"""
    pas = 0
    br = 0
    c = 0
    if sentence[1] == "|" or sentence[2] == "|" or sentence[3] == "|":
        br = 1
    elif sentence[3] == "O":
        pas = 3
    elif sentence[2] == "O":
        pas = 2
    elif sentence[1] == "O":
        pas = 1
    elif sentence[3] == "o":
        pas = 3
    elif sentence[2] == "o":
        pas = 2
    elif sentence[1] == "o":
        pas = 1
    if pas:
        c = 1
    return pas,br,c
def checko(sentence):
    """check"""
    pas = 0
    br = 0
    c = 0
    if sentence[1] == "|":
        br = 1
    elif sentence[1] != " ":
        pas = 1
    if pas:
        c = 1
    return pas,br,c
def main(sent):
    """main"""
    sen = sent
    paas = 0
    count = 0
    for i in sen:
        if i in ("o","^") and not paas:
            paas , check , co = checko(sen)
            count += co
            if check:
                print("POSSIBLE")
                print(count+1)
                break
            if not paas:
                print("IMPOSSIBLE")
                print(len(sen)-1)
                break
        elif i == "O" and not paas:
            paas , check , co= checobig(sen)
            count += co
            if check:
                print("POSSIBLE")
                print(count+1)
                break
            if not paas:
                print("IMPOSSIBLE")
                print(len(sen)-1)
                break
        if paas>0:
            sen = sen.replace(sen[0],"",1)
            paas -= 1
main(input())
