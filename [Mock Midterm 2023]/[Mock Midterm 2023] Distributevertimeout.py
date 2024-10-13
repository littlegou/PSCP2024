"""Distribute"""
def main(money,child):
    """main"""
    money -= child
    if money<0:
        print(-1)
    else:
        ans = money // 7
        check = money % 7
        if ans > child:
            print(child - 1)
        elif ans < child:
            if check + 1 == 4 and child - ans <= 1:
                print(ans-1)
            else:
                print(ans)
        else:
            if not check:
                print(ans)
            else:
                print(child-1)
main(int(input()),int(input()))
