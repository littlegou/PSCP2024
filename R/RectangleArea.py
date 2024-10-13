"""RectangleArea"""
def main(st, nd):
    """main"""
    lis1 = list(map(int, st.split()))
    lis2 = list(map(int, nd.split()))
    x1, y1, w1, h1 = lis1[0], lis1[1], lis1[2], lis1[3]
    x2, y2, w2, h2 = lis2[0], lis2[1], lis2[2], lis2[3]
    if max(x1, x2) < min(x1 + w1, x2 + w2) and max(y1, y2) < min(y1 + h1, y2 + h2):
        ow = min(x1 + w1, x2 + w2) - max(x1, x2)
        oh = min(y1 + h1, y2 + h2) - max(y1, y2)
        oa = ow * oh
        print(oa)
    else:
        print("no overlapping")
main(input(), input())
