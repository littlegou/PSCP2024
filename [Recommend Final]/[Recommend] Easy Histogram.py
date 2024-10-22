"""[Recommend] Easy Histogram"""
def main(sen):
    """[Recommend] Easy Histogram"""
    dic = {}
    for i in sen:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    dic = list(sorted(dic.items(),key=lambda x:(x[0].lower(),x[0].isupper())))
    for i in dic:
        print(f"{i[0]} = {i[1]}")
main(input().replace(" ",""))
