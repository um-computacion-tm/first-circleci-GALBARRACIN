class Producto:

    def __init__(self,codigo_de_barras,nombre,precio, promo_lleva=1, promo_paga=1):

        self.__codigo_de_barras__=codigo_de_barras

        self.__nombre__=nombre

        self.__precio__=precio
        self.__promo_lleva__ = promo_lleva
        
        self.__promo_paga__ = promo_paga

    @property
    def codigo_barras(self):
        return self.__codigo_de_barras__

    def __str__(self):
        return f"{self.__codigo_de_barras__} - {self.__nombre__}  {self.__precio__}"

class ProductosComprados:

    def __init__(self,producto,cantidad):
        self.__producto__=producto
        self.__cantidad__=cantidad

    @property
    def cantidad_final_pagar(self):
        return (
            (self.__cantidad__ // self.__producto__.__promo_lleva__)
            * self.__producto__.__promo_paga__
        ) + self.__cantidad__ % self.__producto__.__promo_lleva__

    def calcular_total(self):
        return self.cantidad_final_pagar * self.__producto__.__precio__

    def __str__(self):
        return (
            str(self.__producto__) +
            " x " + str(self.__cantidad__) +
            " (paga: " + str(self.cantidad_final_pagar) +
            ") -> " + str(self.calcular_total())
        )

class Compra:

    def __init__(self):

        self.__productos_comprados__=[]



    def agregar_producto(self, producto_comprado):

        self.__productos_comprados__.append(producto_comprado)



    @property

    def total(self):

        precio_total=0

        for producto_comprado in self.__productos_comprados__:

            precio_producto_comprado = producto_comprado.calcular_total()

            precio_total += precio_producto_comprado

        return precio_total

    def __str__(self):
        return "\n".join([str(productos_comprados) for productos_comprados in self.__productos_comprados__ ])