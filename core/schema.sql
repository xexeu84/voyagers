CREATE TABLE IF NOT EXISTS participantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    rol VARCHAR(50), -- Viajero, Transportista, Cliente
    contacto VARCHAR(100),
    verificado BOOLEAN DEFAULT FALSE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS hitos_proyecto (
    id SERIAL PRIMARY KEY,
    descripcion TEXT NOT NULL,
    estado VARCHAR(20) DEFAULT 'PENDIENTE', -- PENDIENTE, EN PROCESO, COMPLETADO
    fecha_inicio DATE,
    fecha_fin DATE,
    responsable VARCHAR(50)
);
