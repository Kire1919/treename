from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/arboles')
def arboles():
    nombre = request.args.get('nombre', '')
    try:
        resultado = subprocess.check_output(['python', 'arboles.py', nombre], cwd='C:/miapp')
        return jsonify({'arbol': resultado.decode().strip()})
    except subprocess.CalledProcessError:
        return jsonify({'error': 'No se ha podido generar el árbol'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
