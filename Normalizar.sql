-- Creamos el DataBase y la tabla del proyecto con la que iniciaremos a trabajar.
CREATE DATABASE pi_01;
USE pi_01;

-- Verificamos que la conexion se haya realizado con exito.
SELECT * FROM pelicula;

# Normalizamos las tablas
ALTER TABLE pelicula DROP COLUMN Id_Show;
alter table pelicula RENAME COLUMN `index` TO Id_Show;

#Reemplazar min, Season y Seasons, modificamos los datos nulos por cero y cambiamos el tipo de dato.
UPDATE pelicula SET Duracion = TRIM(REPLACE(Duracion,' Season',''));
UPDATE pelicula SET Duracion = TRIM(REPLACE(Duracion,'s',''));
UPDATE pelicula SET Duracion = TRIM(REPLACE(Duracion,' min',''));
UPDATE pelicula SET Duracion = '0' WHERE Duracion = 'Sin Dato';
ALTER TABLE pelicula CHANGE COLUMN Duracion Duracion INT DEFAULT NULL;