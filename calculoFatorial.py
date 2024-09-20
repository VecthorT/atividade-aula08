def calculadoraFatorial(numFat):
    numPrincipal = numFat;
    calcFat = numFat;
    cont = 1;
    if numFat == 0:
        return 1
    else:
        while cont < numFat:
            calcFat *= numPrincipal - 1;
            numPrincipal -= 1;
            cont += 1;   
        return calcFat

print(calculadoraFatorial(0))

