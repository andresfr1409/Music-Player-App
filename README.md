<h1 align="center">
  <b>AudiOdyssey</b>
</h1>

<p align="center">
  <img src="" alt="AudiOdyssey">
</p>

## Nombre y descripcion 

AudiOdyssey es una aplicación web desarrollada con Flask, HTML, CSS, Bootstrap y MySQL. Permite a los usuarios buscar, reproducir y guardar sus canciones favoritas mediante la integración con la API de Spotify. Esta aplicación ofrece una experiencia musical completa con secciones de Inicio, Búsqueda y Biblioteca.

## Capturas de Pantalla

1. ### Seccion de inicio

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/d468b5bd-9431-4662-a48b-12bc4a651d02)

2. Seccion de Buscar

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/34ddb5af-8bdb-49ed-bce7-b0c3cbeaa79d)

3. Busqueda de cancion por su nombre haciendo una solicitud REQUEST.POST a la API

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/5f49f9b3-6e9a-4335-b3dc-ac8ea331e9e7)

4. Redireccion directa a la cancion en spotify para reproducirla

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/038cfcfd-8dbc-43f7-9156-546638cfe3fd)

5. Seccion de Biblioteca

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/96ac825e-1228-41ec-9cf0-1f1df2a8f721)

6. Se guarda la cancion buscada anteriormente en la Biblioteca de favoritos

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/ed8b0b10-ae17-4dfe-aaa3-99795c0ecf46)

## Funcionalidades Principales

- ### Seccion de Inicio

#### Bienvenida y Explicación
- Presenta a los usuarios una bienvenida al ingresar a la aplicación.
- Brinda una breve explicación que destaca las capacidades principales de AudiOdyssey.

- ### Seccion de Busqueda

#### Buscador Integrado

- Utiliza la API de Spotify para buscar canciones por nombre, año, álbum y cantante o artista.
- Proporciona resultados rápidos y precisos para la experiencia del usuario.

#### Información Detallada

- Muestra detalles completos de las canciones, incluyendo nombre, año, álbum, artista/cantante y duración.

#### Reproducción Directa en Spotify

- Ofrece un botón de reproducción que lleva al usuario directamente a la canción en Spotify para una experiencia de escucha continua.

- ### Biblioteca

#### Almacenamiento en Base de Datos

- Guarda las canciones favoritas de los usuarios en una base de datos MySQL.
- Proporciona un sistema robusto para que los usuarios gestionen y accedan fácilmente a sus selecciones musicales.

## Tecnologias Utilizadas

- ### Flask

- Se utilizo Flask para construir la estructura de la aplicación y manejar las solicitudes del usuario.
- Flask ofrece una arquitectura simple y extensible que facilita el desarrollo de aplicaciones web eficientes.

- ### HTML y CSS

- HTML se emplea para la creación de páginas web y la disposición de los elementos.
- CSS se utiliza para dar estilo a la interfaz de usuario, proporcionando una experiencia visual atractiva y coherente.

- ### Bootstrap

- Se incorporo Bootstrap para lograr una apariencia moderna y una experiencia de usuario consistente en diferentes dispositivos.
- Bootstrap simplifica la maquetación y mejora la respuesta de la aplicación en dispositivos móviles y de escritorio.

- ### MySQL

- Utilizamos MySQL para almacenar y gestionar eficientemente la información de las canciones guardadas en la biblioteca de la aplicación.
- La integración con MySQL proporciona una base de datos robusta y escalable para el almacenamiento de datos.

- ### API de Spotify

- La API de Spotify permite acceder a la extensa biblioteca musical de Spotify y realizar diversas operaciones.
- Se integro la API de Spotify para permitir a los usuarios buscar canciones directamente desde la aplicación y reproducirlas directamente en spotify.
- Esto enriquece la experiencia del usuario al proporcionar acceso a una amplia variedad de contenido musical.

## Instalacion

1. Clonar el repositorio
2. Configurar el entorno virtual y instalar las dependencias con el comando "pip install -r requirements.txt".
3. Configurar la conexión con MySQL.

- Crea una base de datos para la aplicación.
- insertar este codigo SQL para crear la tabla canciones_favoritas

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/55aba2fb-cb83-4a53-bc25-105a518c6286)

- Actualiza las configuraciones de la base de datos aqui:

![image](https://github.com/andresfr1409/Music-Player-App/assets/138944864/d1737e7b-8415-46c5-822f-c322fc955c24)

4. Ejecuta la aplicación directamente en el archivo app.py.

## Uso

Una vez que la aplicación esté en ejecución, abre tu navegador y visita http://localhost:5000. Explora las secciones de Inicio, Búsqueda y Biblioteca para disfrutar de la experiencia musical que ofrece AudiOdyssey. Guarda tus canciones favoritas y descubre nuevas joyas musicales con facilidad.
