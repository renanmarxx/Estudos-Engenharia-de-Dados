# Olá, seja bem vindo!

Este repositório tem a finalidade de explorar conceitos e conteúdos de python relacionados a Engenharia de Dados.

Dentro das pastas contém os arquivos que servem de apoio e instrução para a relação dos códigos que serão desenvolvidos nos estudos.

Para utilizar estes arquivos será necessário configurar o ambiente instalando algumas bibliotecas e configurando ambiente virtual

```
# Instalando Bibliotecas (a nivel global-local)
pip install pyenv
pip install pipx
pipx install poetry

# Instanciando ambiente virtual
poetry env use 3.12.5
poetry init

# Instalando Bibliotecas (no ambiente virtual)
poetry run #aqui o poetry irá utilizar o arquivo 'pyproject.toml' para instalar as biblitecas necessárias
```