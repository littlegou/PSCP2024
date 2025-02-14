"""[Recommend] Pringles"""
def main(up,pringles,down,hl):
    """main"""
    hm = pringles.count(")")
    l = len(pringles)
    pringles = f"{pringles[hl:]:>{l}}"
    a = pringles.count(")")
    print(hm-a)
    if not a:
        print("None.")
    else:
        print("There are still some left.")
    print(up)
    print(pringles+"|")
    print(down)
main(input(),input()[:-1],input(),int(input()))
