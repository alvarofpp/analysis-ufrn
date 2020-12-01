# Análises dos dados abertos da UFRN
Análises presentes:
- Acervo da biblioteca;
- Taxa de aprovação dos componentes curriculares.

## Reprodução
```bash
# Criar environment
python3 -m venv nome-do-env

# Ativar environment
source nome-do-env/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Coletar os dados
python extract.py

# Preparar os dados
python transform.py

# Subir app
streamlit run app.py
```
