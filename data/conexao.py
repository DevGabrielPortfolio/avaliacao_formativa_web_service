import mysql.connector

class Conexao:
    
    def criar_conexao():
        # Criando a conexão com o banco de dados local
        conexao = mysql.connector.connect(host = "localhost",
                                        port = 3306,
                                        user = "root",
                                        password = "root",
                                        database = "db_formativa")
        
        return conexao