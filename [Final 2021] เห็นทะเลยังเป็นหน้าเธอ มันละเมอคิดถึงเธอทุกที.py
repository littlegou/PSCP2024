"""[Final 2021] เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def main(fish):
    """[Final 2021] เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
    dic = {"Bull Shark":"THE SHALLOW ZONE","Chain Catshark":"The Twilight Zone",\
"Great White Shark":"The Twilight Zone","Gummy Shark":"The Twilight Zone","Blue \
Shark":"The Twilight Zone","Mako Shark":"The Twilight Zone","Frilled Shark":"The \
Midnight Zone","Goblin Shark":"The Midnight Zone","Sixgill Shark":"The Midnight\
 Zone","Greenland Shark":"The Midnight Zone","Cookiecutter Shark":"The Midnight \
Zone","Megamouth Shark":"The Abyssal Zone"}
    print(dic[fish.title()].upper() if "SHARK" in fish else "ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
main(input())
