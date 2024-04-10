#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


import json

per_ces = []
# read movies file into variable
with open('kase.json', 'r') as openfile:
    # Reading from json file
    per_ces = json.load(openfile)


    def top(per_ces): 
        return int(per_ces["cena"])


while True: #dod izvēlēties ko darīt
    print("\nkases aparāts:")
    print("1. pivienot preci")
    print("2. dzēst preci")
    print("3. dzēst sarakstu")
    print("4. samaksāt")
    print("5. iziet")
    choice = input("Enter your choice: ")

    if choice == "1": # var pivirnot preci 
        preces_nosaukums = input("ievadiet nosukumu: ")
        cena = input("ievadiet cenu: ")
        prece = {'prece': preces_nosaukums , 'cena': cena }
        per_ces.append(prece)
        pass
    elif choice == "2": # dod izzdzēst preci
        id = int(input("izvelēties preces numuru: "))
        per_ces.pop(id)
        pass
    elif choice == "3": # izdzēš visas preces
        del per_ces
        print("saraksts izdzēsts")
        pass
    elif choice == "4":# meiģina samaksāt
        per_ces.sort(key = top)
        print(per_ces)
        summa = input("ievadiet summu")
        nauda1 = prece
        print(nauda1)




        if summa == nauda1 :
            print("viss ok")
        if summa < nauda1 :
            print("nav pietiekami naudas")
        if summa > nauda1 :
            print("naudas par daudz, bet mēs to paņemsim sev")

        print(
            "čeks summa ir ", nauda1,"samaksāts ir ", summa 
        )

        pass
    elif choice == "5": #iziet no programas 
        print("Exiting...")
        break
    with open("json", "w") as pukupki: # saglabā produktus
        json.dump(per_ces, pukupki)
