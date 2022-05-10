from Script1 import passendeantwort
from Script2 import games
from Generate import Generator
from Display import Picture

#Hier kommen die Parameter rein
zufallsantworten = ["Das ist für dich gerade nicht möglich", "Vielleicht später...", "Du entdeckst hier leider nichts",
                    "Komme später wieder..."]
zufallsantwortengames = ["Das war leider nicht richtig, die Zeit wird knapp...", "Denkst du überhaupt nach?,"
                         "Leider falsch...", "Interesant... aber falsch..."]
reaktionsantworten = {"Seite1":
                            {"kommode" : "In der obersten Schublade liegt ein Photo einer glücklichen Familie",
                             "schrank" : "Du findest einen Schlüssel, mit dem du die Tür öffnest",
                             "vase" : "Als du in die Vase hineinsiehst ist alles dunkel, aber als du sie umdrehst purzeln ein paar Zähne heraus",
                             "fenster" : "Das Fenster ist so beschmutzt, dass du nichts erkennen kannst. Als auf der anderen Seite jedoch plötzlich eine Hand auftaucht, wendest du dich schnell ab",
                             "tisch" : "Der Tisch ist komplett lehrgeräumt und auch unter dem Tisch ist nichts zu sehen.",
                             "beistelltisch" : "An dem kleinen Beistelltischchen lässt sich leider nichts Besonderes finden...",
                             "bild" : "Das Bild sieht wie ein typisches Ölgemälde aus und ist bei genauerem Betrachten etwas vergilbt",
                             "gemälde" : "Die Zeichnung sieht wie ein typisches Ölgemälde aus und ist bei genauerem Betrachten etwas vergilbt"
                             },
                     "Seite2":
                            {"tisch" : "Der Tisch ist komplett lehrgeräumt und auch unter dem Tisch ist nichts zu sehen.",
                             "schrank" : "Jeder Schrank in diesem Raum ist leider komplett lehrgeräumt",
                             "mikrowelle" : "Die Mikrowelle lässt sich mit etwas Aufwand öffnen und darin findet ihr einen Schlüssel mit dem ihr die Tür öffnet.",
                             "schränke" : "Die Schränke sind allesamt lehrgeräumt",
                             },
                     "Seite3":
                            {"bett":"Außer einem Strumpf, für den du keine Verwendung hast, findest du leider nichts",
                             "kommode": "In der obersten Schublade liegt ein Photo einer glücklichen Familie",
                             "hocker": "An der Unterseite des Hockers klebt ein Schlüssel, der ins Schloss passt",
                             "tisch" : "Auch an diesem Tisch ist leider nichts Besonderes",
                             "schrank" : "In dem Schrank stehen nur ein paar unwichtige Bücher, die irgentetwas mit Mathe zu tun haben",
                             "fenster" : "Das Fenster ist verschlossen und lässt sich dementsprechend auch nicht öffnen"
                             },
                     "Seite4":
                            {"kiste" : "In der bereits geöffneten Truhe findet ihr nichts. Ob hier jemand schneller war als ihr?",
                             "truhe" : "In der bereits geöffneten Truhe findet ihr nichts. Ob hier jemand schneller war als ihr?",
                             "tisch" : "Der Tisch ist komplett lehrgeräumt und auch unter dem Tisch ist nichts zu sehen.",
                             "paletten" : "Es handelt sich um leicht vermoderte Paletten, die in jedem Baumarkt erhältlich sind.",
                             "hütte" : "Als ihr die Hütte betretet findet ihr einen Zettel auf dem seltsame Zeichen und Zahlen zu sehen sind",
                             }
                     }
reaktionsantwortengames= {"Game1":
                            {"tip1": "Morsecode",
                             "tip2": "Geburtsreihenfolge",
                             "tip3": "4173",
                             "4173":"Das Schloss öffnet sich, du versteckst dich und wie durch Zauberhand hört das Kratzen auf."},
                          "Game2":
                            {"tip1": "Nehmt euch einen Stift.",
                             "tip2": "Aus dem Stern entspringt die Linie.",
                             "tip3": "Die Himmelsrichtungen helfen.",
                             "3745": "Sehr gut, das Schloss öffnet sich"
                             },
                          "Game3":
                            {"tip1":"Die Schlussfolgerung die am offensichtlichsten ist, ist oft jedoch die falsche.",
                             "tip2": "Müsst ihr Moritz fragen was er hier nicht gemacht hat. (Mal wieder)",
                             "tip3" : "???",
                             "Schlüssel 3" : "Dieser Schlüssel sollte passen und ...       ja es hat funktioniert.",
                             "3" : "Dieser Schlüssel sollte passen und ...       ja es hat funktioniert."
                             },
                          "Game4":
                              {"tip1" : "Ihr müsst Benni fragen. Ich habe das Ganze selber nicht verstanden. RIP.",
                               "20" : "Der Code funktioniert..."
                               }
                         }
keyword = {"Seite1":"schrank",
           "Seite2":"mikrowelle",
           "Seite3":"hocker",
           "Seite4":"hütte"
           }
keywordgames = {"Game1":"4173",
                "Game2":"3745",
                "Game3":"3",
                "Game4":"20"}
