localizacao = {
    "rua" : "Herman Hering",
    "numero" : 789,
    "bairro": "Bom retiro"
}

info_fiscais = {
    "razao_social" : "SANTA CATATINA INFORMATICA LTDA",
    "cnpj" : "82.923.160/0001-77"
}

empresa = {}

for i,valor in localizacao.items():
    empresa[i] = valor

for i, valor in info_fiscais.items():
    empresa[i] = valor

print(empresa)