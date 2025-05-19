#methode 1:Iterative Binary Search
def iterativ_method(tab,target):

    #initialisation des extremités
    pointer_right = len (tab) -1
    pointer_left = 0
    
    #Trouver le milieu
    while pointer_left <= pointer_right:
        milieu = (pointer_left + pointer_right) // 2
        #Trouver la cible
            #si elle est au milieu
        if target == tab[milieu]:
            return milieu
            #Si elle se trouve a gauche du milieu
        elif target < tab [milieu]:
            pointer_right = milieu - 1
            # #Si elle se trouve a droite du milieu
        else :
            pointer_left = milieu + 1

    return -1

#Test
tableau =[1,3,5,7,9,12,43,56,62]
cible = 56
result = iterativ_method(tableau,cible)
print('L\'element se trouve a l\'index:',result)


#Methode 2: Recursive Binary search

def recursiv_method ( tab ,pointer_left, pointer_right, target ):
    if (pointer_right >= pointer_left):
        milieu =  (pointer_left + pointer_right ) //2 
        if target == tab[milieu]:
            return milieu
        elif target > tab[milieu]:
            return recursiv_method (tab, milieu +1 , pointer_right,target)
        else:
            return recursiv_method (tab,pointer_left,milieu -1, target)
    else:
        return -1

#Test
tab = [1,3,5,7,9,12,43,56,62]
cible = 12
result = recursiv_method(tab, 0,len (tab) -1 ,cible)
print(f"L\'element se trouve a l\'index:{result}")
