"""Gram_v1"""
def main(sen):
    """main"""
    yo = sen[0]
    l = len(sen)
    dic = {}
    for i in range(1,l):
        yo += sen[i]
        if yo not in dic:
            dic[yo] = 1
        else:
            dic[yo] = dic[yo] + 1
        yo = sen[i]
    ma = max(dic.values())
    find = list(filter(lambda x:ma==x[1],dic.items()))
    print(find[0][0])
    print(ma)
main(input())
