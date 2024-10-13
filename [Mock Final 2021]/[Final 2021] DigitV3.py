"""[Final 2021] DigitV3"""
def pep8(x,dic):
    """pep8"""
    lis = []
    while " " in x:
        lis.append(dic[x[:x.find(" ")]])
        x = x[x.find(" "):].strip()
    lis.append(dic[x])
    if len(lis) == 2:
        return lis[0]+lis[1]
    if len(lis) == 1:
        return lis[0]
    return None
def cal(x):
    """cal"""
    lis = []
    dic = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,\
"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,\
"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,\
"sixty":60,"seventy":70,"eighty":80,"ninety":90,"hundred":100,"thousand":1000}
    if "thousand" in x:
        while " " in x:
            lis.append(dic[x[:x.find(" ")]])
            x = x[x.find(" "):].strip()
        lis.append(1000)
        if len(lis) == 3:
            return (lis[0] + lis[1])*lis[2]
        if len(lis) == 2:
            return lis[0]*lis[1]
        if len(lis) == 1:
            return lis[0]
    elif "hundred" in x:
        while " " in x:
            lis.append(dic[x[:x.find(" ")]])
            x = x[x.find(" "):].strip()
        lis.append(100)
        if len(lis) == 2:
            return lis[0]*lis[1]
        if len(lis) == 1:
            return lis[0]
    else:
        return pep8(x,dic)
    return None
def main(sen):
    """[Final 2021] DigitV3"""
    ans = 0
    if "thousand" in sen:
        ans += cal(sen[:sen.find(" thousand")+10])
        sen = sen[sen.find(" thousand")+10:].strip()
    if "hundred" in sen:
        ans += cal(sen[:sen.find(" hundred")+8])
        sen = sen[sen.find(" hundred")+8:].strip()
    if sen:
        ans += cal(sen)
    print(ans)
main(input())
