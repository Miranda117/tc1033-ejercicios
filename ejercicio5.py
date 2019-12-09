from ejercicio_4 import VehiclesDP
a=0
class VehiclesAD:
    def make_csv(self):
        a=VehiclesDP()
        lista=a.populet_list()
        b=int(len(lista))
        c=int(b/3)
        archivo=open("VehiclesAD.csv","w+")
        plu=0
        archivo.write("Tipo de vehiculo, Nombre tecnico del vehiculo , Costo del vehiculo\n5")
        for x in range(0,c):
            archivo.write(lista[0+plu]+","+lista[1+plu]+","+lista[2+plu]+"\n" )
            plu+=3
        archivo.close()
if __name__ == "__main__":
    jesus= VehiclesAD()
    jesus.make_csv()

