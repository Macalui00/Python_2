import unittest
from activities import eat, nap, is_funny laugh

class ActivityTests(unittest.TestCase):
    # def test_eat(self):
    #     self.assertEqual(eat("broccoli", is_healthy=True),
    #     "I'm eating broccoli, because my body is a temple"
    #     )
    #     self.assertEqual(eat("pizza", is_healthy=False),
    #     "I'm eating pizza, because YOLO"
    #     )
    def test_eat_healthy(self):
        """La comida debe tener un mensaje positivo para el comer sano"""
        self.assertEqual(eat("broccoli", is_healthy=True),
        "I'm eating broccoli, because my body is a temple"
        )
    def test_eat_unhealthy(self):
        """La comida debe indicar que te has rendido de comer insano"""
        self.assertEqual(eat("pizza", is_healthy=False),
        "I'm eating pizza, because YOLO!"
        )
    def test_eat_healthy_boolean(self):
        """is_healthy debe ser un booleano"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")
    def test_short_nap(self):
        """Siestas cortas deben ser refrescantes"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        """Siestas largas deben ser desalentadoras"""
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I didn't mean to nap for 3 hours!"
        )
    def test_is_funny_tim(self):
        #En teoria estas dos sentencias son lo mismo... Así que comento la primera
        self.assertEqual(is_funny("tim"), False)
        # self.assertFalse(is_funny("tim")) #Hay una pequeña diferencia... assertFalse esta chequeando por valores False-y, no solo falsos. Lo cubriremos más adelante
        #Le podes agregar un comentario opcional:
        # self.assertFalse(is_funny("tim"), "tim no debe ser divertido")
    def test_is_funny_anyone_else(self):
        """Cualquiera que no sea tim será divertido"""
        self.assertTrue(is_funny("blue"), "blue debe ser divertido")
        self.assertTrue(is_funny("tammy"), "tammy debe ser divertido")
        self.assertTrue(is_funny("sven"), "sven debe ser divertido")
    def test_laugh(self):
        self.assertIn(laugh(), ("lol", "haha", "tehehe"))

if __name__ == '__main__':
    unittest.main()

#Lo que tengo que hacer es ejecutar este archivo por consola: python test.py

#Para que te muestre la descripcion de las funciones cuando ejecutas la prueba unitaria: python test.py -v