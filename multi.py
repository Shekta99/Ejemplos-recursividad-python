
#funcion recursiva para multiplicar dos numeros
def multip(n,m):
    if m<1:
        return 0
    return n+ multip(n,m-1)
    pass
    


print(multip(int(input("Introduce el primer numero: ")),int(input("Introduce el segundo numero: "))))


#funcion recursiva para elevar un numero
def poten(n,m):
    if m<1:
        return 1
    return n* poten(n,m-1)
    pass

print(poten(int(input("Introduce la base: ")),int(input("Introduce el exponente: "))))
