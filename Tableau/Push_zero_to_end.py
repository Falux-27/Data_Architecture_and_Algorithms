#Probleme:Soit un tableau array_list [] la tâche consiste à déplacer tous les zéros vers la fin du tableau tout en conservant l’ordre relatif de tous les éléments non nuls


#Methode 1:Approche naïve Utilisation d’un tableau temporaire - O(n) temps et o(n) espace
def move_zero (tab):
    taille = len (tab)
    temp_array = [0] * taille
#    initialiser l'indice du tableau temporaire
    j= 0
    for x in range (taille):
        if tab [x] != 0:
            temp_array [j]= tab[x]
        #Incrementer l'indice du tableau temporaire pour passer aau suivante
            j+=1
    while j < taille:
        temp_array [j] = 0
        j+=1
        #Dupliquer le tableau temporaire
    for elt in range (taille):
        tab[elt] = temp_array[elt]
    return tab 

test = [1, 0 , 0, 5, 6, 0, 11, 90, 0, 41, 0, 19 ]
print("Les zeros du tableau déplacés vers la fin du tableau:", move_zero(test))


#methode 2: Deux traversées (Complexité temporelle : O(n),Espace auxiliaire : O(1))
def method_2(tab):
    count = 0
    taille = len (tab)
    for x in range(taille):
        if tab[x] != 0
        tab[x] , tab[count] = tab [count] , tab [x]
        #On incremente pour aller sur la position suivante
        count =+1
    return tab
#Test
tableau = [ 0, 5, 6, 0, 11,13,0,10,23,0,28,0,15,0,10]
print("Les zeros du tableau déplacés vers la fin du tableau:",method_2(tableau))


