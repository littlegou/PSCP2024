"""Stuttering"""
def main(sen):
    """Stuttering"""
    ans = [" "]
    for i in sen:
        if ans[-1] != i:
            ans.append(i)
    print(" ".join(ans).strip())
main(input().split())
