
class VehiclesIU:
    def add_vehilces(self):
        print ("Que tipo de vehiculo es: ")
        _types_of_vehicles_=str(input())
        _vehicle_name_=str(input("Cual es el nombre tecnico del vehiculo: "))
        _cost_=str(input("Cual es el costro del vehiculo: "))
        return _types_of_vehicles_,_vehicle_name_,_cost_

class VehiclesDP:
    def populet_list(self):
        global lista
        lista=[]
        while 1:
            menu_=Menu()
            c=menu_.menu()
            if c ==2:
                break
            else : 
                pass
            vehivle=VehiclesIU()
            a,b,c=vehivle.add_vehilces()
            
            lista.append(a)
            lista.append(b)
            lista.append(c)
        return lista
    
class Menu:
    def menu (self):
        print("seleccione una opcion\n\r\t1.-Agregar un vehiculo\n\r\t2.-salir")
        option=int(input())
        if option ==1:
            pass
        elif option==2:
            pinrt=print_()
            pinrt.print_in_scream()
            exit
 
        else:
            pass 
        return option
class print_:
    def print_in_scream(self):
        lenn=int(len(lista))
        lenn_range=int(lenn/3)
        plus=0
        print("Tipo de vehiculo, Nombre tecnico del vehiculo , Costo del vehiculo")
        for x in range (0,lenn_range,1):
            print(lista[0+plus]+ ","+lista[1+plus] +","+lista[2+plus])
            plus+=3
 

if __name__ == "__main__":
    a=VehiclesDP()
    a.populet_list()
        

 