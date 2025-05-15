#Le but de ce programme est de trouver le second plus grand element dans un tableau avec 2 approches differentes.
#Si l'elmenent n'existe pas on renvoit -1.


#Approche naïve: utilisation du tri

def second_max(tableau):
    taille = len (tableau)
    for i in range (taille):
        for j in range (i+1 , taille):
            if (tableau [i] > tableau [j]):
                tableau[i] , tableau[j] =tableau [j] , tableau [i]
    print(f"Le tableau trié dans l'ordre croissant:{tableau}" )
    for i in range (taille -2 , -1 ,-1):
        if tableau[i] != tableau[taille -1]:
            return tableau[i]
    return -1

   
#Test
tableau1 = [92,42,54,12,34,7,8,15,4,0,3,27]
second_element = second_max(tableau1)
print("Le second plus grand element de ce tableau est :",second_element)


def best_approach(network):
    largest = -1
    second_largest = -1
    length = len (network)
    for x in range (length):
        if network[x] > largest:
            largest = network[x]
    for r in range (length):
        if (network[r] > second_largest and  network[r] != largest ):
            second_largest = network[r]
    return second_largest

#Test
tab = [2,54,12,34,7,43,56,14,68,9,16,80]
func = best_approach(tab)
print("Avec la deuxieme technique :",func)
