#La tâche ici consiste à trouver les trois plus grands entiers distincts présents dans le tableau.

#S'il y a moins de trois éléments distincts dans le tableau, on renvoit les nombres distincts disponibles dans l'ordre décroissant.


def find_3_largest(liste):
    first = second = third = float ('-inf')
    size = len (liste)
    if size < 3 :
        return "tableau inferieur à 3"

    for element in range (size):
        #Si l'element en cours est superieur au 1er element
        if liste [element] > first:
            third = second
            second = first
            first = liste [element]

        #Si l'element en cours se situe entre le 1er et le 2nd 
        #C'est à dire trouver le 2nd plus grand element 
        elif liste [element] > second and liste [element] != first:
            third = second
            second = liste [element]
        #Trouver le 3em plus grand
        elif liste [element] > third and liste [element] != second and liste [element] != first:
            third = liste [element]
    return first,second,third
#Test
tableau = [2,4,1,8,90,-1,43,5,16,71]
result = find_3_largest(tableau)
print (result)
