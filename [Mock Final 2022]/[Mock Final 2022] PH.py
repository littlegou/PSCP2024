"""PH"""
def main(n):
    """PH"""
    if 0 <= n < 7:
        print("acidic")
    elif n == 7:
        print("neutral")
    elif 7 < n <= 14:
        print("akaline")
    else:
        print("error")
main(float(input()))
