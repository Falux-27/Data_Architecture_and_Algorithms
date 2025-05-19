#Probleme:

#Soit un tableau array[] la tâche consiste à inverser le tableau. L’inversion d’un tableau consiste à réorganiser les éléments de telle sorte que le premier élément devienne le dernier, le deuxième élément devienne l’avant-dernier et ainsi de suite.


#Methode 1: Approche naïve (Utilisation d’un tableau temporaire - O(n) Temps et O(n) Espace)

def inversion(tab):
    taille = len (tab)
    #Tableau temporaire:
    temp_array = [0] * taille
    #Parcour de la liste et ajouter les element a partir de la fin 
    for i in range (taille):
        temp_array [i]= tab[taille - i - 1] 
    return temp_array

#Cas d'usage:
tableau = [1, 4, 3, 2, 6, 5]
print ('L\'inverse du tableau est:',inversion(tableau))



#Methode 2:Utilisation de deux pointeurs - O(n) temps et O(1) espace

def reverse_type_two(tab_0):
    length = len (tab_0)
    #Initialisation des position des pointeurs
    left_pointer = 0
    right_pointer = tab_0[length -1]
    #Comapraison des indices des pointeurs
    while left_pointer > right_pointer :
        #Swapping
        tab_0[left_pointer] , tab_0[right_pointer] = tab_0[right_pointer] , tab_0[left_pointer]
        #Incrementation et decrementation pour faire bouger les pointeurs
        left_pointer = +1
        right_pointer = -1


#Methode 3: Utilisation de la récursivité - O(n) Temps et O(n) Espace
def recursive_func(tableau_x , i , j):
    if i > j:
        return
    tableau_x [i], tableau_x[j] = tableaux_x[j],tableau_x[i]
    #Appel de la fonction récursive pour passer aux indice suivantes
    recursive_func (tableau_x,i+1,j-1)
def reverser_func(tab):
    taille = len (tab)
    recursive_func(tab , 0,taille -1)

#Cas d'usage:
test = [1,5,2,8,6,11,2,84,0,43,7]
print(f"le tableau inversé avec la 3em methode :",reverser_func(test))




