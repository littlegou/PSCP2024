"""[Recommend] Easy Histogram"""
def ans(dic):
    """findans"""
    for i in dic:
        # print(i[1])
        if len(i[1]) == 1:
            # print(i[1][0])
            # print(i[1][0][0])
            print(f"{i[1][0][0]} = {len(i[1][0])}")
        elif len(i[1]) == 2:
            # print(i[1][0])
            # print(i[1][0][0])
            # print(i[1][1][0])
            print(f"{i[1][0][0]} = {len(i[1][0])}")
            print(f"{i[1][1][0]} = {len(i[1][1])}")
def main(sen):
    """[Recommend] Easy Histogram"""
    dic = {}
    for i in sen:
        if i.isspace():
            continue
        if i.lower() not in dic:
            # print(dic)
            dic[i.lower()] = [i]
            # print(dic[i.lower()])
        elif len(dic[i.lower()]) == 1:
            # print(dic[i.lower()])
            if i in dic[i.lower()][0]:
                dic[i.lower()][0] += i
            elif dic[i.lower()][0].islower():
                dic[i.lower()].append(i)
            elif dic[i.lower()][0].isupper():
                dic[i.lower()].insert(0,i)
        elif len(dic[i.lower()]) == 2:
            # print(dic[i.lower()])
            if i.islower():
                dic[i.lower()][0] += i
            elif i.isupper():
                dic[i.lower()][1] += i
    dic = sorted(dic.items())
    # print(dic)
    ans(dic)
main(input())
