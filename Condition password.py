import random
def aleatoire ():
    pwd=""
    for i in range(4):
        pwd=pwd+str(random.randint(0,9))
    with open("moncode_python.txt", "w") as fichier:
        fichier.write(pwd)
    return pwd

def tentative(password):
    for i in range(3):
        mpt=input("Écrivez le mots de passe : ")
        if mpt==password:
            if i>1:
                print("test de si vous êtes un robot ou pas, on vous a envoyer un fichier avec le code que vous devrez réécrire si dessous")
                m=aleatoire()
                z=input("Écrivez le mots de passe qui vous a était envoyer sur le fichier  : ")
                if m==z:
                    return("vous avez accès au compte ")
                else:
                    z=input("Réessayer : ")
                    if m==z:
                        return("vous avez accès au compte ")


                return("vous avez bloquer le compte")
            return("vous avez accès au compte ")
password= "bonjour"
v=tentative(password)
print(v)

# autre programme
mp = input("Met un mot de passe")
c = 0 
if len(mp) > 8:
    print("Bien le mot de passe est au dessus de 8")
    c += 1
else:
    print("Le mot de passe est en dessous")

if not re.search('[A-Z]',mp):
    print("Il manque un majuscule")
else:
    print("Il y a bien un majuscule")
    c += 1

if not re.search('[a-z]',mp):
    print("Il manque un minuscule")
else:
    print("Il y a bien un minuscule")
    c += 1
    
if not re.search('[@#$%^&*]',mp):
    print("Il manque un caractere special")
else:
    print("Il y a bien un caractere special")
    c += 1
    
if not re.search('[1234567890]', mp):
    print("Il manque un chiffre")
else:
    print("Il y a un chiffre")
    c += 1
if c <= 1:
    print("Eclater")
elif c == 2:
    print("Mot de passe faible")
elif c == 3:
    print("Mot de passe moyen")
elif c == 4:
    print("Franchement bien le mot de passe")
elif c == 5:
    print("Tarpin bien ton mot de passe")

