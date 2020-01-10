import sqlite3
import io

#conexao BD
conn = sqlite3.connect('contatos.db')
#iterador para o BD
cursor = conn.cursor()

def imprime_cabecalho():
     print("******************************\n")   
     print("*   C.R.U.D in Python         *\n")
     print("******************************\n")   
     return 0

#cria o sql do banco
def cadastra():
     cursor.execute("""
         CREATE TABLE IF NOT EXISTS contatos (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              idade INTEGER,
              cpf VARCHAR(11) NOT NULL,
              email TEXT NOT NULL,
              telefone TEXT,
              cidade TEXT,
              uf VARCHAR(2) NOT NULL
              );
          """)

     #entrada de dados
     print('-------Cadastro do Contato------\n')
     c_nome = input('Insira o Nome: ')
     c_idade = input('Insira a Idade: ')
     c_cpf = input('CPF: ')
     c_email = input('Email: ')
     c_telefone = input('Numero de Telefone: ')
     c_cidade = input('Nome da Cidade: ')
     c_uf = input('UF: ')

     cursor.execute("""
          INSERT INTO contatos (nome,idade,cpf,email,telefone,cidade,uf)
          VALUES (?,?,?,?,?,?,?)
               """, (c_nome,c_idade,c_cpf,c_email,c_telefone,c_cidade,c_uf))

     #gravando dados
     conn.commit()
     print('\nDados Inseridos Com Sucesso!\n')
     return 0

def listar_cadastros():
     cursor.execute("""
          SELECT * FROM contatos;
          """)
     #lendo dados
     print('-------Contatos Cadastrados------\n')
     for linha in cursor.fetchall():
          print(linha)
     return 0

def update_cadastro():
     print('-------Atualizar Dados do Contato------\n')
     id_contato = input('Insira o ID do Contato: ')
#TODO criar uma struct ou classe com as variaveis de cadastro, para nao repeti-las
     c_nome = input('\nNome: ')
     c_idade = input('Idade: ')
     c_cpf = input('CPF: ')
     c_email = input('Email: ')
     c_telefone = input('Telefone: ')
     c_cidade = input('Cidade: ')
     c_uf = input('UF: ')

     cursor.execute("""
               UPDATE contatos
               SET nome = ?, idade = ?, cpf = ?, email = ?, telefone = ?, cidade = ?, uf = ?
               WHERE id = ?
               """,(c_nome,c_idade,c_cpf,c_email,c_telefone,c_cidade,c_uf,id_contato))
     conn.commit()
     return 0

def deleta_cadastro():
     id_del = input('ID do contato que deseja DELETAR: ')

     cursor.execute("""
               DELETE FROM contatos
               WHERE id = ?
               """, (id_del))
     conn.commit()
     print('Contato Deletado!')
     return 0

def backup_cadastros():
     with io.open('contatos_dump.sql','w') as f:
          for linha in conn.iterdump():
               f.write('%s\n' % linha)
     print('Backup Terminado\n')
     return 0
#TODO adicionar verificacao na hora de criar ou importar backup               
def import_backup():
     f = io.open('contatos_dump.sql', 'r')
     sql = f.read()
     cursor.executescript(sql)
     print('Dados Importados!')
     return 0

imprime_cabecalho()
#TODO adicionar um loop para rodar esse bloco enquanto for true
print('Selecione uma Opcao: \n')
print('1-> Cadastrar um Contato\n2-> Listar Contatos\n3-> Atualizar Dados\n4-> Deletar Contato')
print('5-> Fazer Backup dos Contatos\n6-> Importar Backup de Contatos\n0~> Encerrar\n')
opcao = input('Opcao Desejada: ')

if opcao == "1": 
    cadastra()
elif opcao == "2":
     listar_cadastros()
elif opcao == "3":
     update_cadastro()
elif opcao == "4":
     deleta_cadastro()
elif opcao == "5":
     backup_cadastros()
elif opcao == "6":
     import_backup()
elif opcao == "0":
     print('Encerrando...\n')
else:
     print("\nOpcao Invalida\nEncerrando...")

conn.close()
