from super import Compra, Producto, ProductosComprados
from base_productos import BaseDeDatosProductos

base_datos_producto = BaseDeDatosProductos()
base_datos_producto.agrega_producto(Producto("1234", "Yerba", 2000))
base_datos_producto.agrega_producto(Producto("2345", "Leche", 1800, 2, 1))
base_datos_producto.agrega_producto(Producto("3456", "Pan", 3800, 3, 2))

compra = Compra()

while True:
    try:
        codigo_barras = input("ingrese codigo de barras o FIN: ")
        if codigo_barras == "FIN":
            break
        cantidad = int(input("cantidad: "))
        producto = base_datos_producto.busca_producto(codigo_barras) 
        producto_comprado = ProductosComprados(producto, cantidad)
        compra.agregar_producto(producto_comprado)
        print(compra)
    except:
        print("error")


print("TOTAL PAGAR! ")
print(compra.total)