class BaseDeDatosProductos:
    def __init__(self):
        self.__base_datos__ = {}

    def agrega_producto(self, producto):
        self.__base_datos__[producto.codigo_barras] = producto

    def busca_producto(self, codigo_barras):
        return self.__base_datos__[codigo_barras]