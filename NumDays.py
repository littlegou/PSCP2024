"""NumDays"""
def main(d1,m1,d2,m2):
    """NumDays"""
    dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if m2<m1:
        m1,m2 = m2,m1
        d1,d2 = d2,d1
    elif m1 == m2 and m1>m2:
        m2 , m1 = m1 , m2
    day = 0
    if dic[m1] < d1 or dic[m2] < d2:
        print("Impossible")
    else:
        lis = list(range(m1,m2+1))
        for i in lis:
            day += dic[i]
        day -= d1 + (dic[m2]-d2)
        print(day)
main(int(input()),int(input()),int(input()),int(input()))
