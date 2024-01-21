import math

def numeroALetra (numero):
    """Devuelve el número ingresado en palabras."""

    ceroANueve = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    diezAQuince = ["diez", "once", "doce", "trece", "catorce", "quince"]
    dieciVeinti = ["dieci", "veinti"]
    decenas = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if numero>=0 and numero<10:
        palabra = ceroANueve[numero]
    elif numero>=10 and numero<16:
        palabra = diezAQuince[numero]
    elif numero>=16 and numero<20:
        palabra = dieciVeinti[0]+ceroANueve[numero-10]
    elif numero>=20 and numero<30:
        if numero==20:
            palabra = decenas[0]
        else:
            palabra = dieciVeinti[1]+ceroANueve[numero-20]
    elif numero>=30 and numero<=99:
        palabra = decenas[math.trunc(numero/10)-2]+" y "+ceroANueve[numero-(math.trunc(numero/10)*10)]
    else:
        palabra = "Ese valor está fuera de los límites de este programa."
    
    return palabra

numero = int(input("Ingrese un número entero (entre 0 y 99): "))
print("Resultado: "+numeroALetra(numero))