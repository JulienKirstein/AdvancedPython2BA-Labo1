def ftc(a, l):
    #On compare un aliment dans le dictionnaire a avec les autres aliments du dictionnaire a:
    #Si la somme des glucides et lipides de l'aliment est < que la somme des glucides et lipides des autres aliments,
    #on retire 0.001 au nombre de calories de l'aliment que l'on comparait sinon, c'est à l'autre que l'on fait cette opération
    #On répète cette opération pour tous les aliments.
    #Le but est d'avoir des nombres de calories différents pour chaque aliment
    o = 0
    while o < len(l):
        c = 1 + o
        while c < len(l):
            if a[l[o]][0] == a[l[c]][0]:
                if (a[l[o]][1]+a[l[o]][2]) < (a[l[c]][1]+a[l[c]][2]):
                    a[l[o]][0] -= 0.001
                else:
                    a[l[c]][0] -= 0.001
                ftc(a, l)
            c += 1
        o += 1

def ftc2(a, l, n):
    #Le nombre n permet juste de pouvoir travailler soit avec des lipides/glucides/protéines
    #On compare un aliment dans le dict a avec les autres:
    #Si le nombre de calories de l'aliment de base est plus petit que celui de l'autre aliment
    #on retire 0.001 au nombre de protéines/glucides/lipides de l'aliment que l'on comparait sinon, c'est à l'autre que l'on fait cette opération
    #On répète cette opération pour tous les aliments.
    #Le but est de ne plus avoir le même nombre de lipidse/glucides/protéines pour chaque aliment qui serait dans ce cas là
    o = 0
    while o < len(l):
        c = 1 + o
        while c < len(l):
            if a[l[o]][n] == a[l[c]][n]:
                if a[l[o]][0] < a[l[c]][0]:
                    a[l[o]][n] -= 0.001
                else:
                    a[l[c]][n] -= 0.001
                ftc2(a, l, n)
            c += 1
        o += 1

#a est un dictionnaire qui contient chaque aliment de la recette en question avec ses propriétées (calories, ...)
#exemple:{'Ananas': [50, 0, 12, 0.5], 'Banane': [90, 0, 20, 1.5], 'Bacon': [119, 3.2, 0.8, 22]}
def toexecutable(a):
    #On rajoute dans la liste 'l' chaque aliment de la recette en question
    #puis, on modifie a de telle sorte qu'il n'y ait pas 2 fois le même nombre de calories/lipides/glucides/protéines
    l = []
    for i in a:
        l.append(i)
    ftc(a, l)
    ftc2(a, l, 1)
    ftc2(a, l, 2)
    ftc2(a, l, 3)
    return a


def croissant(a, n):
    #On trie juste par ordre croissant les aliments soit en fct de leur nombre de calories,soit lipides,soit glucides soit protéines
    #On retourne le résultat
    b = {}
    l = []
    c = []
    for i in a:
        b[a[i][n]] = i
    for i in b:
        l.append(i)
    l.sort()
    for i in l:
        c.append(b[i])
    return c


def calculer(a):
    #On va calculer le coéfficient de chaque aliment dans la recette en question
    coé = {}
    for i in a:
        #le coéfficient initiale de chaque aliment vaut 1
        coé[i] = 1
    #On prend juste tout les aliments de la recette triés en fct des calories
    b = croissant(a, 0)
    #Si l'aliment se trouve en début de liste, on lui rajoutera 1/2 quantité
    #Puis plus l'on se rapproche du millieu de la liste, plus petite la quentité sera rajouté à cette aliment là
    #Une fois passé le milieu de la liste, on retirera a l'aliment en question une certaine quentité
    # qui pour le dernier par exemple vaudrat -1/2 quantité
    #On fait une distinction si la recette contient un nombre pair ou impair d'aliments
    if len(b) % 2 == 0:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            c += 1
    else:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            #print("avant", b[c])
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            #print("apres", b[len(b)-1-c])
            c += 1
    #même opération mais pour les aliments triés en fct de lipides
    b = croissant(a, 1)
    if len(b) % 2 == 0:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            #print("avant", b[c])
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            #print("apres", b[len(b)-1-c])
            c += 1
    else:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            #print("avant", b[c])
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            #print("apres", b[len(b)-1-c])
            c += 1
    #même opération mais pour les aliments triés en fct de glucides
    b = croissant(a, 2)
    if len(b) % 2 == 0:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            #print("avant", b[c])
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            #print("apres", b[len(b)-1-c])
            c += 1
    else:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            #print("avant", b[c])
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            #print("apres", b[len(b)-1-c])
            c += 1
    #même opération mais pour les aliments triés en fct de protéines
    #mise à part que l'on fait ca dans l'autre sens d'ou la fct reverse()
    #car l'on veut favoriser le nombre de protéines contrairement à avant ou l'on voulait diminuer le nombre
    #de calories, lipides, glucides
    b = croissant(a, 3)
    b.reverse()
    if len(b) % 2 == 0:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            c += 1
    else:
        c = 0
        while c < len(b)/2 - 1:
            coé[b[c]] += coé[b[c]]/(c+2)
            coé[b[len(b)-1-c]] -= coé[b[len(b)-1-c]]/(c+2)
            c += 1
    return coé