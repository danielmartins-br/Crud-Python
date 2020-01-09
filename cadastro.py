import sqlite3
import io
import terminal-banner

#banner de apresentacao
banner_text = "Hello!"
mensagem = terminal_banner.Banner(banner_text)
print(mensagem)

#conexao BD
conn = sqlite3.connect('contatos.db')
#iterador para o BD
cursor = conn.cursor()

print('\n-------C.R.U.D in Python-------\n')
print('Selecione uma Opcao: ')
print('1-> Cadastrar um Contato\n2-> Listar Contatos\n3-> Atualizar Dados\n4-> Deletar Contato\n')
opcao = input('Opcao Desejada: ')

if opcao == "1": 
    cadastra()

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

def listar_cadastros():
     cursor.execute("""
          SELECT * FROM contatos;
          """)
     #lendo dados
     print('-------Contatos Cadastrados------\n')
     for linha in cursor.fetchall():
          print(linha)

def update_cadastro():
     print('-------Atualizar Dados do Contato------\n')
     id_contato = input('Insira o ID do Contato: ')

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

def deleta_cadastro():
     id_del = input('ID do contato que deseja DELETAR: ')

     cursor.execute("""
               DELETE FROM contatos
               WHERE id = ?
               """, (id_del))
     conn.commit()
     print('Contato Deletado!')

def backup():
     with io.open('contatos_dump.sql','w') as f:
          for linha in conn.iterdump():
               f.write('%s\n' % linha)
     print('Backup Terminado\n')
               
def import_backup():
     f = io.open('contatos_dump.sql', 'r')
     sql = f.read()
     cursor.executescript(sql)
     print('Dados Importados!')

conn.close()
