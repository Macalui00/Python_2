"""Tipos de aserciones:
- self.assertEqual(x, y)
- self.assertNotEqual(x, y)
- self.assertTrue(x)
- self.assertFalse(x)
- self.assertIsNone(x)
- self.assertIsNotNone(x)
- self.assertIn(x, y)
- self.assertNotIn(x, y)
- y muchos más...

Definamos una funcion más en activities y hagamosle el testeo

Usamos assertRaises para asegurarnos de que obtenemos un error en una situacion determinada y no solamente eso, sino tambien una garantia del tipo de error:
Testing for Errors:

class SomeTest(unittest.TestCase):
    def testing_for_error(self):
        '''Testeando por un error'''
        with self.assertRaises(IndexError):
            #Acá indicamos el codigo que queremos que genere un index error
            l = [1,2,3]
            l[100]

Probemo un ejemplo de esto donde cando se ingresa el is_healthy, si este no es un valor booleano tire un error
"""