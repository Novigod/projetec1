create table if not exists usuarios(
    nome varchar(50),
    email varchar(80),
    senha varchar(15),
    primary key(email)
);
