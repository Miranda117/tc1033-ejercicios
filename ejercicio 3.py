class vehiculos :
    def __init__(self,medio_de_desplazamiento,_capacidad_de_pasajeros,_matricula,_velocidad_maxima,_tipo_decombustible,_caracteristicas_del_motor):
        self.medio_de_desplazamiento=medio_de_desplazamiento
        self.capacidad_de_pasajeros=_capacidad_de_pasajeros
        self.matricula=_matricula
        self.velocidad_maxima=_velocidad_maxima
        self.tipo_decombustible=_tipo_decombustible
        self.caracteristicas_del_motor=_caracteristicas_del_motor


class vehiculos_terrestres(vehiculos):
    def __init__(self,_numero_de_ruedas,_numero_de_puertas,_caracteristicas_de_las_ruedas ):
        self.numero_de_ruedas=_numero_de_ruedas
        self.numero_de_puertas=_numero_de_puertas
        self.caracteristicas_de_las_ruedas=_caracteristicas_de_las_ruedas



class vehiculo_marino(vehiculos):
    def __init__(self,_tipo_de_propulcion):
        self.tipo_de_propulcion=_tipo_de_propulcion

class vehiculo_aereo(vehiculos):
    def __init__(self,_numero_de_ruedas,_numero_de_puertas,_caracteristicas_de_las_ruedas ):
        self.numero_de_ruedas=_numero_de_ruedas
        self.numero_de_puertas=_numero_de_puertas
        self.caracteristicas_de_las_ruedas=_caracteristicas_de_las_ruedas 