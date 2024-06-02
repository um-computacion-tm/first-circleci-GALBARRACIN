import unittest
from super import Producto, ProductosComprados, Compra

class TestProducto(unittest.TestCase):
    def test_crear_producto(self):
        producto = Producto("123456789", "Yerba", 3)
        self.assertEqual(producto.__codigo_de_barras__, "123456789")
        self.assertEqual(producto.__nombre__, "Yerba")
        self.assertEqual(producto.__precio__, 3)

class TestProductosComprados(unittest.TestCase):
    def test_calcular_total(self):
        producto = Producto("123456789", "Yerba", 3)
        productos_comprados = ProductosComprados(producto, 2)
        self.assertEqual(productos_comprados.calcular_total(), 6)

class TestCompra(unittest.TestCase):
    def test_agregar_producto(self):
        compra = Compra()
        producto = Producto("123456789", "Yerba", 3)
        productos_comprados = ProductosComprados(producto, 2)
        compra.agregar_producto(productos_comprados)
        self.assertEqual(len(compra.__productos_comprados__), 1)
        self.assertEqual(compra.__productos_comprados__[0].calcular_total(), 6)

    def test_total_compra(self):
        compra = Compra()
        producto1 = Producto("123456789", "Yerba", 3)
        productos_comprados1 = ProductosComprados(producto1, 2)
        compra.agregar_producto(productos_comprados1)

        producto2 = Producto("987654321", "Fideos", 2)
        productos_comprados2 = ProductosComprados(producto2, 4)
        compra.agregar_producto(productos_comprados2)

        self.assertEqual(compra.total, 6 + 8)

if __name__ == '__main__':
    unittest.main()