"""[Mock Final 2023] Snake"""
import json
def main(n,lis):
    """[Mock Final 2023] Snake"""
    snake = {3:21,8:30,17:13,28:84,52:29,57:40,58:77,62:22,75:86,80:100,88:18,90:91,95:51,97:79}
    dic = {i:1 for i in range(1,n+1)}
    ind = 0
    lisans = []
    for i in lis:
        dic[list(dic.keys())[ind]] += i
        if dic[list(dic.keys())[ind]] in snake:
            dic[list(dic.keys())[ind]] = snake[dic[list(dic.keys())[ind]]]
        if dic[list(dic.keys())[ind]] >= 100:
            lisans.append(list(dic.keys())[ind])
            dic.pop(list(dic.keys())[ind])
            if not dic:
                break
            if ind>=len(dic):
                ind = 0
        else:
            ind = (ind+1)%len(dic)
    dic =list(sorted(list(dic.items()),key=lambda x:(-int(x[1]),-int(x[0]))))
    if not lisans:
        print(-1)
    else:
        print(*lisans)
    if dic:
        for i in dic:
            print(i[0],end=" ")
main(int(input()),json.loads(input()))
