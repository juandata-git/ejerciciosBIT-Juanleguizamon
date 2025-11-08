# clasificar evaluacion de conocimiento de empleados.

def clasificar_desempeño(puntaje):
    if puntaje > 90:
        return "Excelente"
    elif puntaje > 70:
        return "Aprobado"
    elif puntaje > 50:
        return "Regular"
    else : 
        return "Reporbado"
print(clasificar_desempeño(100))


def clasificar_por_edades(edad):
    if 18 <= edad <= 24:
        return "junior"
    elif 25 <= edad <= 34:
        return "mesenior"
    elif 35 <= edad <= 50:
        return "senior"
    else:
        return "menor de edad o supera los 50 años"

# Ejemplo de prueba
print(clasificar_por_edades(17)) 