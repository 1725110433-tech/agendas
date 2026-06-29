CREATE TABLE  contactos(
    id_contactos INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);

INSERT INTO contactos(nombre, primer_apellido, segundo_apellido, email, telefono)
VALUES
('Roberto', 'vazquez', 'alvarado', 'beto@', '7751030840'),
('Luis', 'zoyate', 'lopez', 'luis@', '7751044840');

SELECT * FROM contactos;