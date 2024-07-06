#Question a choix multiples 

import random
countries=['Benin','France','Togo','Italie']
random.shuffle(countries)

score=0
def question_capitale_reponse(pays):
    print(f"Quel est la capitale de {pays}")
    print("(a)-> Rome")
    print("(b)-> Paris")
    print("(c)-> Porto-Novo")
    print("(d)-> Lomé")
    reponse=input("Entrer votre choix entre (a,b,c.d) :")
    return reponse


def verification_resultat( pays,reponse):
    global score 
    if pays == "Benin" and reponse == 'c':
        print("Bonne reponse ")
        score+=1
    elif pays == 'Togo' and reponse == 'd':
        print("Bonne reponse")
        score+=1
    elif pays == 'France' and reponse == 'b':
        print("Bonne reponse")
        score+=1
    elif pays == 'Italie' and reponse == 'a':
        print("Bonne reponse")
        score+=1
    else :
        print("Mauvaise reponse")

for i in countries :
    rep= question_capitale_reponse(i)
    verification_resultat(i,rep)
    print("------------------------------")
print("Votre score est de :" ,score, "sur ",4)

        
