"""Majority"""
def main():
    """main"""
    candi = int(input())
    voter = int(input())
    dic = {}
    for i in range(1,candi+1):
        dic[i] = 0
    for i in range(voter):
        point = int(input())
        dic[point] =  dic[point] + 1
    lis = list(dic.items())
    lis.sort(key = lambda x:x[1],reverse=True)
    score = lis[0][1]
    num = lis[0][0]
    if score>=voter/2:
        print(num,score)
    else:
        print(0,score)
main()
