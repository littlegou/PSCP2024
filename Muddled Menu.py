"""Muddled Menu"""
def main(s):
    """main"""
    lis = []
    rem = []
    if s != "CLOSED":
        while s != "DONE":
            if "Can't do:" in s:
                s = s.replace("Can't do: ","")
                if s not in rem:
                    rem.append(s)
            elif s == "SOMETHING'S WRONG":
                lis.clear()
                rem.clear()
            elif s == "CLOSED":
                lis.clear()
                rem.clear()
                break
            elif s[-2:] == "#N":
                lis.append(s[:-3].strip())
            else:
                please = s.find("#")
                please = int(s[please+1:])
                if please>=0:
                    lis.insert(please-1,s[:-3].strip())
                else:
                    lis.insert(please+1,s[:-3].strip())
            s = input()
    for i in rem:
        while i in lis:
            lis.remove(i)
    revlis = lis[:]
    revlis.reverse()
    print(f"Full Course: {lis} Reversed: {revlis}")
main(input())
