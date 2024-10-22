"""[Recommend] Solar System"""
def one(sen):
    """one"""
    ans = ""
    for i in sen:
        if not i.isspace():
            ans += i
        elif i.isspace():
            break
    return ans.strip()
def done(sen):
    """done"""
    ans = ""
    for i in sen[::-1]:
        if not i.isspace():
            ans += i
        elif i.isspace():
            break
    return ans[::-1].strip()
def main(sen):
    """[Recommend] Solar System"""
    sen = " " + sen + " "
    left = (sen[:sen.find(" Sun ")]).strip()
    right = sen[sen.find(" Sun ")+5:].strip()
    if not left:
        print(f"Hot: {one(right)}")
        print(f"Cool: {done(right)}")
    elif not right:
        print(f"Hot: {done(left)}")
        print(f"Cool: {one(left)}")
    elif not left.count(" ") and not right.count(" "):
        print(f"Hot: {left} {right}")
        print(f"Cool: {left} {right}")
    elif not left.count(" "):
        print(f"Hot: {left} {one(right)}")
        print(f"Cool: {done(right)}")
    elif not right.count(" "):
        print(f"Hot: {done(left)} {right}")
        print(f"Cool: {one(left)}")
    else:
        print(f"Hot: {done(left)} {one(right)}")
        if left.count(" ") < right.count(" "):
            print(f"Cool: {done(right)}")
        elif left.count(" ") > right.count(" "):
            print(f"Cool: {one(left)}")
        else:
            print(f"Cool: {one(left)} {done(right)}")
main(input())
