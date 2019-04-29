# FlaskProject

## Para utilizar este projeto, siga os seguintes passos:

1. Baixe o Python disponível em [Python 3.7](https://www.python.org/).
2. Configure o VirtualEnv e ative o mesmo.
3. No diretório configurado para o virtualenv, Clone este projeto com `git clone https://github.com/devdcardoso/FlaskProject`
4. Instale o Flask via pip com o comando `pip install flask`
5. Instale o pytest via pip com o comando `pip install pytest`

## Para rodar o primeiro exemplo:

- No windows:
  - Acessar o diretório que contém o arquivo `hello.py`
  - Usar o comando `set FLASK_APP=hello.py`
- No Linux:
  - Acessar o diretório que contém o arquivo `hello.py`
  - Usar o comando `export FLASK_APP=hello.py`
- Rodar o Flask com o comando `flask run`
- Acessar http://127.0.0.1:5000/
  
## Para rodar o segundo exemplo:
- No windows:
  - Acessar o diretório que contém a pasta `flaskr`
  - Usar o comando `set FLASK_APP=flaskr`
- No Linux:
  - Acessar o diretório que contém a pasta `flaskr`
  - Usar o comando `export FLASK_APP=flaskr`
- Rodar o comando `flask init-db`
- Rodar o comando `flask run`
- Acessar http://127.0.0.1:5000/
