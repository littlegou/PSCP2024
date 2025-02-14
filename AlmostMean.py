""" sfdf """
def main(n):
    """ sad """
    num = 0
    x = 0
    total = 0
    dic = {}
    for _ in range(n):
        num = input()
        a = num.find("\t")
        dic[num[:a].strip()] = num[a+1:].strip()
        x += float(num[a+1:].strip())
    total = x / n
    ans = 0
    for student, score in dic.items():
        score_float = float(score)
        if ans < score_float < total:
            ans = score_float
    studentnum = 0
    for student, score in dic.items():
        if float(score) == ans:
            studentnum = student
    if n == 1:
        print(num)
    else:
        print(f"{studentnum}\t{ans}")
main(int(input()))
