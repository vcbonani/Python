class Data:

    def __init__(self, dia, mes, ano):
        #recebe o dia
        if (dia > 0 and dia < 32):
            if (mes == 2 and dia <30):
                self.dia = dia
            elif (dia < 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)):
                self.dia = dia
            elif(dia < 32 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)):
                self.dia = dia
            else:
                print("Digite um dia válido")
        else:
            print("Digite um dia válido")

        #recebe o mês
        if (mes > 0 and mes < 13):
            self.mes = mes
        else:
            print("Digite um mês válido")

        #recebe o ano
        if (ano > 0 and ano < 10000):
            self.ano = ano
        else:
            print("Digite um ano válido")

    def formatada(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}")