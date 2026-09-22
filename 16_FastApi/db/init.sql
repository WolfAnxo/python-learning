CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    prioridad TEXT NOT NULL,
    usuario_id INT NOT NULL,
    CONSTRAINT fk_tareas_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
);