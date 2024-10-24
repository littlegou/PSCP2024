"""Decoding using Matrix"""
def main(sen):
    """main"""
    sen = sen.split()
    matrix = input()[1:-1].strip()
    real_matrix = []
    f = ""
    for i in range(matrix.count("]")):
        sub = []
        for j in matrix:
            if j == "]":
                break
            if j.isnumeric() or j == "-":
                f += j
            elif f:
                sub.append(f)
                f = ""
        matrix = matrix[matrix.find("]")+2:]
        real_matrix.append(sub)
    lis = []
    for _ in range(len(sen)//len(real_matrix)):
        ans = []
        for _ in range(len(real_matrix[0])):
            ans.append(float(sen[0]))
            del sen[0]
        lis.append(ans)
    decoding = []
    for i in range(len(lis)):
        lisans = []
        for j in range(len(real_matrix[0])):
            ans = 0
            for k in range(len(real_matrix[0])):
                ans += int(int(real_matrix[k][j]) * lis[i][k])
            lisans.append(ans)
        decoding.extend(lisans)
    for i in decoding:
        if not i:
            print(" " , end = "")
        else:
            print(chr(i+64) , end = "")
main(input())
