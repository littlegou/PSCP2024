"""Easy Histogram"""
def main(sen):
    """main"""
    dic = {}
    for i in sen:
        if i not in dic and not i.isspace():
            dic[i] = 1
        elif not i.isspace():
            dic[i] += 1
    dic = sorted(dic.items(),key = lambda x:(x[0].lower(),x[0].isupper()))
    for i in dic:
        print(i[0] + " = " + str(i[1]))
main(input())
