"""[Final 2021] Music Lover"""
def main(song):
    """[Final 2021] Music Lover"""
    dic = {}
    for i in range(song):
        lis = input().split("-")
        if lis[0] not in dic:
            dic[lis[0]] = [lis[1].strip()]
        else:
            dic[lis[0]].append(lis[1].strip())
    for i in dic.items():
        print(i[0])
        print(*i[1],sep="\n")
main(int(input()))
