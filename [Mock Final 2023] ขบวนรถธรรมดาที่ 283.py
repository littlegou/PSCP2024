"""ขบวนรถธรรมดาที่ 283"""
def main(lis):
    """ขบวนรถธรรมดาที่ 283"""
    if lis[0] != lis[1]:
        n = input()
        dic = {}
        while n != "Done":
            n = n.split(", ")
            if n[0] in (lis[0],lis[1]):
                dic[n[0]] = float(n[1])
            if len(dic) == 2:
                break
            n = input()
        e_nd = dic.get(lis[1],"No")
        s_t = dic.get(lis[0],"No")
        if e_nd == "No" or s_t == "No":
            print("Error")
        else:
            print(f"{abs(float(e_nd)-float(s_t)):.2f}")
    else:
        print("0.00")
main(input().split(", "))
