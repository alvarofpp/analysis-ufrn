from data import AppData
from transformers import BibliotecaTransformer, TaxaDeAprovacaoTransformer


# Variável que conterá os dados para o app
app_json = {}
treatments = {
    'acervo-biblioteca': BibliotecaTransformer(),
    'taxa-aprovacao': TaxaDeAprovacaoTransformer(),
}

# Tratamento
for key, treatment in treatments.items():
    treatment.execute()
    app_json[key] = treatment.get_data()
    treatment.clear()

# Salva
AppData.save(app_json)
