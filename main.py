'''
    Sugestão: usar como banco de dados (database - db) o SQLite3 
    https://docs.python.org/3/library/sqlite3.html 
    
    Obs: não se preocupe, 90% dos comandos SQL são iguais aos do SQL Server
        
'''

#git add nomedoArquivo (mais de um arqu, dá espaço)
#git commit -m "mensagem, do que fiz"
#git push

#cd (navegar entre pastas)
#ls (listar aquivos da pasta)


# Criar db e Conectar db
import sqlite3

conexao = sqlite3.connect("db/dados.db")
cursor = conexao.cursor()

# Se as tabelas não existirem crie-as.


# criar tabela ventilação mecanica invasiva e nao invasiva.

tabela =
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
modo_respiratorio     varchar(20)     not null,
fiO2                        float     not null,
peep                        float     not null,
pressao_pico_inspiratoria   float      null,
pressao_inspiratoria        float      null,
volume_corrente             float      not null,
tempo_inspiratorio          float      null,
tempo_expiratorio           float      null,
relacao_ie                  float      null,
);

CREATE TABLE ventilacao_nao_invasiva(
id                  int         autoincrement       primary key,
bipap               varchar(3)       null,
cpap                varchar(3)       null,
ipap                float       null,,
epap                float       null,
presao_suporte      float       null,
);
#bipap e cpap está como varchar, porque o usuario vai indicar qual deles o paciente faz uso
# responde com sim ou não.