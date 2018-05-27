import unittest

import romeu_julieta


class TestRomeuJulieta(unittest.TestCase):

    def test_dizer_1_1(self):
        self.assertEqual(romeu_julieta.dizer(1), "1")

    def test_dizer_2_2(self):
        self.assertEqual(romeu_julieta.dizer(2), "2")

    def test_dizer_4_4(self):
        self.assertEqual(romeu_julieta.dizer(4), "4")

    def test_dizer_3_queijo(self):
        self.assertEqual(romeu_julieta.dizer(3), "queijo")

    def test_dizer_6_queijo(self):
        self.assertEqual(romeu_julieta.dizer(6), "queijo")

    def test_dizer_9_queijo(self):
        self.assertEqual(romeu_julieta.dizer(9), "queijo")

    def test_dizer_5_goiabada(self):
        self.assertEqual(romeu_julieta.dizer(5), "goiabada")

    def test_dizer_10_goiabada(self):
        self.assertEqual(romeu_julieta.dizer(10), "goiabada")

    def test_dizer_20_goiabada(self):
        self.assertEqual(romeu_julieta.dizer(20), "goiabada")

    def test_dizer_15_romeu_julieta(self):
        self.assertEqual(romeu_julieta.dizer(15), "romeu e julieta")

    def test_dizer_30_romeu_julieta(self):
        self.assertEqual(romeu_julieta.dizer(30), "romeu e julieta")

    def test_dizer_45_romeu_julieta(self):
        self.assertEqual(romeu_julieta.dizer(45), "romeu e julieta")


if __name__ == '__main__':
    unittest.main()
