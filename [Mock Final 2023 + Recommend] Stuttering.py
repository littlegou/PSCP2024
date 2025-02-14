"""[Mock Final 2023 + Recommend] Stuttering"""
def main(sen):
    """[Mock Final 2023 + Recommend] Stuttering"""
    ans = [" "]
    for i in sen:
        if ans[-1] != i:
            ans.append(i)
    print(" ".join(ans).strip())
main(input().split())
