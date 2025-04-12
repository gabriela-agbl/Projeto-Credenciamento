CREATE TABLE IF NOT EXISTS EVENTO (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_organizador INT NOT NULL,
    nome VARCHAR(100),
    data_inicio DATE,
    data_fim DATE,
    local VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(100),
    tipo_usuario ENUM('organizador', 'participante') NOT NULL
);

CREATE TABLE IF NOT EXISTS CREDENCIAL (
    id_credencial INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_evento INT,
    codigo VARCHAR(50),
    status ENUM('ativa', 'inativa'),

    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario),
    FOREIGN KEY (id_evento) REFERENCES EVENTO(id_evento)
);