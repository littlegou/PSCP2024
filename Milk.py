"""Milk"""
def cal(a,b,c,d):
    """main"""
    # a = ขวดละ
    # b = ต้องใช้กี่ขวดเพื่อ promotion
    # c = ได้กี่ขวดจาก promotion
    # d = money
    if not b:
        can = d // a
    else:
        can = d // a
        free = (can // b) * c
        remain = (can%b) + free
        can += free
        while remain>=b:
            free = ((remain)//b) * c
            remain = ((remain)%b) + free
            can += free
    print(can)
cal(int(input()),int(input()),int(input()),int(input()))
