def elegir_actividad(tiempo_disponible, energia, clima): 

    actividades = { 

        "leer un libro": {"min_tiempo": 30, "energia": "baja", "clima": "cualquier"}, 

        "ir al cine": {"min_tiempo": 120, "energia": "media", "clima": "cualquier"}, 

        "dar un paseo": {"min_tiempo": 20, "energia": "baja", "clima": "bueno"}, 

        "hacer ejercicio": {"min_tiempo": 45, "energia": "alta", "clima": "bueno"}, 

        "ver una serie": {"min_tiempo": 40, "energia": "media", "clima": "cualquier"}, 

    } 

  

    opciones = [] 

  

    for actividad, criterios in actividades.items(): 

        if (tiempo_disponible >= criterios["min_tiempo"] and  

            (criterios["energia"] == energia or criterios["energia"] == "baja") and 

            (criterios["clima"] == clima or criterios["clima"] == "cualquier")): 

            opciones.append(actividad) 

  

    return opciones if opciones else ["Descansar"] 

  

 

 

# Ejemplo de uso 

tiempo_disponible = 60  # minutos 

energia = "media"  # puede ser "baja", "media" o "alta" 

clima = "bueno"  # puede ser "bueno" o "malo" 

  

actividad_recomendada = elegir_actividad(tiempo_disponible, energia, clima) 

print("Actividades recomendadas:", actividad_recomendada) 