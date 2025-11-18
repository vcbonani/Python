from datetime import date,datetime,timezone,timedelta
from pytz import timezone
import pytz

'''
for tz in pytz.all_timezones:
    print(tz)
'''

data_atual = date.today()
print(data_atual)

data_em_texto = "{}/{}/{}".format(data_atual.day,data_atual.month,data_atual.year)
print(data_em_texto)

data_strftime = data_atual.strftime("%d/%m/%Y")
print(data_strftime)

data_hora_atual = datetime.now()
print(data_hora_atual)

data_hora_texto = data_hora_atual.strftime("%d/%m/%Y %H:%M")
print(data_hora_texto)

data_hora_banco_de_dados = "11/10/1991 19:00"
data_hora_convertida = datetime.strptime(data_hora_banco_de_dados,"%d/%m/%Y %H:%M")
print(data_hora_convertida)

diferenca = timedelta(hours=-4)
print(diferenca)


fuso_horario_2 = timezone("America/Sao_Paulo")
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_2)
print(data_hora_sao_paulo.strftime("%d/%m/%Y %H:%M"))