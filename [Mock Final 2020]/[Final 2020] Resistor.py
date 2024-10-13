"""[Final 2020] Resistor"""
def main(one,two,thr,fou):
    """[Final 2020] Resistor"""
    onetwo = {"Black":"0","Brown":"1","Red":"2","Orange":"3","Yellow":"4","Green":"5"\
              ,"Blue":"6","Purple":"7","Grey":"8","White":"9"}
    three = {"Black":1,"Brown":10,"Red":100,"Orange":1000,"Yellow":10000,"Green"\
            :100000,"Blue":1000000,"Purple":10000000,"Gold":0.1,"Silver":0.01}
    four = {"Brown":1,"Red":2,"Green":0.5,"Blue":0.25,"Purple":0.1,"Grey":0.05,"Gold":5,"Silver":10}
    if one in onetwo and two in onetwo and thr in three and fou in four:
        print(f"{(int(onetwo[one]+onetwo[two]) * three[thr])*(1-(four[fou])/100):.4f}")
        print(f"{(int(onetwo[one]+onetwo[two]) * three[thr])*(1+(four[fou])/100):.4f}")
    else:
        print("Error")
main(input(),input(),input(),input())
