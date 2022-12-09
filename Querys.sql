use pi_01;

-- Realizamos las consultas.
-- Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])
select Titulo from prueba 
where Lanzamiento = 2018 and Tipo = 'Movie' and Plataforma = 'Hulu'
order by Duracion DESC limit 1;

-- Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)

select Plataforma, count(Titulo) as Cantidad, Tipo from prueba
where Plataforma = 'Netflix'
group by Tipo;

-- Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
-- Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.
Select p.Plataforma, count(g.Genero) as Cantidad
from prueba p inner join genero g on  g.index=p.Id_Show
where g.Genero='Comedy'
group by Plataforma
order by Cantidad desc limit 1;

-- Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

Select p.Plataforma, p.Lanzamiento, count(a.Actores) as Cantidad, a.Actores
from prueba p inner join actor a on  a.index=p.Id_Show
where p.Plataforma = 'Netflix' and p.Lanzamiento = 2018
group by a.Actores
order by Cantidad desc limit 1;

