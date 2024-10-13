"""PrasomSib"""
def main(sen):
    """main"""
    count = 0
    sen = list(map(int,list(sen)))
    while sum(sen)>=10:
        find = 0
        for _,j in enumerate(sen):
            find += j
            if find == 10:
                sen = sen[1:]
                count += 1
                break
            if find >= 10:
                sen = sen[1:]
                break
    print(count)
main(input())
