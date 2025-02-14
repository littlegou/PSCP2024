"""Day2011"""
def main(d,m):
    """main"""
    dic = {1:7,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:7,11:3,12:5}
    ans = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",0:"Saturday"}
    print(ans[(d + dic[m]-1)%7])
main(int(input()),int(input()))
