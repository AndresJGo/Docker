# Docker
Esta es la tarea de Docker para el taller de tecnologías Disruptivas.

# Instrucciones de uso.
## Para poder visualizar todas las peliculas, ingresar a Postman y colocar la siguiente URL con el método GET:
- http://127.0.0.1:5000/movies

## Para poder visualizar una sola pelicula, ingresar a Postman y colocar la siguiente URL con el método GET con el ID de la película correspondiente:
- http://127.0.0.1:5000/movies/{id}

## Para poder agregar una pelicula, ingersar a Postman y colocar la siguiente URL con el método POST:
- http://127.0.0.1:5000/addMovie
- Agregar en el cuerpo de la petición la pelicula a anexar con un archivo JSON con los siguientes atributos:
  {
  "id": 3452,
  "title": "The City of Ember",
  "director": "Andres Jimenez"
 }

## Para poder actualizar una pelicula, ingresar a Postman y colocar la siguiente URL con el método UPDATE:
- http://127.0.0.1:5000/updateMovie/1
- Incluir en el cuerpo de la petición los cambios a realizar como se muestra a continuación:
    {
  "title": "Película Actualizada",
  "director": "Andrés Jiménez"
    }
  
## Para poder borrar una película, ingresar a Postman y colocar la siguiente URL con el método DELETE con el ID de la pelicula correspondiente:
- http://127.0.0.1:5000/deleteMovie/{id}
