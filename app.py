from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Lista de nombres de árboles
arboles = ["abedul", "abeto", "acacia", "acebo", "achicoria", "álamo", "árbol del pan", "arce", "avellano", "azufaifo", "baobab", "baño de oro", "bérbero", "brezo", "cactus", "caja", "calabaza", "camomila", "cedro", "cerezo", "cidro", "ciruela", "clavo", "coco", "corteza de roble", "corteza de sauce", "cresta de gallo", "crotón", "curuba", "dátil", "eucalipto", "falso pimentero", "fresno", "frutilla", "ginkgo", "girasol", "granado", "grosella espinosa", "guayaba", "henna", "hibisco", "higuera", "hinojo", "hisopo", "holly", "jacaranda", "jazmín", "jengibre", "jícara", "junco", "laurel", "lavanda", "lima", "lúpulo", "magnolia", "mandarina", "manzano", "maracuyá", "margarita", "menta", "mezquite", "mimosa", "mora", "moringa", "muérdago", "naranjo", "nogal", "olivo", "palma", "paraíso", "papaya", "peral", "perejil", "pino", "plátano", "plumeria", "pomelo", "poncirus", "porotillo", "quenepa", "quillay", "rábano", "rosa", "rosal silvestre", "sándalo", "sauce", "siempreviva", "spathodea", "tamarindo", "tangelo", "tejo", "temu", "tomate", "toronja", "uva", "vainilla", "vid", "yaca", "ylang ylang", "yuca"]

# Función que genera el nombre de árbol a partir del nombre ingresado
def generar_nombre_arbol(nombre):
    suma_ascii = sum(ord(c) for c in nombre)
    indice_arbol = suma_ascii % len(arboles)
    print("Indice del árbol:", indice_arbol) 
    return arboles[indice_arbol]


@app.route('/arboles')
def obtener_nombre_arbol():
    nombre = request.args.get('nombre', '')
    nombre_arbol = generar_nombre_arbol(nombre)
    comando = ['python', 'arboles.py', nombre_arbol]
    resultado = subprocess.check_output(comando, cwd='C:/miapp')
    return jsonify({'nombre_arbol': nombre_arbol, 'resultado': resultado.decode()})

if __name__ == '__main__':
    app.run(debug=True)

