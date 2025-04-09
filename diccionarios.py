#Diccionario:
# colección de datos que
# los almacena en pares
# clave- valor
# un diccionario comienza y termina 
# con llaves (curly braces)
# la clave se separa del valor 
# por dos puntos (:)
# cada elemento (propiedad) del
# diccionario se separa por una coma

#ejemplo : diccionario
# que almacene los datos de
#pais

pais1 = {
            'nombre': 'Argentina',
            'capital': 'Buenos Aires',
            'moneda': 'Peso Argentino',
            'ciudades': [
                            "cordoba",
                            "Rosario",
                            "Mendoza"
                        ],
        'población':{
            "censo": 46,
            "densidad" : 16
        }
        }
#acceeder a la información 
print(pais1['nombre'])
pais2 = {
            'nombre': 'Paraguay',
            'capital': 'Asunción',
            'moneda': 'Guaraní',
            'ciudades': [
                            "Encamación",
                            "Concepcion",
                            "Villarica"
                        ],
        'población':{
            "censo": 46,
            "densidad" : 16
                    }
        }
#acceeder a la información 
print(pais2['capital'])

pais3 = {
            'nombre': 'Chile',
            'capital': 'Santiago de chile',
            'moneda': 'Peso chileno',
            'ciudades': [
                            "Viña del mar",
                            "Puerto Varas",
                            "Arica"
                        ],
        'población':{
            "censo": 17,
            "densidad" : 26
                    }
        }
print("censo:" , pais1['población']['censo'], "millones de hab")
print("densidad:" ,
      pais1['población']['densidad'], "por km2"
    )