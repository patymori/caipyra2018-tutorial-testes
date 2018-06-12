"""
Nomes de autores de obras bibliográficas


- leia um número inteiro correspondendo ao número de nomes que será fornecido
- leia estes nomes (que podem estar em qualquer tipo de letra) e imprima a versão formatada no estilo exemplificado anteriormente.

As seguintes regras devem ser seguidas nesta formatação:
- o sobrenome será igual a última parte do nome e deve ser apresentado em letras maiúsculas;
- se houver apenas uma parte no nome, ela deve ser apresentada em letras maiúsculas (sem vírgula): se a entrada for “Guimaraes” , a saída deve ser “GUIMARAES”;
- se a última parte do nome for igual a "FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA" ou "JUNIOR" e houver duas ou mais partes antes, a penúltima parte fará parte do sobrenome. Assim: se a entrada for "Joao Silva Neto", a saída deve ser "SILVA NETO, Joao" ; se a entrada for "Joao Neto" , a saída deve ser "NETO, Joao";
- as partes do nome que não fazem parte do sobrenome devem ser impressas com a inicial maiúscula e com as demais letras minúsculas;
- "da", "de", "do", "das", "dos" não fazem parte do sobrenome e não iniciam por letra maiúscula.

"""
import unittest
import nomes_autores

class NomesAutoresTestCase(unittest.TestCase):
    """docstring for NomesAutoresTestCase."""


    def test_get_number(self):
        self.assertEqual(nomes_autores.get_number('joão silva'), 2)
        self.assertEqual(nomes_autores.get_number('joão silva neto'), 3)
        self.assertEqual(nomes_autores.get_number('joão'), 1)

    def test_format_name_retorna_maiusculo_se_for_nome_unico(self):
        for test in (("Guimaraes", "GUIMARAES"),
                     ("Silva", "SILVA"),
                     ):
            entrada, esperado = test
            self.assertEqual(nomes_autores.format_name(entrada), esperado)

    def test_format_name_retorna_ultimo_nome_maiusculo_se_for_composto_por_2_nomes(self):
        entrada = "Guimaraes Rosa"
        esperado = "ROSA, Guimaraes"
        self.assertEqual(nomes_autores.format_name(entrada), esperado)

    def test_formart_name_retorna_dois_maiusculos_se_nome_com_sufixo(self):
        entrada = "Guimaraes Rosa neto"
        esperado = "ROSA NETO, Guimaraes"
        self.assertEqual(nomes_autores.format_name(entrada), esperado)
        entrada = "Guimaraes Rosa filho"
        esperado = "ROSA FILHO, Guimaraes"
        self.assertEqual(nomes_autores.format_name(entrada), esperado)
