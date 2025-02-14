"""[Recommend] VerticalHistogram"""
def main(sen):
    """[Recommend] VerticalHistogram"""
    dic = {}
    for i in sen:
        if i.isalpha() and i not in dic:
            dic[i] = 1
        elif i.isalpha():
            dic[i] += 1
    ma_x = max(list(dic.values()))
    lis = list(sorted(dic.keys()))
    for i in range(ma_x,0,-1):
        print(f"{i:>2}  ",end="")
        for j in lis:
            print("* " if i<=dic[j] else "  " ,end="")
        print()
    print("    "+" ".join(lis))
main(input())
