"""HorizontalHistogram"""
import math
def main(sen):
    """main"""
    dic = {}
    for i in sen:
        if i not in dic and not i.isspace():
            dic[i] = "-"
        elif not i.isspace():
            dic[i] += "-"
    dic = sorted(dic.items(),key = lambda x:(ord(x[0])<97,x[0]))
    for i in dic:
        print(i[0],":",end=" ")
        ans = f"{i[1]:<{math.ceil(len(i[1])/5)*5}}"
        realans = ""
        for j in range(math.ceil(len(ans)/5)):
            realans += ans[j*5:(j+1)*5] + "|"
        if realans[-1] == "|":
            print(realans[:-1])
        else:
            print(realans)
main(input())
