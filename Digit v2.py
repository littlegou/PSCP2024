"""Digit v2"""
def main():
    """main"""
    sen = input().split()
    lis = []
    dic = {"zero":1,"one":1,"two":1,"three":1,"four":1,"five":1,"six":1,"seven":1,"eight":1,\
"nine":1,"ten":2,"eleven":2,"twelve":2,"thirteen":2,"fourteen":2,"fifteen":2,"sixteen":2,\
"seventeen":2,"eighteen":2,"nineteen":2,"twenty":2,"thirty":2,"forty":2,"fifty":2,"sixty":2,\
"seventy":2,"eighty":2,"ninety":2,"hundred":3,"thousand":4}
    for i in sen:
        lis.append(dic[i])
    print(max(lis))
main()
