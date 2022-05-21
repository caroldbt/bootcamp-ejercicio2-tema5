def numeroprimo(numero):
    if numero== 0 or numero==1 or numero ==4:
        return "El numero ",numero," no es primo"
    x=2
    while x < numero/2:
        if numero%x==0:
            return "El numero ",numero," no es primo"
        x+=1
    return "El numero ",numero," es primo"
valor=int(input("Ingrese un numero entero: "))
print(numeroprimo(valor))