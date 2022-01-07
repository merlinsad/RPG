import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="rpg",
)

mycursor = mydb.cursor()


def inserir_level():
    sql = f"INSERT INTO jogadores (level) VALUES (%s)"
    val = 1
    mycursor.execute(sql, val)
    mydb.commit()


def inserir_conta(nome, classe, categoria):
    sql = f"INSERT INTO jogadores (nome, classe, categoria) VALUES (%s,%s,%s)"
    val = (nome, classe, categoria)
    mycursor.execute(sql, val)

    mydb.commit()

    print(f"O jogador {nome} foi cadastrado com sucesso!!")


