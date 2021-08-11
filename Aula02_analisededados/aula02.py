import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.csv")
print(tabela)

# O parâmetro axis (0 é para excluir linha e
# 1 para excluir coluna)
tabela = tabela.drop("Unnamed: 0",axis=1)


tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")

# all elimina colunas totalmente vazia
tabela = tabela.dropna(how="all",axis=1)

# any elimina se ao menos um valor vazio
tabela = tabela.dropna(how="any",axis=0)

print(tabela.info())
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela,x=coluna,color="Churn")
    grafico.show()
