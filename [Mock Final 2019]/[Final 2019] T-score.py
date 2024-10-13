"""[Final 2019] T-score"""
def main(n,_):
    """main"""
    score = []
    score2 = []
    for _ in range(n):
        a = int(input())
        score.append(a)
        score2.append(a**2)
    x = sum(score)/n
    sd = ((sum(score2)*n - ((sum(score))**2))/((n-1)*n))**0.5
    for i in score:
        z = 0 if not sd else (i-x)/sd
        print(f"{50+10*z:.2f}")
main(int(input()),int(input()))
