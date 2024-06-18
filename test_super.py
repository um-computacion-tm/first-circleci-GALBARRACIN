import unittest
from super import Producto, ProductosComprados, Compra

class TestProducto(unittest.TestCase):
    def test_crear_producto(self):
        producto = Producto("123456789", "Yerba", 3000)
        self.assertEqual(producto.__codigo_de_barras__, "123456789")
        self.assertEqual(producto.__nombre__, "Yerba")
        self.assertEqual(producto.__precio__, 3000)
        self.assertEqual(producto.__promo_lleva__, 1)
        self.assertEqual(producto.__promo_paga__, 1)

class TestProductosComprados(unittest.TestCase):
    def test_cantidad_final_pagar_1_1(self):
        producto = Producto("123456789", "Yerba", 3000)
        productos_comprados = ProductosComprados(producto, 2)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 2)

    def test_cantidad_final_pagar_2_1(self):
        producto = Producto("123456789", "Yerba", 3000, promo_lleva=2, promo_paga=1)
        productos_comprados = ProductosComprados(producto, 2)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 1)

    def test_cantidad_final_pagar_4_2(self):
        producto = Producto("123456789", "Yerba", 3000, promo_lleva=2, promo_paga=1)
        productos_comprados = ProductosComprados(producto, 4)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 2)

    def test_cantidad_final_pagar_5_2(self):
        producto = Producto("123456789", "Yerba", 3000, promo_lleva=2, promo_paga=1)
        productos_comprados = ProductosComprados(producto, 5)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 3)

    def test_cantidad_final_pagar_3_2_simple(self):
        producto = Producto("123456789", "Yerba", 3000, promo_lleva=3, promo_paga=2)
        productos_comprados = ProductosComprados(producto, 3)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 2)

    def test_cantidad_final_pagar_3_2_complex(self):
        producto = Producto("123456789", "Yerba", 3000, promo_lleva=3, promo_paga=2)
        productos_comprados = ProductosComprados(producto, 6)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 4)

    def test_cantidad_final_pagar_3_2_resto(self):
        producto = Producto("123456789", "Yerba", 3000, promo_lleva=3, promo_paga=2)
        productos_comprados = ProductosComprados(producto, 7)
        self.assertEqual(productos_comprados.cantidad_final_pagar, 5)

    def test_calcular_total(self):
        producto = Producto("123456789", "Yerba", 3000)
        productos_comprados = ProductosComprados(producto, 2)
        self.assertEqual(productos_comprados.calcular_total(), 6000)


class TestCompra(unittest.TestCase):
    def test_agregar_producto(self):
        compra = Compra()
        producto = Producto("123456789", "Yerba", 3000)
        productos_comprados = ProductosComprados(producto, 2)
        compra.agregar_producto(productos_comprados)
        self.assertEqual(len(compra.__productos_comprados__), 1)
        self.assertEqual(compra.__productos_comprados__[0].calcular_total(), 6000)

    def test_total_compra(self):
        compra = Compra()
        producto1 = Producto("123456789", "Yerba", 3000)
        productos_comprados1 = ProductosComprados(producto1, 2)
        compra.agregar_producto(productos_comprados1)

        producto2 = Producto("987654321", "Fideos", 2000)
        productos_comprados2 = ProductosComprados(producto2, 4)
        compra.agregar_producto(productos_comprados2)

        self.assertEqual(compra.total, 6000 + 8000)

if __name__ == '__main__':
    unittest.main()