"""Water"""
def cal(a,b,c,d,x):
    """cal"""
    ans = 0
    if x>b:
        ans = ((x-b)*c)+(b*a)
    else:
        ans = x * a
    if ans<=d:
        ans = 0
    return ans
def main(n,a,b,c,d):
    """Water"""
    ans = 0
    for _ in range(n):
        ans += cal(a,b,c,d,float(input()))
    print(f"{ans:.2f}")
main(int(input()),float(input()),float(input()),float(input()),float(input()))
