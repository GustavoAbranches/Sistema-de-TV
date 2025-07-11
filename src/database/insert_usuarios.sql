
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) CHECK (role IN ('superadmin', 'admin', 'editor')),
    setor VARCHAR(100),
    ativo BOOLEAN DEFAULT TRUE
);

-- Inserts exemplo:
INSERT INTO usuarios (nome, email, senha_hash, role) VALUES
('Super Admin', 'superadmin@fatec.com', 'senha_superadmin_hash', 'superadmin'),
('Admin Secretaria', 'secretaria@fatec.com', 'senha_secretaria_hash', 'admin'),
('Admin Marketing', 'marketing@fatec.com', 'senha_marketing_hash', 'admin'),
('Editor Horários', 'editor_horarios@fatec.com', 'senha_editor_hash', 'editor');
