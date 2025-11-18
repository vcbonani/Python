from datetime import datetime,timedelta

class DatasBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        self.meses_do_ano=["janeiro","fevereiro","março","abril","maio","junho",
                      "julho","agosto","setembro","outubro","novembro","dezembro"]
        return self.meses_do_ano[self.momento_cadastro.month-1]

    def dia_semana(self):
        self.dias_semana = ["segunda","terca","quarta","quinta","sexta","sábado","domingo"]
        return self.dias_semana[self.momento_cadastro.weekday()]

    def formata_data(self):
        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def tempo_cadastro(self):
        return (datetime.today() + timedelta(weeks=4)) - self.momento_cadastro
        # o timedelta acima é uma gambiarra só para demonstrar a variação de tempo