"""DataSpike"""
def cal(x,y):
    """cal"""
    if x<y:
        x = y
    return x
def main():
    """main"""
    one = int(input())
    two = int(input())
    thr = int(input())
    fou = int(input())
    fiv = int(input())
    six = int(input())
    sev = int(input())
    eig = int(input())
    ans = one
    ans = cal(ans,two)
    ans = cal(ans,thr)
    ans = cal(ans,fou)
    ans = cal(ans,fiv)
    ans = cal(ans,six)
    ans = cal(ans,sev)
    ans = cal(ans,eig)
    print(ans)
main()
