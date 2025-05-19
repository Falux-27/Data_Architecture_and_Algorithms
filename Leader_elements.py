#Approche naïve : Boucle imbriqué

#L'idée est de parcourir le tableau avec deux boucles imbriquées et de faire des comparaison .
#Si un element est superieur au suivant on le considere comme leader et au cas échéant non

def leaders(tab):
    tab_leader = []
    size  = len (tab)
    if (size < 3):
        return "Tableau inférieur à 3 éléments"
    for elt in range (size -1):
        is_leader = True
        for x in range (elt +1 , size):
        #Si un élément suivant est plus grand
            if tab[elt] < tab[x]:
                is_leader = False
                break
        if is_leader :
            tab_leader.append(tab[elt])

    tab_leader.append(tab[-1]) #Ajout du dernier element

    return tab_leader

#Test
tableau = [21,43,67,3,7,66,21,12,9,12,32,14,15,27,43,35,19,0]
result = leaders(tableau)
print("Les elements leaders du tableau sont:", result)


#Approche prévue: 

#L’idée est de scanner tous les éléments de droite à gauche dans un tableau 
#et de garder une trace du maximum jusqu’à présent

def second_approach(liste):
    size =len (liste)
    tab_leads = []
    max_found = liste [-1]
    tab_leads.append(max_found)
    for x in range (size -2 , -1 , -1):
        if liste[x] > max_found :
            max_found = liste[x]
            tab_leads.append(max_found)
    tab_leads.reverse()
    return tab_leads

#Test 
tableau = [1,4,8,6,7,3,2,14,8,9,0]
result = second_approach(tableau)
print ("Les elements leaders du tableau sont:", result)

            






















