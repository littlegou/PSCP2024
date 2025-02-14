"""[Recommend] Fever"""
def main(deg):
    """[Recommend] Fever"""
    if deg < 38:
        print("No Fever")
    elif 38 <= deg < 39:
        print("Mild Fever")
    elif 39 <= deg < 40:
        print("High Fever")
    else:
        print("Very High Fever")
main(float(input()))
