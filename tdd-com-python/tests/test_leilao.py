from unittest import TestCase

from dominio import Usuario, Lance, Leilao
from tests.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self): # deixar no setUp aquilo que é usado em todos os testes
                     # colocar muitos elementos pode diminuir a performance do teste
        self.vini = Usuario('Vini',500.0)
        self.lance_do_vini = Lance(self.vini, 100.0)
        self.leilao = Leilao('Celular')


    # outras nomenclaturas para teste possíveis:
    #   test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        ka = Usuario('Ka',500.0)
        lance_da_ka = Lance(ka, 150.0)

        self.leilao.propoe(lance_da_ka)
        self.leilao.propoe(self.lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            ka = Usuario('Ka',500.0)
            lance_da_ka = Lance(ka, 90.0)

            self.leilao.propoe(self.lance_do_vini)
            self.leilao.propoe(lance_da_ka)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_somente_um_lance(self):
        self.leilao.propoe(self.lance_do_vini)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(100.0, self.leilao.maior_lance)


    def test_deve_retornar_o_maior_e_o_menor_valor_quando_leilao_tiver_tres_lances(self):
        gui = Usuario("Gui",500.0)
        ka = Usuario('Ka',500.0)

        lance_da_ka = Lance(ka, 150.0)
        lance_do_gui = Lance(gui, 200.0)

        self.leilao.propoe(self.lance_do_vini)
        self.leilao.propoe(lance_da_ka)
        self.leilao.propoe(lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    #se o leilao nao tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_vini)

        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    #se o usuario for diferente, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario("Yuri",500.0)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_vini)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_recebida = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebida)


    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_vini_200 = Lance(self.vini, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_vini)
            self.leilao.propoe(lance_do_vini_200)