# Análises dos dados abertos da UFRN

Análises presentes:

- Acervo da biblioteca;
- Taxa de aprovação dos componentes curriculares.

## Reprodução

Você pode executar esse aplicativo de duas formas:

- Usando virtual environment;
- Usando Docker.

### Usando virtual environment

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

### Usando Docker

```bash
# Criar a imagem Docker
make build

# Extrair os dados
make extract

# Transformar os dados em um único JSON
# (essa etapa pode demorar um pouco)
make transform

# Subir app
make run
```
