"""ชีวะจักรโบราณ"""
def cal(dic,num):
    """cal"""
    x = num
    count = 0
    ans = ""
    while num//9 >= 1:
        count += 1
        num /= 9
    ans += "bagingu " * count
    num = x
    for i in range(8,0,-1):
        if (int(9**count))*i<num:
            if i == 1:
                ans = ans[:-3] + "do "*bool(ans[:-3])
            ans += dic[i]*bool(dic[i]!="papan") + "do "*bool(dic[i]!="papan")
            num -= (int(9**count))*i
            a , num = cal(dic,num)
            ans += a
            break
        if (int(9**count))*i==num:
            if i == 1:
                ans = ans[:-3] + "do "*bool(ans[:-3])
            ans += dic[i]*(bool(dic[i]!="papan") or bool(not num-1)) + " "
            num -= (int(9**count))*i
            break
    if int(num)>0:
        ans += dic[int(num)]
    return ans,num
def main(num):
    """ชีวะจักรโบราณ"""
    dic = {0:"zezeso",1:"papan",2:"dogugu",3:"gushigi",4:"zugogo",\
5:"zugagi",6:"gibugu",7:"gezun",8:"gegido",9:"bagin"}
    if num<=9:
        print(dic[num])
    elif num <= 17:
        print("bagindo " + dic[num-9])
    else:
        ans = cal(dic,num)
        ans = ans[0].strip()
        if ans[-2:] == "do" and ans[-4:-2] != "gi":
            ans = ans[:-2].strip()
        print(ans[:-2] if ans[-2:] == "do" and ans[-4:-2] != "gi" else ans)
main(int(input()))
