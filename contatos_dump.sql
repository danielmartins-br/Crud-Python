BEGIN TRANSACTION;
CREATE TABLE contatos (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              idade INTEGER,
              cpf VARCHAR(11) NOT NULL,
              email TEXT NOT NULL,
              telefone TEXT,
              cidade TEXT,
              uf VARCHAR(2) NOT NULL
              );
INSERT INTO "contatos" VALUES(4,'Vladmyr',0,'89126531091','vlad@mail.com','89120034','Pripyat','RU');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('contatos',4);
COMMIT;
