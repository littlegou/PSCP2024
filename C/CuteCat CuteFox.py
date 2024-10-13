"""CuteCat CuteFox"""
def main():
    """main"""
    n = int(input())
    dic = {}
    for _ in range(n):
        sen = input()
        find = sen.find(" : ")
        left = sen[2:find-1]
        right = sen[find+4:-2]
        dic.update({left:right})
    checkkey = dic.keys()
    checkvalue = dic.values()
    if "Garfield" not in checkkey and "Cat01" not in checkvalue:
        dic.update({"Garfield":"Cat01"})
    if "Fubuki" not in checkkey and "Fox01" not in checkvalue:
        dic.update({"Fubuki":"Fox01"})
    checkkey = dic.keys()
    checkvalue = dic.values()
    cat = 0
    fox = 0
    for i in checkvalue:
        if i[:3] == "Cat":
            cat += 1
        elif i[:3] == "Fox":
            fox += 1
    print(f"Cat : {cat}")
    print(f"Fox : {fox}")
    dic = sorted(dic.items(),key = lambda x:(x[1][0],int(x[1][3:])))
    for i in dic:
        print(f"{i[0]} : {i[1]}")
main()
