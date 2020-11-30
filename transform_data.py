from data import AppData
from transforms import BibliotecaTransform, TaxaDeAprovacaoTransform


# Variável que conterá os dados para o app
app_json = {}
treatments = {
    'acervo-biblioteca': BibliotecaTransform(),
    'taxa-aprovacao': TaxaDeAprovacaoTransform(),
}

# Tratamento
for key, treatment in treatments.items():
    treatment.execute()
    app_json[key] = treatment.get_data()
    treatment.clear()

# Salva
AppData.save(app_json)
