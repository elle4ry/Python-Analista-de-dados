import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host,user,password,db,table):
    # criar conexao
    conn = pymysql.connect(host=host,user=user,password=password,db=db)

    cursor = conn.cursor()

    # executar consulta
    query = 'select * from ' + table + ' limit 10'
    cursor.execute(query)

    # buscar resultados
    resultados = cursor.fetchall()

    # exibir resultado
    print('Tabela MySQL:')
    for linha in resultados:
        print(linha)

    # fechar a conexão
    cursor.close()
    conn.close()

def df_conexao_mysql(host,user,password,db,table):
    # cria conexão
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)

    # executar consulta e salvar em um dataframe
    query = 'SELECT * FROM ' + table
    df = pd.read_sql(query,conn)

    print('Tabela MySQL com DataFrame: \n', df.head())

    # fechar a conexão
    conn.dispose()
    return df

def conexao_csv(path):
    # ler arquivo csv
    df = pd.read_csv(path)
    print('Dados csv: \n', df.head())

    # escrever arquivo JSON
    df.to_json('dados.json', orient='records', index=False)

#conexao_mysql('localhost','root','root','informatica','cliente')

df_cliente = df_conexao_mysql('localhost','root','root','informatica','cliente')

#conecxao_excel('dados.xlsx')