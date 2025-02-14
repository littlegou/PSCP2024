"""LetterFrequency"""
def main(sen):
    """main"""
    dic = {}
    for i in sen:
        if i.lower().isalpha() and i.lower() not in dic:
            dic[i.lower()] = 1
        elif i.lower().isalpha():
            dic[i.lower()] += 1
    dic = sorted(dic.items(),key = lambda x:-x[1])
    print(dic[0][0])
main(input())
