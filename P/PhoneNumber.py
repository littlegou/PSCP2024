"""PhoneNumber"""
def main(x,word):
    """main"""
    l = x[:-8]
    m = x[-8:-4]
    r = x[-4:]
    if word == "Domestic":
        print(l+" "+m+" "+r)
    else:
        if len(l)>1:
            l = "+66"+l[-1:]
        else:
            l = "+66"
        print(l+" "+m+" "+r)
main(input(),input())
