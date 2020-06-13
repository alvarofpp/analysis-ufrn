import json
from AppJson import AppJson
from treatments import BibliotecaTreatment


# Variável que conterá os dados para o app
app_json = {}
treatments = {
    'acervo-biblioteca': BibliotecaTreatment(),
}

### BIBLIOTECA
for key, treatment in treatments.items():
    treatment.execute()
    app_json[key] = treatment.get_data()
    treatment.clear()

# Salva
AppJson.save(app_json)
