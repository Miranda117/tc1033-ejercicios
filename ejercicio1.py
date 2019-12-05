def greet(x):
    for a in range (0,x):
        print ("Agregue un nombre")
        nombre=input()
        lista=[]
        lista.append(nombre)
        print("Hola ",lista)
    return lista


def run (a):
    for x in range(0,a,1):
        print ("run")

if  __name__ == "__main__":
    print("Bienvenido, ¿Cuantas personas usaran este programa?")
    a = int(input())
    greet(a)
    b=int(input("ahora difuite un nimero, este debe ser un entero: "))
    run(b)