import pandas as pd
import matplotlib.pyplot as plt

datas = pd.read_csv('datas_feminicidio.csv', delimiter=',')
# Excluindo coluna de indice
datas = datas.drop(['Unnamed: 0'], axis=1)
# Juntando valores
datas = datas.groupby('Titulo').sum()
# Separando o item em destaque
upTipo, upCount = datas['Quantidade'].idxmax(), datas['Quantidade'].max()
# Imprimindo resultados
print(f'O tipo de feminicidio mais comum é \033[1m{upTipo}\033[0m com \033[1m{upCount:.0f}\033[0m casos.')
datas.plot.barh(title='Casos de Feminicídio SP 2023', xlabel='Casos relatados', ylabel='Catergorias')
