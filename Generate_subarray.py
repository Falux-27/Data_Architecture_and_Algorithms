def sous_tableaux(arr):
    resultats = []
    n = len(arr)

    for i in range(n):  # point de départ
        for j in range(i, n):  # point de fin (inclus)
            sous_tableau = arr[i:j+1]
            resultats.append(sous_tableau)

    return resultats

# Exemple d'utilisation
arr = [1, 2, 3]
print(sous_tableaux(arr))

