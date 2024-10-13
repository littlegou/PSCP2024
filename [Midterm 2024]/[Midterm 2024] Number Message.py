"""[Midterm 2024] Number Message"""
def main(sen):
    """main"""
    ans = ""
    l = len(sen)
    for i in range(l):
        if (sen[i] == "3" and sen[i-1] == "1") or (sen[i] == "2" and sen[i-1] == "1"):
            pass
        elif sen[i] == "1" and sen[i+1] == "2":
            ans += "R"
        elif sen[i] == "1" and sen[i+1] == "3":
            ans += "B"
        elif sen[i] == "3" and sen[i-1] != "1":
            ans += "E"
        elif sen[i] == "1":
            ans += "I"
        elif sen[i] == "4":
            ans += "A"
        elif sen[i] == "5":
            ans += "S"
        elif sen[i] == "0":
            ans += "O"
        elif sen[i].isalpha() or sen[i] == " ":
            ans += sen[i]
    print(ans.upper())
main(input())
