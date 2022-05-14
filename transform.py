from data import Data
from transformers import BibliotecaTransformer, TaxaDeAprovacaoTransformer


if __name__ == '__main__':
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
    Data.save(app_json)
