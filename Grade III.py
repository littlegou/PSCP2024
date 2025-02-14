"""Grade III"""
def grade(a):
    """grade"""
    p = 0
    if a>=95:
        p = 4
    elif a>=90:
        p = 3.5
    elif a>=85:
        p = 3
    elif a>=80:
        p = 2.5
    elif a>=75:
        p = 2
    elif a>=70:
        p = 1.5
    elif a>=65:
        p = 1
    elif a>=60:
        p = 0.5
    elif a>=0:
        p = 0
    return p
def main(c):
    """main"""
    su = 0
    for _ in range(c):
        score = float(input())
        su += grade(score)
    ans = f"{float(su/c):.4f}"
    print(f"{ans[:4]}")
main(int(input()))
