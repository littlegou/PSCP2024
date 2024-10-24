"""[Recommend] Cat Parade"""
def main(n):
    """[Recommend] Cat Parade"""
    dic = {}
    count = 0
    while n != "END":
        if n == "IT'S A DOG":
            count -= 1
            dic.popitem()
        else:
            for i in n.split(", "):
                count += 1
                if i not in dic:
                    dic[i] = [count,1]
                else:
                    dic[i][1] += 1
        n = input()
    for i in sorted(dic.items()):
        print(f"{i[0]} {i[1][0]} {i[1][1]}")
main(input())
