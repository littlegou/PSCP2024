"""CaesarV2"""
def find(x,y):
    """find"""
    se1 = list(x)
    se2 = list(y)
    lis = []
    for i in range(len(x)):
        if se2[i].isalpha() and se1[i].isalpha():
            lis.append((ord(se1[i]) - ord(se2[i])) if ord(se1[i]) - ord(se2[i])>=0 \
            else 26 - abs(ord(se1[i]) - ord(se2[i])))
    if all(lis[0] == int(i) for i in lis):
        return lis[0]
    return 0
def main(senn):
    """main"""
    k = ["what", "when", "why", "which", "this", "there", "where", "the", "is", "am", "are", \
         "you", "we", "they", "he", "she", "it"]
    k = sorted(k,key = lambda x:(len(x),x))
    sen = "".join(j for j in senn if j.isalpha() or j == " ")
    lis = sen.split()
    lis = sorted(lis,key = lambda x:(x[0].lower()))
    lw = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hm = 0
    for i in lis:
        for j in k:
            if len(i) == len(j):
                hm = find(i.lower(),j.lower())
            if hm:
                break
        if hm:
            break
    for i in senn:
        if i.isupper():
            print(up[(up.find(i)-hm)%26],end = "")
        elif i.islower():
            print(lw[(lw.find(i)-hm)%26],end = "")
        else:
            print(i,end = "")
main(input())
