## 
edades = [12, 17, 8, 15, 22, 9, 30, 25]
for edad in edades:
    if edad < 10 :
        continue
    if edad > 18:
        print(f"Adulto: {edad} años")
    if edad == 25:
        print("¡Encontramos al estudiante de 25 años! Deteniendo el análisis.")
        break
    else:
        print(f"Menor: {edad} años")



        #Parte 2
nombres = ["Juan", "Pedro", "Jorge", "María", "Ana"]
i = 0

while i < len(nombres):
    nombre = nombres[i]
    i += 1

    if nombre == "Ana":
        print("¡Ana está en la lista!")
        break
    if nombre.startswith("J"):
        continue
    print(nombre)

    ##pendiente de realizar !!!