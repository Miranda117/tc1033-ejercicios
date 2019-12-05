def greet(x):
    print("Hola ",x,",¿como estas? ")


def run (a):
    for x in range(0,a,1):
        print ("run")

if  __name__ == "__main__":
    print("Bienvenido, ¿cual es su nombre?")
    a = input()
    greet(a)
    b=int(input("ahora difuite un nimero, este debe ser un entero: "))
    run(b)