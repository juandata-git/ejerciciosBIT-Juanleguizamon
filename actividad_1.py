## Actividad 1 - Estructuras y tipos de datos

inventario = [
    {"producto": "camisa", "precio": 25900, "stock": "11"},
    {"producto": "pantalón", "precio": 39900, "stock": "23"},
]

nuevo_producto = {"producto": "abrigo", "precio": 50000, "stock": "2"}
inventario.append(nuevo_producto)

## se agrego un nuevo producto usando .append

for item in inventario:
    item["stock"] = int(item["stock"])


## se usa for para recorrer todo el inventario y cambiar el "stock" de str a int

for item in inventario:
    item["precio"] += 10000

    print(inventario)

## se usa for nuevamente para reccorer todo el codigo y cambiar esta vez el "precio" pero como ya son numeros enteros se puede sumar los 10000