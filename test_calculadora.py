import unittest


class Calculadora:

    def soma(num1, num2):
        return num1 + num2


class CalculadoraTest(unittest.TestCase):

    def test_soma(self):
        params_expected = (
            ((3, 2), 5),
            ((10, 24), 34),
            ((1.5, 4.3), 5.8),
        )
        for param, result in params_expected:
            with self.subTest(param=param, result=result):
                self.assertEqual(
                    Calculadora.soma(*param),
                    result
                )

if __name__ == '__main__':
    unittest.main()
