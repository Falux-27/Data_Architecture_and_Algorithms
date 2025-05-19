#On considere un tableau,la tâche consiste à vérifier s’il est trié par ordre croissant ou non.

#Approche itérative:

def iterativ_approach(tab):
    size = len (tab)
    for i in range (size):
        if tab[i-1] > tab[i]:
            return " Tableau non trié"
    return "Ce tableau est trié"

#Test
tab = [1,2,4,3,6]
result = iterativ_approach(tab)
print (result)
