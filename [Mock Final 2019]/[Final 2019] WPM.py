"""WPM"""
def checkk(x):
    """KId"""
    if x<11:
        return 'Very Slow'
    if 11<=x<=20:
        return 'Slow'
    if 21<=x<=30:
        return 'Average'
    if 31<=x<=40:
        return 'Fast'
    if x>40:
        return 'Very Fast'
    return None
def checka(x):
    """Adults"""
    if x<26:
        return 'Very Slow'
    if 26<=x<=35:
        return 'Slow/Beginner'
    if 36<=x<=45:
        return 'Intermediate/Average'
    if 46<=x<=65:
        return 'Fast/Advanced'
    if 66<=x<=80:
        return 'Very Fast'
    if x>80:
        return 'Insane'
    return None
def main():
    """WPM"""
    chos = input()
    wpm = int(input())
    if chos == 'Kids':
        print(checkk(wpm))
    elif chos == 'Adults':
        print(checka(wpm))
main()
