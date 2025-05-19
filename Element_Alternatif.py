#L'idée est d'afficher le premier élément,sautez le deuxième élément,
#afficher le troisième, sautez le quatrième élément etc


#----> Approche itérative
def alternative (liste):
    result =[]
    for i in range(0 , len (liste), 2): #Parcourir la liste en fonction de la taille par pas de 2
        result.append (liste[i])        #ajouter les elements de chaque indice                              
    return result                       #Complexité temporelle 0(n)

#Appel de la fonction 
array = [2,3,5,77,1,9,54,8,1001,47]
alt = alternative(array)
print(alt)


#-----> Approche recursive
def func_recursive(liste ,idx , result ):
    if idx < len(liste):
        result.append (liste[idx])
        func_recursive(liste , idx +2 , result) #recursivité
    return result
    
#Appel de la fonction
network = [2,3,5,77,1,9,54,8,100,41,00,121,32,60]
nvell_list = []
resultat = func_recursive(network , 0,nvell_list)
print(resultat)
