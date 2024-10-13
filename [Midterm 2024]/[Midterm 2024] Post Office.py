"""[Midterm 2024] Post Office"""
def envelop(x):
    """env"""
    a = 0
    if 0<=x<=10:
        a =  16
    elif x<=20:
        a =  18
    elif x<=100:
        a =  23
    elif x<=250:
        a =  28
    elif x<=500:
        a =  33
    elif x<=1000:
        a =  48
    elif x<=2000:
        a =  68
    return a
def package(x):
    """pack"""
    a = 0
    if 0<=x<=500:
        a = 45
    elif x<=1000:
        a = 55
    elif x<=2000:
        a = 70
    return a
def main(env,pack):
    """main"""
    ans = 0
    for _ in range(env):
        ans += envelop(float(input()))
    ans += 13*env + 15*pack
    for _ in range(pack):
        ans += package(float(input()))
    print(ans)
main(int(input()),int(input()))
