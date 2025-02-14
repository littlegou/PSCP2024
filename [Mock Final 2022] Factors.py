"""Factors"""
import math
def main(n):
    """Factors"""
    for _ in range(n):
        dic = {}
        a = int(input())
        for i in range(2,math.ceil(a/2)+1):
            while not a%i:
                if i not in dic and not a%i:
                    dic[i] = 1
                    a /= i
                elif not a%i:
                    dic[i] += 1
                    a /= i
        lis = list(dic.items()) if dic.items() else [[str(a),"1"]]
        ans = ""
        for i in lis:
            i = list(map(str,i))
            if i[1] != "1" and i[0] != "1":
                ans += "**".join(i)
            else:
                ans += i[0]
            ans += " x "
        print(ans.strip(" x "))
main(int(input()))
