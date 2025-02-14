"""OTP"""
def four(n):
    """four"""
    a = (n[0] == n[1]) + (n[0] == n[2]) + (n[0] == n[3]) + (n[1] == n[2]) + \
(n[1] == n[3]) + (n[2] == n[3])
    if a == 1:
        return print("Valid")
    return print("Invalid")
def six(n):
    """six"""
    a = (n[0] == n[1]) + (n[0] == n[2]) + (n[0] == n[3]) + (n[1] == n[2]) + \
(n[1] == n[3]) + (n[2] == n[3]) + (n[0] == n[4]) + (n[0] == n[5]) + (n[1] == n[4]) +\
(n[1] == n[5]) + (n[2] == n[4]) + (n[2] == n[5]) + (n[3] == n[4]) + (n[3] == n[5]) + (n[4] == n[5])
    if (a == 2 and (len(set(n))) == 4) or (a == 3 and (len(set(n))) == 4):
        return print("Valid")
    return print("Invalid")
def eight(n):
    """eight"""
    a = (n[0] == n[1]) + (n[0] == n[2]) + (n[0] == n[3]) + (n[1] == n[2]) + \
(n[1] == n[3]) + (n[2] == n[3]) + (n[0] == n[4]) + (n[0] == n[5]) + (n[0] == \
n[6]) + (n[0] == n[7]) + (n[1] == n[4]) + (n[1] == n[5]) + (n[1] == n[6]) + \
(n[1] == n[7]) + (n[2] == n[4]) + (n[2] == n[5]) + (n[2] == n[6]) + (n[2] == n[7]) +\
(n[3] == n[4]) + (n[3] == n[5]) + (n[3] == n[6]) + (n[3] == n[7]) + (n[4] == n[5]) +\
(n[4] == n[6]) + (n[4] == n[7]) + (n[5] == n[6]) + (n[5] == n[7]) + (n[6] == n[7])
    if a in (3,6):
        return print("Valid")
    return print("Invalid")
def main(n):
    """main"""
    while n != "0":
        if len(n) == 4:
            four(n)
        elif len(n) == 6:
            six(n)
        elif len(n) == 8:
            eight(n)
        n = input()
main(input())
