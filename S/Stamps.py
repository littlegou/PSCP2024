"""Stamps"""
def main():
    """main"""
    n = int(input())
    a = int(input()) #ครบทุกๆ a บาท
    b = int(input()) #ได้แสดมป์สะสม b ดวง
    c = int(input()) #แสตมป์ครบทุกๆ c ดวง
    d = int(input()) #ส่วนลด d บาท
    stamp = 0
    ans = 0
    bill = 0
    for _ in range(n):
        while stamp >= c and bill >0:
            bill -= d
            stamp -= c
            if bill <0:
                bill = 0
        ans += bill
        if bill >= a:
            stamp += (bill//a)*b
        bill = int(input())
    while stamp >= c and bill >0:
        bill -= d
        stamp -= c
        if bill <0:
            bill = 0
    ans += bill
    if bill >= a:
        stamp += (bill//a)*b
    print(ans)
    print(stamp)
main()
