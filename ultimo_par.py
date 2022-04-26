"""problema 3
"""

print("------------------------------")
print("------ULTIMO DIGITTO PAR------")
print("------------------------------")


#input

x = int(input("digite el valor de x: "))

#processing
ultimo_digito = x % 10

r = ultimo_digito % 2


#output

if r == 0:
    msj="es par"
    print("eso era")
    