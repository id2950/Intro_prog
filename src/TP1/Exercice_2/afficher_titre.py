texte = [
"L'ingénieux hidalgo",
"Don Quichotte de la Manche",
"",
"Composé par Miguel de Cervantes",
"",
"Avec privilège royal",
"à Madrid",
"en l'an de grâce 1605"
]



def afficher_titre(texte, largeur):
    largeur = max(largeur,max([len(txt) for txt in texte]))
    texte = [
    "L'ingénieux hidalgo",
    "Don Quichotte de la Manche",
    "",
    "Composé par Miguel de Cervantes",
    "",
    "Avec privilège royal",
    "à Madrid",
    "en l'an de grâce 1605"
    ]
    print(largeur)
