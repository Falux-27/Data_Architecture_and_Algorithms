#L’approche pour résoudre ce problème consiste à 
#parcourir l’ensemble du réseau et à trouver le maximum parmi eux

#--->Complexite temporelle et spatiale 0(n) et 0(1) respectivement
def max_elt (lst):
    max_value   = lst[0]
    for elt in lst:
        if elt > max_value:
            max_value = elt
    return f"Le plus grand element du tableau est = {max_value}"
    
#Appel de la fonction
liste = [12, 25, 73, 24, 53, 16]
plus_grand = max_elt(liste)
print (plus_grand) 


