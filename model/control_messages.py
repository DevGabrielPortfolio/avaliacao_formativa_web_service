from data.conexao import Conexao


class Mensagem:
    def cadastrar_requisito(descricao, nivel, valor):
        conn = Conexao.criar_conexao()

        cursor = conn.cursor()

        sql = """INSERT INTO tb_requisitos
                    (descricao, nivel, valor)
                VALUES
                    (%s, %s, %s)"""
        
        valores = (descricao, nivel, valor)
    
        # Executando o comnado sql
        cursor.execute(sql,valores)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conn.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conn.close()


    def recuperar_requisitos():
        #Criar conexão 
        conn = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conn.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT cod_requisito, descricao, nivel, valor, situacao FROM tb_requisitos;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel 
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conn.close()

        return resultado
    
    def delete_requisito(id):
        # Criando a conexão com o banco de dados
        conn = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conn.cursor()

        # Criando o sql que será executado
        sql = "DELETE FROM tb_requisitos WHERE cod_requisito = %s;"
                
        values = (id,)
    
        # Executando o comnado sql
        cursor.execute(sql,values)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conn.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conn.close()

    def update_requisito(id, situacao):
        # Criando a conexão com o banco de dados
        conn = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conn.cursor()

        # Criando o sql que será executado
        sql = "UPDATE tb_requisitos SET situacao = %s WHERE cod_requisito = %s;"
                
        values = (situacao,id)
    
        # Executando o comnado sql
        cursor.execute(sql,values)
    
        # Confirmo a alteração (commit serve para fixar a alteração)
        conn.commit()
    
        # Fecho a conexao com o banco
        cursor.close()
        conn.close()