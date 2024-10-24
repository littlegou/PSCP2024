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
def main(sen):
    """[Recommend] Solar System"""
    sen = " " + sen + " "
    left = (sen[:sen.find(" Sun ")]).strip()
    right = sen[sen.find(" Sun ")+5:].strip()
    if not left:
        print(f"Hot: {one(right)}")
        print(f"Cool: {one(right[::-1])[::-1]}")
    elif not right:
        print(f"Hot: {one(left[::-1])[::-1]}")
        print(f"Cool: {one(left)}")
    elif not left.count(" ") and not right.count(" "):
        print(f"Hot: {left} {right}")
        print(f"Cool: {left} {right}")
    elif not left.count(" "):
        print(f"Hot: {left} {one(right)}")
        print(f"Cool: {one(right[::-1])[::-1]}")
    elif not right.count(" "):
        print(f"Hot: {one(left[::-1])[::-1]} {right}")
        print(f"Cool: {one(left)}")
    else:
        print(f"Hot: {one(left[::-1])[::-1]} {one(right)}")
        if left.count(" ") < right.count(" "):
            print(f"Cool: {one(right[::-1])[::-1]}")
        elif left.count(" ") > right.count(" "):
            print(f"Cool: {one(left)}")
        else:
            print(f"Cool: {one(left)} {one(right[::-1])[::-1]}")
main(input())
