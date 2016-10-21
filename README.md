Forno SA
========
Software para controle do Forno SA. Forno SA é um projeto da disciplina Projeto
Integrador 2 da Universidade de Brasília, campus do Gama.

Integrantes
-----------

Criastiano Costa
Luciano Almeida

Instruções para Instalação
--------------------------

1. As seguintes dependências devem ser instaladas:
```
sudo apt-get update && sudo apt-get install -y git nginx python3-dev postgresql postgresql-contrib pgadmin3 python-psycopg2 nodejs npm
```

2. Instale Bower:
```
sudo npm install npm -g
sudo npm install -g bower
```

3. Instalar o virtualenvwrapper:
* É recomendável utilizar o virtualenvwrapper. Instale com:
```
sudo pip install virtualenvwrapper
mkdir ~/Envs
```

* Adicione as linhas a seguir no final do arquivo .bashrc:
```
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Envs
source /usr/local/bin/virtualenvwrapper.sh
```

* Execute o comando a seguir para carregar as configurações feitas:
```
source ~/.bashrc
```

4. Clone este repositório com o comando:
```
cd ~/Envs
git clone https://github.com/forno-sa/forno-sa-web
```

5. Crie e acesse o novo ambiente virtual com os comandos:
```
mkvirtualenv forno -a $HOME/Envs/forno-sa-web -p /usr/bin/python3
workon forno
```

6. Instale as dependências do python:
```
pip install -r requirements.txt
```

7. Instale as dependências do Bower e atualiza arquivos estáticos:
```
./manage.py bower install
./manage.py collectstatic --noinput
```

8. Atualize o banco de dados e rode o servidor:
```
./manage.py migrate
./manage.py runserver
```

9. O servidor estará acessível no endereço:
```
http://127.0.0.1:8000
```