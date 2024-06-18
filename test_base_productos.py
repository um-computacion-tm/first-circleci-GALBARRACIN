import unittest
from base_productos import BaseDeDatosProductos
from super import Producto


class TestBaseDeDatosProductos(unittest.TestCase):

    def test_agrega_producto(self):
        producto = Producto('123456789', 'Producto1', 10.0)
        base_datos = BaseDeDatosProductos()
        base_datos.agrega_producto(producto)
        self.assertIn('123456789', base_datos.__base_datos__)
        self.assertEqual(base_datos.__base_datos__['123456789'], producto)

    def test_busca_producto(self):
        producto1 = Producto('123456789', 'Producto1', 10.0)
        producto2 = Producto('987654321', 'Producto2', 20.0)
        base_datos = BaseDeDatosProductos()
        base_datos.agrega_producto(producto1)
        base_datos.agrega_producto(producto2)
        self.assertEqual(base_datos.busca_producto('123456789'), producto1)
        self.assertEqual(base_datos.busca_producto('987654321'), producto2)

    def test_busca_producto_inexistente(self):
        base_datos = BaseDeDatosProductos()
        with self.assertRaises(KeyError):
            base_datos.busca_producto('123456789')

if __name__ == '__main__':
    unittest.main()