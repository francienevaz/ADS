-- Comando que mostra o BD Selecionado

/* Comentário de várias
linhas
*/

select database(); -- mostra o BD atual

drop table estado; -- exclui a table estado

show tables();  -- lista todas as tabelas do banco

create table produto (
    id int  not null auto_increment,
    descricao varchar(100),
    preco decimal(8,2)
);

insert into produto (
    descricao, preco
) values ('Smartphone Galaxy A3', 1500.90); -- insere  um registro na tabela produto

select * from produto;

insert  into produto (descricao, preco) values ('Smartphone Galaxy S4', 1350.00)

select * from produto order by preco; -- ordena os dados por ordem crescente de preço - é a ordem padrão asc (ascendente) não precisa ser definida

select * from produto order by preco desc; -- ordena os dados por ordem decrescente de preço;

drop database aula; -- apaga o banco de dados aula

CREATE TABLE aluno (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(100),
    genero char(1),
    data_nascimento date,
    estadoCivil char(1) CHECK (estadoCivil IN ('S', 'C', 'V')),
    salario decimal(10,2) unsigned DEFAULT 0,
    email varchar(120) UNIQUE
);

insert into aluno values ('Helena Magalhães', 'F', '2000-01-01', 'C', 2500,
                         'helena.magalhaes@email.com'),
                         ('Nicolas Oliveira', 'M', '2002-12-10', 'S', 8500, 'nicolas.oliveira@email.com'),
                         ('Ana Rosa Silva', 'F', '1996-12-31', 'S', 8500, 'ana.rosa@email.com'),
                         ('Tales Heitor Souza', 'M', '2000-10-01', 'V', 7689, 'tales.heitor@email.com'),
                         ('Bia Meireles', 'F', '2002-03-14', 'V', 9450, 'bia.meireles@email.com'),
                         ('Pedro Filho', 'M', null, 'S', 6800, 'pedro.filho@email.com'),
                         ('Helena Soares', 'F', '1994-08-10', 'S', 8600, 'helena.soares@email.com');




