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

# Se as tabelas não existirem crie-as.
criar_tabelas_query_lista = [
    """ 
        CREATE TABLE IF NOT EXISTS usuarios (
        id          integer         primary key     autoincrement,
        nome        varchar(50)     not null,
        tipo        integer         not null,
        email       varchar(50)     not null
        );
    """,
    """  
        CREATE TABLE IF NOT EXISTS usuarios_tipos (
        id          integer         primary key     autoincrement,
        tipo        varchar(50)     not null
        );
    """, 
    """ 
        CREATE TABLE IF NOT EXISTS dados_vitais (
        id                      integer         primary key     autoincrement,
        pressao_arterial        varchar(10)     not null,
        saturacao_O2            integer         not null,
        frequencia_cardiaca     integer         not null,
        ausculta_pulmonar       varchar(50)     not null
        );
    """, 
    """ 
        CREATE TABLE IF NOT EXISTS ventilacao_mecanica_invasiva (
        id                          integer         primary key     autoincrement,
        modo_respiratorio           varchar(20)     not null,
        fiO2                        float           not null,
        peep                        float           not null,
        pressao_pico_inspiratoria   float           null,
        pressao_inspiratoria        float           null,
        volume_corrente             float           not null,
        tempo_inspiratorio          float           null,
        tempo_expiratorio           float           null,
        relacao_ie                  float           null
        );
    """, 
    """ 
        CREATE TABLE IF NOT EXISTS ventilacao_nao_invasiva (
        id                  integer          primary key     autoincrement,
        bipap               varchar(3)       null,
        cpap                varchar(3)       null,
        ipap                float            null,
        epap                float            null,
        presao_suporte      float            null
        )
        """,
    ]

#bipap e cpap está como varchar, porque o usuario vai indicar qual deles o paciente faz uso
# responde com sim ou não.


def  conectar_banco_de_dados():
    '''
        Cria a conexão e o cursor do banco de dados

        retorna uma tupla (conexao, cursor)
    '''
    conexao = sqlite3.connect("db/dados.db")
    cursor = conexao.cursor()
    
    return (conexao, cursor)


def criar_tabelas(conectar, query):
    '''
        Por limitação do sqlite que não cria as todas em uma só query,
        foi necessária a definicão dessa função que recebe
        conectar [function]: função que retorna (conexão, cursor)
        query [string]: a query de definição da tabela 

        return [bool]
    '''
    try:
        conexao, cursor = conectar()
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()

        return True
    
    except Exception as e:
        print() 
        print(f'erro: {e}')
        print(query)
        print()
        
        return False
        

for q in criar_tabelas_query_lista:
    criar_tabelas(conectar_banco_de_dados, q)
  