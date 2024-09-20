def calculadoraFatorial(numFat):
    numPrincipal = numFat;
    calcFat = numFat;
    cont = 1;
    while cont < numFat:
        calcFat *= numPrincipal - 1;
        numPrincipal -= 1;
        cont += 1;   
    return calcFat

print(calculadoraFatorial(12))

