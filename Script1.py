import random
def passendeantwort(reaktionsantworten, keyword,zufallsantworten):
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Handlung: ")

    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligenteAntworten = False
    keyword_treffer = False
    for einzelwort in nutzerwoerter:
        if einzelwort in reaktionsantworten:
            print(reaktionsantworten[einzelwort])
            intelligenteAntworten = True
        if einzelwort == keyword:
            keyword_treffer = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
    if keyword_treffer == True:
        print("Du hast es geschafft")
    return keyword_treffer