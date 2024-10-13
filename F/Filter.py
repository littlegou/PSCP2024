"""Filter"""
import json
def main(dic,score):
    """main"""
    dic = sorted(json.loads(dic).items())
    check = 1
    for i in dic:
        if i[1]>= score:
            print(i[0]+"\t"+str(f"{i[1]:.2f}"))
            check = 0
    if check:
        print("Nope")
main(input(),float(input()))
