"""[Final 2019] Hint"""
def check(n):
    """check"""
    if n[0] == "<":
        num = list(range(int(n[1])))
    elif n[0] == "<=":
        num = list(range(int(n[1])+1))
    elif n[0] == ">":
        num = list(range(int(n[1])+1,10))
    elif n[0] == ">=":
        num = list(range(int(n[1]),10))
    elif n[0] == "==":
        num = [int(n[1])]
    elif n[0] == "!=":
        num = [0,1,2,3,4,5,6,7,8,9]
        num.remove(int(n[1]))
    return num
def main(first,ten,hun):
    """[Final 2019] Hint"""
    for i in check(hun.split()):
        for j in check(ten.split()):
            for k in check(first.split()):
                print(str(i)+str(j)+str(k))
main(input(),input(),input())
