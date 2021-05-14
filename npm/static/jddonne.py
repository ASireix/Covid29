import json
import random
from datetime import datetime, timedelta

with open('dataCenter.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)

with open('review.json', 'r') as file:
    dataView=file.read()
objView = json.loads(dataView)

#IMPORTANT

QTE = 20000 #nombre de formulaires
REECRITURE = False 

#GLOBALE
NOM = []
for a in obj :
    NOM.append(a['id'])

PRENOM = []
for a in range(QTE):
    x=str(a)
    while len(x) < len(str(QTE)) :
        x="0"+x
    PRENOM.append(x)

SEXE = ["homme","femme","autre"] #46-42-12

COVID = ["RP-PCR","Antigénique","Dépistage Salivaire","Sérologiques"]



def gen_datetime(min_year=2020, today=datetime.now()):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    end = today - timedelta(21)
    return start + (end - start) * random.random()



def lage():
    prob=random.randint(0,100)#7-18=20 19-50=60 51-80=10 81+=10
    
    if(prob<=20):
        age=random.randint(7,18)
    elif(prob<=80):
        age=random.randint(19,50)
    elif(prob<=90):
        age=random.randint(51,80)
    else:
        age=random.randint(81,99)
        
    return age

def lsexe(age):
    prob=random.randint(0,100)#homme=46 femme=42 autre=12
    
    if(15<age<30):
        if(random.randint(1,3)==3):
            return "autre"
        
    if(prob<=46):
        sexe="homme"
    elif(prob<=88):
        sexe="femme"
    else:
        sexe="autre"
    
    return sexe

def delai(dateT):
    prob=random.randint(0,100)#7-10=21 11-17=53 18-21=26
    
    if(prob<=21):
        tps = random.randint(7,10)
        dateR=dateT + timedelta(tps)
    elif(prob<=74):
        tps = random.randint(11,17)
        dateR=dateT + timedelta(tps)
    else:
        tps = random.randint(18,21)
        dateR=dateT + timedelta(tps)
    
    if(tps<=9):
        tps=5
    elif(tps>=15):
        tps=1
    else:
        tps=random.randint(2,4
                           )
    return dateR,tps

def commentaires(age,total):
    commentaire=None
    
    if(total==2 and 10<=age<=80):
        commentaire = "nul"
    elif(total==5 and 20<=age<=60):
        commentaire="convenable"
    elif(total==10 and (7<=age<=20 or 50<=age<=99)):
        commentaire="Très bien"
    
    return commentaire


def donnee(pos):
    nom=random.choices(NOM)
    prenom="user"+PRENOM[pos]
    age=lage()
    sexe=lsexe(age)
    dateT = gen_datetime()
    dateR,tps = delai(dateT)
    dateT=str(dateT)[0:10]+"T22:00:00.000Z"
    dateR=str(dateR)[0:10]+"T22:00:00.000Z"
    typeTest=random.choice(COVID)
    prise=random.randint(1,5)
    commentaire=commentaires(age,tps+prise)
    
    return [nom,prenom,age,sexe,dateT,dateR,typeTest,tps,prise,commentaire]

def template(qte=QTE):
    if(REECRITURE):
        fichier=[]
    else:
        fichier=objView
    
    for a in range(qte):
        tab=donnee(a)
        
        fiche={
                "siteId":tab[0],
                "prenom":tab[1],
                "age":tab[2],
                "sexe":tab[3],
                "dateT":tab[4],
                "dateR":tab[5],
                "typeTest":tab[6],
                "tpsAttente":tab[7],
                "priseCharge":tab[8],
                "com":tab[9]
        }
        fichier.append(fiche)   
    return fichier



with open("review.json", "w") as file:
    json.dump(template(), file, ensure_ascii=False)
    
    
    
    
    
    