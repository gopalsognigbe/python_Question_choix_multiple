#Question a choix multiples 

#definir les questions en respectant l'ordre (question,(proposition),(reponse correcte))
question1=('Quelle est la capitale de France ?',('Paris','Rome','Porto-novo','Lomé','gopal'),'Paris')
question2=('Quelle est la capitale de Italie ?',('Paris','Rome','Porto-novo','Lomé'),'Rome')
question3=('Quelle est la capitale de Benin ?',('Paris','Rome','Porto-novo','Lomé'),'Porto-novo')
question4=('Quelle est la capitale de Togo ?',('Paris','Rome','Porto-novo','Lomé'),'Lomé')

questionnaire=[question1,question2,question3,question4]


def poser_question(question):
    print(f'{question[0]}')
    for i in range (len(question[1])):
        print(f'{i+1} -> {question[1][i]}')
    index=verification_resultat(question)
    if question[1][index] == question[2]:
        print("Bonne reponse!!")
        print("_________________________________")
        return True
    else:
        print("Mauvaise reponse!")
    print("_________________________________")
    return False

#verification de la reponse de l'utilisateur et exclusion des erreurs potentiels 
def verification_resultat(question):
    reponse = input(f"Entrer la bonne reponse entre 1 et {len(question[1])} :")
    try :
        index=int(reponse)-1
    except:
        print("Erreur vous devez entrer un chiffre !!!")
        print('')
        return verification_resultat(question)
    if not 0 <= index <=len(question[1]) :
        print(f"Veuillez mettre un chiffre entre 1 et {len(question[1])} !!!")
        print("")
        return verification_resultat(question)
    print("")
    return index
  
#lancement des questions dans la liste quetionnairea et decompte du score 
def lancer_question(questionnaire):
    score=0
    for question in questionnaire:
        if poser_question(question) == True:
            score +=1
    print("Votre score est de :" ,score, "sur ",len(questionnaire))
    
lancer_question(questionnaire)


        
