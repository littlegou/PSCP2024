"""100 meters"""
def check(one,two,three,num):
    """check"""
    if num < one:
        two , three = one , two
        one = num
    elif num < two:
        three = two
        two = num
    elif num < three:
        three = num
    return one,two,three
def ch(a,b,c,d,e,f,g,h,num):
    """check"""
    ans = 0
    if num == a:
        ans = 1
    elif num == b:
        ans = 2
    elif num == c:
        ans = 3
    elif num == d:
        ans = 4
    elif num == e:
        ans = 5
    elif num == f:
        ans = 6
    elif num == g:
        ans = 7
    elif num == h:
        ans = 8
    return ans
def main():
    """main"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    g = float(input())
    h = float(input())
    one = a
    if b < one:
        one = b
        two = a
    else:
        two = b
    if c < one:
        two,three = one,two
        one = c
    else:
        if c < two:
            three = two
            two = c
        else:
            three = c
    one,two,three = check(one,two,three,d)
    one,two,three = check(one,two,three,e)
    one,two,three = check(one,two,three,f)
    one,two,three = check(one,two,three,g)
    one,two,three = check(one,two,three,h)
    print(ch(a,b,c,d,e,f,g,h,one),end = " ")
    print(ch(a,b,c,d,e,f,g,h,two),end = " ")
    print(ch(a,b,c,d,e,f,g,h,three))
main()
