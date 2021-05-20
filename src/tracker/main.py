from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import pvlib


latitude = -23.313602
longitude = -46.221382
altitude = 655
tmz = 'America/Sao_Paulo'
temperatura = 20
pressao = 94000

agora = datetime.now()

dia = agora.today().day
mes = agora.today().month
ano = agora.today().year
hora = agora.today().hour
minuto = agora.today().minute
segundo = agora.today().second

data_inicio = datetime(ano, mes, dia, 0, 0, 0)
data_fim = datetime(ano, mes, dia, 23, 59, 59)

datas = pd.date_range(start=data_inicio, end=data_fim, freq='1Min', tz=tmz)

posicao_sol = pvlib.solarposition.get_solarposition(
    datas,
    latitude,
    longitude,
    altitude,
    temperature=temperatura,
    pressure=pressao
)
posicao_sol.plot()

dt = pd.DatetimeIndex([agora.isoformat()])
posicao_sol_atual = pvlib.solarposition.get_solarposition(
    dt,
    latitude,
    longitude,
    altitude,
    temperature=temperatura,
    pressure=pressao,
    tz=tmz)

plt.scatter(posicao_sol_atual.index.values[0],
            posicao_sol_atual['elevation'][0], linewidths=20, c='y')

plt.show()