"""[Final 2020] Colors"""
def main(col1,col2):
    """[Final 2020] Colors"""
    lis = "".join(sorted([col1,col2]))
    dic = {"RedYellow":"Orange","BlueRed":"Violet","BlueYellow":"Green"\
           ,"RedRed":"Red","YellowYellow":"Yellow","BlueBlue":"Blue"}
    print(dic[lis] if lis in dic else "Error")
main(input(),input())
