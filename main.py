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
        tipo_id     integer         not null,
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
        ausculta_pulmonar       varchar(50)     not null,
        usuario_id              integer         not null
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
        relacao_ie                  float           null,
        usuario_id                  integer         not null
        );
    """, 
    """ 
        CREATE TABLE IF NOT EXISTS ventilacao_nao_invasiva (
        id                  integer          primary key     autoincrement,
        bipap               varchar(3)       null,
        cpap                varchar(3)       null,
        ipap                float            null,
        epap                float            null,
        presao_suporte      float            null,
        usuario_id          integer         not null
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

def escrever_banco_de_dados(query, parametros=None, banco=conectar_banco_de_dados):
    try:
        conexao, cursor = banco()
        if (parametros):

            cursor.execute(query, (parametros))
        
        else:
            cursor.execute(query)

        conexao.commit()
        cursor.close()
        conexao.close()

        return True
    
    except Exception as e:
        print() 
        print(f'erro: {e}')
        print()
        return False

def criar_tabelas(query):
    '''
        Por limitação do sqlite que não cria as todas em uma só query,
        foi necessária a definicão dessa função que recebe
        conectar [function]: função que retorna (conexão, cursor)
        query [string]: a query de definição da tabela 

        return [bool]
    '''
    try:
        
        return escrever_banco_de_dados(query)
    
    except Exception as e:
       
        return False


def inserir_tipos_de_usuarios():
    
    query = """
                INSERT INTO usuarios_tipos (tipo)
                VALUES
                (?);
            """
    
    # para inserir apenas um valor, é necessiário colocar a vírgula no final para que a função execute entenda como apenas um valor.
    tipo_usuarios = [
                ('paciente',), 
                ('profissional',),
                ('administrador',)
                ]

    try:
        
        for tipo in tipo_usuarios:
            escrever_banco_de_dados(query, tipo)
            
    except Exception as err:
        print(err)


def dados_vitais(usuario_id):
    query = """
            INSERT INTO dados_vitais (pressao_arterial, saturacao_O2, frequencia_cardiaca, ausculta_pulmonar, usuario_id)
            VALUES
            (?, ?, ?, ?, ?);
        """
    dados = [ 
        '10x8',
        '98%',
        '50bpm',
        'ap:mv+ sem ra',
        usuario_id
    ]
    
    ## terminar a funcao dados vitais
    

    

if (__name__ == '__main__'):
    """
        Aqui começam a ser chamadas as funções
    """

    for q in criar_tabelas_query_lista:
        criar_tabelas(q)
    

    inserir_tipos_de_usuarios()

