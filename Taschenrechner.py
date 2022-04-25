##Einfacher Rechner ohne eval()

def rechner(x):
# Anlegen einer "dictionary" mit deren Hilfe Operatoren aus dem Input-String (x) bestimmt werden
    import operator
    operator = {
                "*" :   operator.mul,
                "+" :   operator.add,
                "**":   operator.pow,
                "-" :   operator.sub,
                "/" :   operator.truediv,
                "//":   operator.floordiv,
                "%" :   operator.mod
                }

# Aufteilen des Input-Strings in 3 Parts = a (wert1), b(operator), c (wert2).

    for i in range(0, len(x)):
        if x[i] in operator:
            b = x[i]
            if x[i + 1] in operator:    #  Überprüft ob ein Operator mit 2 Zeichen besteht
                b2 = x[i + 1]
                b += b2
                break
            else:
                b2 = ""
                break

    a = int(x[0:i])
    if b2:
        c = int(x[i + 2:])
    else:
        c = int(x[i + 1:])
    return (operator[b](a, c))      # operator[operator](wert1, wert2) oder: wert1> operator> wert2


print(rechner(input("Gebe Rechenaufgabe ein: ")))
