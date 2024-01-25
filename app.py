import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key = "mysecretkey"

# configurar MySql
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] =  '127.0.0.1' # localhost
app.config['MYSQL_DB'] =  'bibloteca_canciones'
app.config['MYSQL_PORT'] =  3306

# conexion a Mysql 
mysql = MySQL(app)

# Configurar las variables de entorno con las credenciales de la API de Spotify
os.environ['SPOTIPY_CLIENT_ID'] = '014e127abc17487db32712633d5c8ea4'
os.environ['SPOTIPY_CLIENT_SECRET'] = '091271e1da5e42faa398c02292b3c949'

# Función auxiliar para convertir la duración en milisegundos a minutos y segundos
def convertir_duracion(duracion_ms):
    duracion_segundos = duracion_ms // 1000
    minutos = duracion_segundos // 60
    segundos = duracion_segundos % 60
    return f"{minutos}:{segundos:02d}"

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar_canciones():
    # Obtener el término de búsqueda desde los parámetros de la solicitud POST
    query = request.form.get('query')
    # Autenticarse con las credenciales de la API de Spotify
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    # Realizar la solicitud de búsqueda a la API de Spotify
    results = sp.search(q=query, type='track', limit=10)
    # Procesar la respuesta de la API y extraer los resultados relevantes
    canciones = []
    for track in results['tracks']['items']:
        cancion = {
            'nombre': track['name'],
            'artista': track['artists'][0]['name'],
            'enlace': track['external_urls']['spotify'],
            'imagen': track['album']['images'][0]['url'],
            'fecha': track['album']['release_date'],
            'duracion': convertir_duracion(track['duration_ms']),
            'album_enlace': track['album']['external_urls']['spotify'],
            'album_nombre': track['album']['name']
        }
        canciones.append(cancion)
    # Renderizar la plantilla HTML y pasar los resultados de búsqueda
    return render_template('index.html', canciones=canciones)

@app.route('/agregar_favorita/<int:id_cancion>', methods=['POST'])
def agregar_cancion_favorita(id_cancion):
    try:
        # Obtener los datos enviados por el formulario
        nombre = request.form.get('nombre')
        artista = request.form.get('artista')
        enlace = request.form.get('enlace')
        imagen = request.form.get('imagen')
        fecha = request.form.get('fecha')
        duracion = request.form.get('duracion')
        album_enlace = request.form.get('album_enlace')
        album_nombre = request.form.get('album_nombre')
        
        # Insertar la canción en la tabla canciones_favoritas (usando INSERT IGNORE)
        cur = mysql.connection.cursor()
        cur.execute("INSERT IGNORE INTO canciones_favoritas (nombre, artista, enlace_cancion, imagen, fecha_lanzamiento, duracion, enlace_album, nombre_album) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (nombre, artista, enlace, imagen, fecha, duracion, album_enlace, album_nombre))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e), 500

@app.route('/eliminar_favorita/<int:id_cancion>', methods=['POST'])
def eliminar_cancion_favorita(id_cancion):
    try:
        # Eliminar la canción favorita de la tabla de canciones_favoritas
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM canciones_favoritas WHERE id_cancion = %s", (id_cancion,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('biblioteca'))
    except Exception as e:
        return str(e), 500

@app.route('/biblioteca')
def biblioteca():
    try:
        # Obtener las canciones favoritas del usuario desde la tabla canciones_favoritas
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM canciones_favoritas")
        canciones_favoritas = cur.fetchall()
        cur.close()
        
        # Renderizar la plantilla HTML y pasar las canciones favoritas a la página "biblioteca.html"
        return render_template('biblioteca.html', canciones_favoritas=canciones_favoritas)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)