"""Solar System"""
def find(a,b):
    """find"""
    position = -1
    for _ in range(b):
        position = a.find(" ",position+1)
    return position
def main(sen):
    """main"""
    sen = " " + sen + " "
    wh = sen.find(" Sun ")
    left = sen[:wh].strip()
    right = sen[wh+4:].strip()
    hot = ""
    cool = ""
    hmleft = left.count(" ") + 1
    hmright = right.count(" ") + 1
    if hmleft == 1 and hmright == 1:
        if not left.strip():
            hot = right.strip()
            cool = right.strip()
        elif not right.strip():
            hot = left.strip()
            cool = left.strip()
        else:
            hot = left.strip() + " " + right.strip()
            cool = left.strip() + " " + right.strip()
    elif hmleft == 1 and not left.strip():
        hot = right[:find(right,1)].strip()
        cool = right[find(right,hmright-1):].strip()
    elif hmright == 1 and not right.strip():
        hot = left[find(left,hmleft-1):].strip()
        cool = left[:find(left,1)].strip()
    elif hmleft == 1:
        hot = left.strip() + " " + right[:find(right,1)].strip()
        cool = right[find(right,hmright-1):].strip()
    elif hmright == 1:
        hot = left[find(left,hmleft-1):].strip() + " " + right.strip()
        cool = left[:find(left,1)].strip()
    elif hmleft == hmright:
        hot = left[find(left,hmleft-1):].strip() + " " + right[:find(right,1)].strip()
        cool = left[:find(left,1)].strip() + " " + right[find(right,hmright-1):].strip()
    elif hmleft<hmright:
        hot = left[find(left,hmleft-1):].strip() + " " + right[:find(right,1)].strip()
        cool = right[find(right,hmright-1):].strip()
    elif hmleft>hmright:
        hot = left[find(left,hmleft-1):].strip() + " " + right[:find(right,1)].strip()
        cool = left[:find(left,1)].strip()
    print(f"Hot: {hot.strip()}")
    print(f"Cool: {cool.strip()}")
main(input())
