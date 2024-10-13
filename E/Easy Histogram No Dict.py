"""Easy Histogram No Dict"""
def main(sen):
    """main"""
    ans = []
    for i in sen:
        if i not in ans and not i.isspace():
            ans.append(i)
    ans = sorted(ans,key=lambda x:(x.lower(),x.isupper()))
    for i in ans:
        print(f"{i} = {sen.count(i)}")
main(input())
