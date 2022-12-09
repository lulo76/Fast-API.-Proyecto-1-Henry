from fastapi import FastAPI
import pymysql
app = FastAPI()

@app.get('/')
def hola ():
    return 'Proyecto Idividual SOY HENRY N° 1'

#Conexion
conexion=pymysql.connect(host='localhost',port=3306,user='root',passwd='0123456789',db='pi_01')
cursor=conexion.cursor()

#Query's N° 1
@app.get('/get_max_duration/')
def query_1 (año:int, plataforma:str,tipo:str):
    año=año
    plataforma=plataforma
    tipo=tipo
    cursor.execute(f"""SELECT Titulo
                    FROM pelicula 
                    WHERE Lanzamiento = {año} AND Tipo = '{tipo}' AND Plataforma = '{plataforma}'
                    ORDER BY Duracion DESC LIMIT 1;""")
    response = cursor.fetchall()[0][0]
    return {'La respuesta de la Query 1 es: ':response}

#Query's N° 2
@app.get('/get_count_plataform/')
def query_2 (plataforma:str):
    plataforma=plataforma
    cursor.execute(f"""SELECT Plataforma, count(Titulo) AS Cantidad, Tipo
                    FROM pelicula
                    WHERE Plataforma = '{plataforma}'
                    GROUP BY Tipo;""")
    response = cursor.fetchall()
    return {'La respuesta de la Query 2 es: ':response}

#Query's N° 3
@app.get('/get_listedin/')
def query_3 (genero:str):
    genero=genero
    cursor.execute(f"""SELECT p.Plataforma, count(g.Genero) AS Cantidad
                    FROM pelicula p INNER JOIN genero g ON  g.index=p.Id_Show
                    WHERE g.Genero='{genero}'
                    GROUP BY Plataforma
                    ORDER BY Cantidad DESC LIMIT 1;""")
    response = cursor.fetchall()
    return {'La respuesta de la Query 3 es: ':response}

#Query's N° 4
@app.get('/get_actor/')
def query_4 (plataforma:str, año:int):
    plataforma=plataforma
    año=año
    cursor.execute(f"""SELECT p.Plataforma, p.Lanzamiento, count(a.Actores) AS Cantidad, a.Actores
                    FROM pelicula p INNER JOIN actor a ON  a.index=p.Id_Show
                    WHERE p.Plataforma = '{plataforma}' AND p.Lanzamiento = {año}
                    GROUP BY a.Actores
                    ORDER BY Cantidad DESC LIMIT 1;""")
    response = cursor.fetchall()
    return {'La respuesta de la Query 4 es: ':response}