'''
    Sugestão: usar como banco de dados (database - db) o SQLite3 
    https://docs.python.org/3/library/sqlite3.html 
    
    Obs: não se preocupe, 90% dos comandos SQL são iguais aos do SQL Server
        
'''


# Criar db e Conectar db
import sqlite3

conexao = sqlite3.connect("db/dados.db")
cursor = conexao.cursor()

# Se as tabelas não existirem crie-as.


# criar tabela ventilação mecanica invasiva e nao invasiva.

tabela = """
CREATE TABLE pacientes(
id          int             autoincrement   primary key,
nome        varchar(50)     not null,
tipo        int             not null,
email       varchar(50)     not null
);

CREATE TABLE usuarios_tipos(
id          int             autoincrement   primary key,
tipo        varchar(50)     not null,
);

CREATE TABLE dados_vitais(
id          int             autoincrement   primary key,
pressao_arterial        varchar(10)     not null,
saturacao_O2            int             not null,
frequencia_cardiaca     int             not null,
ausculta_pulmonar       varchar(50)     not null
);

CREATE TABLE ventilacao_mecanica_invasiva(
id          int             autoincrement   primary key,
modo
)

"""