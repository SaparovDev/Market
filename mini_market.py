'''Mini Market'''

import json
# Menu di import qiliw
from menu_market import menu


with open("Narseler.json", "w", encoding="utf-8") as file:
    '''Menu di json formatda saqlaw'''
    json.dump(menu, file, indent=4, ensure_ascii=False)


print("Narseler Json file g'a saqlandi")