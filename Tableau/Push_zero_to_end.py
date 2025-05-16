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


