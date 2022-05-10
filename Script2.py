import random
def games(reaktionsantworten,keyword,zufallsantworten):
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Wie lautet die Lösung?")
    
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    keyword_treffer = False
    for einzelwort in nutzerwoerter:
        if einzelwort in reaktionsantworten :
            print(reaktionsantworten[einzelwort])
            intelligenteAntworten = True
        if einzelwort == keyword:
                keyword_treffer = True
    if intelligenteAntworten == False:
            print(random.choice(zufallsantworten))
    if keyword_treffer == True:
            print("")
    return keyword_treffer