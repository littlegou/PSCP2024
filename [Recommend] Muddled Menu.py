"""[Recommend] Muddled Menu"""
def main(sen):
    """[Recommend] Muddled Menu"""
    lis = []
    while sen != "DONE":
        if sen == "CLOSED":
            lis = []
            break
        if sen == "SOMETHING'S WRONG":
            lis = []
        elif "Can't do: " in sen:
            sen = sen.replace("Can't do: ","")
            lis.remove(sen)
        elif " #" in sen and sen[-1] == "N":
            lis.append(sen[:sen.find(" #")])
        elif " #" in sen:
            lis.insert(int(sen[sen.find(" #")+2:])-1,sen[:sen.find(" #")])
        sen = input()
    print(f"Full Course: {lis} Reversed: {list(reversed(lis))}")
main(input())
