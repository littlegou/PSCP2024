"""[Midterm 2024] Scientific Notation"""
def fromx(l_l,r_r,r_,l_,pm):
    """x"""
    if int(l_l):
        aaaaa = len(r_r) - len(str(int(r_r))) + 1
        if l_ == l_l and r_ == -1:
            print(f"{pm}0.{l_l}")
        elif l_ == l_l:
            print(f"{pm}{0.:<0{abs(r_)+1}}{l_l}")
        elif not r_r[aaaaa:] and r_ == -1:
            print("0."+l_l+str(r_r[:aaaaa]))
        elif not r_r[aaaaa:]:
            print(str(r_r[:aaaaa]))
        elif len(l_l)<abs(r_) or r_ == -1:
            print(pm+"0."+("0"*(abs(r_)-1))+l_l[0]+l_l[1:]+r_r.rstrip('0'))
        else:
            print(pm+l_l+str(r_r[:aaaaa]) + "." + r_r[aaaaa:].rstrip('0'))
    else:
        print(pm+"0."+("0"*(abs(r_)-1))+l_l[0]+l_l[1:]+r_r.rstrip('0'))
def fromnum(s,p):
    """fromnum"""
    left = s[:s.find(".")]
    right = s[(s.find(".")+1):]
    if not int(left):
        y0y = len(right) - len(str(int(right))) + 1
        if not right[y0y:]:
            print(p+str(int(right[:y0y])) + " x 10^-"+str(y0y))
        else:
            print(p+str(int(right[:y0y])) + "." + right[y0y:]+ " x 10^-"+str(y0y))
    else:
        if int(left)<10:
            print(p+s + " x 10^0")
        else:
            print(p+left[0]+"."+left[1:]+right+" x 10^"+str(len(left)-1))
def check(s,yy):
    """check"""
    l = s[:s.find(" x")]
    r = int(s[s.find("^")+1:])
    rr = l[(l.find(".")+1):]
    y0u = len(rr)-r
    if l.find(".") != -1:
        ll = l[:l.find(".")]
    else:
        ll = l
    if r<0:
        fromx(ll,rr,r,l,yy)
    else:
        if int(ll):
            y0y = len(rr)-(len(rr) - r)
            if l == ll:
                print(f"{yy}{ll:<0{r+1}}")
            elif not rr[y0y:]:
                print(f"{yy}{ll}{str(rr[:y0y]):<0{r}}")
            else:
                print(yy+ll+str(rr[:y0y]) + "."*(rr[y0y:].rstrip('0')) + rr[y0y:].rstrip('0'))
        else:
            print(f"{yy}{float(l)*(10**(r)):.{y0u}f}")
def main(sen):
    """main"""
    if sen[0] == "-":
        yyy = "-"
        sen = sen[1:]
    else:
        yyy = ""
    if sen.find("x") != -1:
        check(sen,yyy)
    else:
        if not float(sen):
            print(0)
            return
        yoy = sen.find(".")
        if yoy == -1:
            how = len(sen)-1
            if not sen[1:].rstrip('0'):
                print(yyy+sen[0] + " x 10^"+str(how))
            else:
                print(yyy+sen[0]+"."+sen[1:].rstrip('0') + " x 10^"+str(how))
        else:
            fromnum(sen,yyy)
main(input())
