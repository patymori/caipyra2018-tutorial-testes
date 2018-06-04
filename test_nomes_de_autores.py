import unittest

import nomes_de_autores


class FormatarNomesAutoresTest(unittest.TestCase):

    def test_nome_sobrenome(self):
        self.assertEqual(
            nomes_de_autores.formatar_nome_de_autor('Diana Gabaldon'),
            'GABALDON, Diana'
        )

    def test_charlotte_bronte(self):
        self.assertEqual(
             nomes_de_autores.formatar_nome_de_autor('Charlotte Brönte'),
             'BRÖNTE, Charlotte'
        )

    def test_somente_sobrenome(self):
        self.assertEqual(
            nomes_de_autores.formatar_nome_de_autor('Aristóteles'),
            'ARISTÓTELES'
        )

    def test_machado_de_assis(self):
        self.assertEqual(
            nomes_de_autores.formatar_nome_de_autor('Machado de Assis'),
            'ASSIS, Machado de'
        )

    def test_ana_beatriz_barbosa_silva(self):
        self.assertEqual(
            nomes_de_autores.formatar_nome_de_autor(
                'Ana Beatriz Barbosa Silva'),
            'SILVA, Ana Beatriz Barbosa'
        )

    def test_armando_farias_filho(self):
        self.assertEqual(
            nomes_de_autores.formatar_nome_de_autor(
                'Armando Freitas Filho'),
            'FREITAS FILHO, Armando'
        )

    def test_armando_filho(self):
        self.assertEqual(
            nomes_de_autores.formatar_nome_de_autor(
                'Armando Filho'),
            'FILHO, Armando'
        )


if __name__ == '__main__':
    unittest.main()
