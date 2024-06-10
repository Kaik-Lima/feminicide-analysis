import pandas as pd

datas = pd.read_csv('datas_feminicidio.csv', delimiter=',')
# Excluindo coluna de indice
datas = datas.drop(['Unnamed: 0'], axis=1)
# Juntando valores
datas = datas.groupby('Titulo').sum()
# Separando o item em destaque
upTipo, upCount = datas['Quantidade'].idxmax(), datas['Quantidade'].max()
# Imprimindo o resultado
print(f'O tipo de feminicidio mais comum é \033[1m{upTipo}\033[0m com \033[1m{upCount:.0f}\033[0m casos.')