intro1 = "Du willst gerade durch die Tür gehen, als auf der anderen Seite der Tür plötzlich Kratzgeräusche zu hören sind. Du suchst nach einem Versteck und siehst einen Schrank, der leider mit einem Zahlenschloss versperrt ist. Finde den Code und zwar schnell.",
intro2 = "Nachdem ihr durch die Tür, die ihr, mit Hilfe des Schlüssels geöffnet habt durchgegangen seid, verspührt ihr einen jämmerlichen Geruch in der Nase. Ihr seid in einem Badezimmer. Komisch, riecht so, als wäre erst vor Kurzem jemand dort gewesen… Ihr wollt so schnell wie möglich aus dem Raum und vor diesem Gestank fliehen. Ihr seht eine andere Tür neben der Dusche. Verdammt, sie ist mit einem Zahlenschloss gesichert. Ihr werdet niemals den 4-stelligen Zahlencode knacken können, denkt ihr, da findet ihr unter dem Toilettendeckel ein Papier. Ein Rätsel? Kann das der Schlüssel zur Flucht sein?"
intro3 = "Ihr verwendet den gefundenen Schlüssel um die Tür zu öffnen. Im nächsten Raum liegen ein paar Schlüssel über den Boden verstreut sonst nichts. Welcher dieser schlüssel sollte passen? (Es ist der Originalschlüssel der passt.)"
intro4 = "Gibt dieses Rätsel den Code für die Tür an? Um das zu erfahren müsst ihr es lösen..."

outro1 = "Du kannst nun in Ruhe durch die Tür gehen. (Blättere jetzt um). Bei dem nächsten Raum scheint es sich um eine Küche zu handeln. Auch hier gibt es wieder eine verschlossene Tür. Doch wo ist der Schlüssel?"
outro2 = "Ihr öffnet das Schloss und hastet durch die Tür in den nächsten Raum. (Umblättern) Dieser neue Raum scheint dem ersten Raum zu ähneln und es gibt eibe verschlossene Tür hinter einem Durchgang. Wo ist der Schlüssel?"
outro3 = "Ihr nehmt den richtigen Schlüssel und schreitet durch die Tür. Ihr findet euch in einem Garten wieder. Auf der einen Seite des Gartens ist eine Tür im Zaun, auf der anderen stehen Gartenmöbel. Was wollt ihr untersuchen? (Umblättern)"
outro4 = "Ihr öffnet das elektronische Schloss und sprintet ohne euch noch einmal umzusehen davon. Ob das eine so gute Entscheidung war..."

Urls = {"Game1" : "www.chatbotka.jimdofree.com/minigame1",
        "Game2" : "www.chatbotka.jimdofree.com/minigame2",
        "Game3" : "www.chatbotka.jimdofree.com/minigame3",
        "Game4" : "www.chatbotka.jimdofree.com/minigame4",
        "Finished" : "www.chatbotka.jimdofree.com/finished",
        "Start" : "www.chatbotka.jimdofree.com/bild1"
        }
#Hier gehts los

print("Willkommen beim Horrorspiel")
print("House of Fear")
print("Zum beenden einfach 'Stop' eintippen")
print("Haben sie die zugehörigen Bilder vorliegen? (Ja/ Nein)")
nutzereingabe = input("Ihre Antwort: ")
nutzereingabe = nutzereingabe.lower()
if nutzereingabe == "ja":
        print("Dieser interaktive Chatbot wird Sie anleiten und Sie durch das Spiel führen.")
        print("Falls man Ihnen nichts anderes sagt, schreiben Sie einfach, wo Sie einen Schlüssel bzw. Code vermuten und lassen sich überraschen.")
        while Generator(Urls["Start"]) == False:
            print("")
        while Picture() == False:
            print("")
        while passendeantwort(reaktionsantworten["Seite1"],keyword["Seite1"],zufallsantworten) == False:
            print("")
        print(intro1)
        while Generator(Urls["Game1"]) == False:
            print("")
        while Picture() == False:
            print("")
        while games(reaktionsantwortengames["Game1"],keywordgames["Game1"],zufallsantwortengames) == False:
            print("")
        print(outro1)
        while passendeantwort(reaktionsantworten["Seite2"],keyword["Seite2"],zufallsantworten) == False:
            print("")
        print(intro2)
        while Generator(Urls["Game2"]) == False:
            print("")
        while Picture() == False:
            print("")
        while games(reaktionsantwortengames["Game2"],keywordgames["Game2"],zufallsantwortengames) == False:
            print("")
        print(outro2)
        while passendeantwort(reaktionsantworten["Seite3"],keyword["Seite3"],zufallsantworten) == False:
            print("")
        print(intro3)
        while Generator(Urls["Game3"]) == False:
            print("")
        while Picture() == False:
            print("")
        while games(reaktionsantwortengames["Game3"],keywordgames["Game3"],zufallsantwortengames) == False:
            print("")
        print(outro3)
        while passendeantwort(reaktionsantworten["Seite4"],keyword["Seite4"],zufallsantworten) == False:
            print("")
        print(intro4)
        while Generator(Urls["Game1"]) == False:
            print("")
        while Picture() == False:
            print("")
        while games(reaktionsantwortengames["Game4"],keywordgames["Game4"],zufallsantwortengames) == False:
            print("")
        print(outro4)
        while Generator(Urls["Finished"]) == False:
            print("")
        while Picture() == False:
            print("")
else: print("Ohne die Bilder (die du auf unserer Website finden kannst) kannst du nur verlieren...")
print("Du kannst das Spiel nun schließen")
