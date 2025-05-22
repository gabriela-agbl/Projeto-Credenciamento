CREATE TABLE IF NOT EXISTS EVENTO (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_organizador INT NOT NULL,
    nome VARCHAR(100),
    data_inicio DATE,
    data_fim DATE,
    FOREIGN KEY (id_organizador) REFERENCES USUARIO(id_usuario)
);

CREATE TABLE IF NOT EXISTS USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(100),
    tipo_usuario ENUM('organizador', 'participante') NOT NULL,
    credencial VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS INSCRICAO (
    id_inscricao INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    id_usuario INT,
    FOREIGN KEY (id_evento) REFERENCES EVENTO(id_evento),
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
);