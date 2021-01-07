import random

richtige = 0
gesamt = 0
durchlauf = 1


wieviele = int(input("Wie viele richtige soll es geben? (0-6) "))
if wieviele < 0:
    print("Das war unter 0.")
    quit()
elif wieviele > 6:
    print("Das war über 6.")
    quit()

durchlaufe = int(input("Wie viele Durchläufe, soll es geben? "))
if durchlaufe < 1:
    print("Es muss mindestens einen Durchlauf geben.")
    quit()


while durchlauf <= durchlaufe:
    richtige = 0
    wieoft = 0
    while richtige != wieviele:
        richtige = 0
        tipp = []
        ziehung = []

        while len(tipp) < 6:
            if len(tipp) < 6:
                zahl = random.randint(1, 50)
                if not zahl in tipp:
                    tipp.append(zahl)
        while len(ziehung) < 6:
            if len(ziehung) < 6:
                zahl2 = random.randint(1, 50)
                if not zahl2 in ziehung:
                    ziehung.append(zahl2)

        y = 0
        while y < len(tipp):
            x = 0
            while x < len(tipp):
                if tipp[x] == ziehung[y]:
                    richtige += 1
                x += 1
            y += 1
        wieoft += 1
        print("Durchlauf", (durchlauf), "| Ziehung ",
              wieoft, "| Richtige", richtige)
    gesamt += wieoft
    durchlauf += 1


durchschnitt = round((gesamt / durchlaufe), 2)



print("Um", durchlaufe, "mal", wieviele, "richtige zu bekommen, musste insgesamt",
      gesamt, "mal gezogen werden. Das sind im Durschschnitt", durchschnitt, "mal. (also ist die Chance 1:" + str(durchschnitt) + ")")
input("Drücke Enter zum beenden")
