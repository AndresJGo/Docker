from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para almacenar las películas
movies = []

@app.route('/movies', methods=['GET'])
def get_movies():
    # Este endpoint se utiliza para obtener todas las películas en la lista.
    return jsonify(movies), 200

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    # Este endpoint se utiliza para obtener una película por su ID único.
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return jsonify(movie), 200
    return jsonify({'error': 'Movie not found'}), 404

@app.route('/addMovie', methods=['POST'])
def add_movie():
    # Este endpoint se utiliza para agregar una nueva película a la lista.
    # Requiere un JSON con los campos 'id', 'title' y 'director'.
    new_movie = request.json
    if 'id' not in new_movie or 'title' not in new_movie or 'director' not in new_movie:
        return jsonify({'error': 'Invalid data'}), 400
    movies.append(new_movie)
    return jsonify(new_movie), 201

@app.route('/updateMovie/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    # Este endpoint se utiliza para actualizar los detalles de una película existente.
    # Se identifica la película usando su ID único y se envían los nuevos datos en un JSON.
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        update_data = request.json
        movie.update(update_data)
        return jsonify(movie), 200
    return jsonify({'error': 'Movie not found'}), 404

@app.route('/deleteMovie/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    # Este endpoint se utiliza para eliminar una película de la lista por su ID único.
    global movies
    movies = [m for m in movies if m['id'] != movie_id]
    return jsonify({'message': 'Movie deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
