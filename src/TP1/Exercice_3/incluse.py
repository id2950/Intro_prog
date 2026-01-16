def incluse(a,b,c):
    str(a)
    b = str(set(b))
    for i in range(0,len(a)):
        for j in range (0,len(b)):
            if a[i] == b[j]:
                c = c + 1
            else :
                c = c + 0
    if c == len(a):
        print(True)
    else :
        print(False)

a = input("première chaine de texte : ")
b = input("deuxième chaine de texte : ")
c = 0
incluse(a,b,c)
