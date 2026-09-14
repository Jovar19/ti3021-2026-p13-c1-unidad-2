#Producto para una tienda
""""
Cada producto tendrá:
    Nombre
    Precio (El precio nunca puede ser negativo)
Además:
    Mostrar Información del producto.
    Crear un producto de ejemplo.
    Verificar si un producto es costoso (Mayor a $50.000).
"""

class Producto:
    def __init__(self, nombre, precio, descripcion, stock, sku):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock
        self.sku = sku

        if precio < 0:
            self.precio = 0
        else:
            self.precio = precio

    def mostrar_informacion(self):
        print("Producto:", self.nombre)
        print("Precio:", self.precio)

    def es_costoso(self):
        return self.precio > 50000


# Crear un producto de ejemplo
producto = Producto("Notebook", 75000, "Notebook Lenovo 3400 Pro Max", 8, 2)

# Mostrar información
producto.mostrar_informacion()

# Verificar si es costoso
if producto.es_costoso():
    print("El producto es costoso")
else:
    print("El producto no es costoso")