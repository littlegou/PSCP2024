"""[Recommend] Impostor"""
import json
def main(n):
    """[Recommend] Impostor"""
    dic = {}
    while n != "Start":
        dic.update(json.loads(n))
        n = input()
    n = input()
    dead = {}
    while n != "End":
        dead.update({n:dic.pop(n)})
        n = input()
    print(str(list(dic.values()).count("Impostor")) , "Impostor Remains")
    print("***Alive***")
    for i in list(sorted(dic.items(),key=lambda x:x[0])):
        print(i[0],":",i[1])
    print("***Dead***")
    for i in list(sorted(dead.items(),key=lambda x:x[0])):
        print(i[0],":",i[1])
main(input())
