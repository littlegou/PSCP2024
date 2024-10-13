"""DNA"""
def finda(l,aa,bb):
    """finda"""
    ans = ""
    for i in range(l,-1,-1):
        for j in range(l+1):
            if i+j>l:
                break
            x = aa[j:j+i]
            if bb.find(x) != -1 and len(x)>len(ans):
                ans = x
    return ans
def findb(l,aa,bb):
    """findb"""
    ans = ""
    for i in range(l,-1,-1):
        for j in range(l+1):
            if i+j>l:
                break
            x = bb[j:j+i]
            if aa.find(x) != -1 and len(x)>len(ans):
                ans = x
    return ans
def main(a,b):
    """DNA"""
    la = len(a)
    lb = len(b)
    for i in a+b:
        if i not in ("C","T","A","G"):
            print("Error")
            return
    ans1 = finda(lb,a,b)
    ans2 = findb(la,a,b)
    if not ans1 and not ans2:
        print("None")
    elif len(ans1)>=len(ans2):
        print(ans1)
    else:
        print(ans2)
main(input(),input())
