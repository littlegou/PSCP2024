"""Decoding using Matrix"""
import json
def main(sen):
    """main"""
    sen = sen.split()
    matrix = input().replace("'",'"')
    matrix = json.loads(matrix)
    lis = []
    for _ in range(len(sen)//len(matrix)):
        ans = []
        for _ in range(len(matrix[0])):
            ans.append(int(sen[0]))
            del sen[0]
        lis.append(ans)
    decoding = []
    for i in range(len(lis)):
        lisans = []
        for j in range(len(matrix[0])):
            ans = 0
            for k in range(len(matrix[0])):
                ans += int(matrix[k][j]) * lis[i][k]
            lisans.append(ans)
        decoding.extend(lisans)
    for i in decoding:
        if not i:
            print(" " , end = "")
        else:
            print(chr(i+64) , end = "")
main(input().upper())
