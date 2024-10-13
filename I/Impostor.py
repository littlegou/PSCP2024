"""Impostor"""
def main(sen):
    """main"""
    dic = {}
    while sen != "Start":
        check = sen.find(" : ")
        dic[sen[2:check-1]] = sen[check+4:-2]
        sen = input()
    sen = input()
    dead = {}
    while sen != "End":
        dead[sen] = dic.pop(sen)
        sen = input()
    val = list(dic.values())
    print(val.count("Impostor"),"Impostor Remains")
    print("***Alive***")
    for i in sorted(dic.items()):
        print(i[0],":",i[1])
    print("***Dead***")
    for i in sorted(dead.items()):
        print(i[0],":",i[1])
main(input())
