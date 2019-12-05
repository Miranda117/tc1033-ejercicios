def greet(x):
    for a in range (0,x):
        print ("Agregue un nombre")
        nombre=input()
        lista=[]
        lista.append(nombre)
        print("Hola ",lista)
    return lista


def perceptron (a,b,c,d):
    resultado=(a*b+c*d)
    if resultado > 20:
        print("el numer obtenido es 1")
        print("Pero el resultado de la operacion es: ",resultado)
    else :
        print ("el resultado obtenido en la operacion es 0")
        print("Pero el resultado de la operacion es: ",resultado)
    


def run (a):
    for x in range(0,a,1):
        print ("run")


if  __name__ == "__main__":
    print("Bienvenido, ¿Cuantas personas usaran este programa?")
    a = int(input())
    greet(a)
    b=int(input("ahora difuite un nimero, este debe ser un entero: "))
    run(b)
    print("ahora ingrese cuatro numero")
    c=int(input("-> "))
    d=int(input("-> "))
    e=int(input("-> "))
    f=int(input("-> "))
    perceptron(c,d,e,f)