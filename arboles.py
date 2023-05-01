import tkinter as tk

# Lista de nombres de árboles
arboles = ["abedul", "abeto", "acacia", "acebo", "achicoria", "álamo", "árbol del pan", "arce", "avellano", "azufaifo", "baobab", "baño de oro", "bérbero", "brezo", "cactus", "caja", "calabaza", "camomila", "cedro", "cerezo", "cidro", "ciruela", "clavo", "coco", "corteza de roble", "corteza de sauce", "cresta de gallo", "crotón", "curuba", "dátil", "eucalipto", "falso pimentero", "fresno", "frutilla", "ginkgo", "girasol", "granado", "grosella espinosa", "guayaba", "henna", "hibisco", "higuera", "hinojo", "hisopo", "holly", "jacaranda", "jazmín", "jengibre", "jícara", "junco", "laurel", "lavanda", "lima", "lúpulo", "magnolia", "mandarina", "manzano", "maracuyá", "margarita", "menta", "mezquite", "mimosa", "mora", "moringa", "muérdago", "naranjo", "nogal", "olivo", "palma", "paraíso", "papaya", "peral", "perejil", "pino", "plátano", "plumeria", "pomelo", "poncirus", "porotillo", "quenepa", "quillay", "rábano", "rosa", "rosal silvestre", "sándalo", "sauce", "siempreviva", "spathodea", "tamarindo", "tangelo", "tejo", "temu", "tomate", "toronja", "uva", "vainilla", "vid", "yaca", "ylang ylang", "yuca"]

# Función que genera el nombre de árbol a partir del nombre ingresado
def generar_nombre_arbol():
    nombre = entrada_nombre.get()
    suma_ascii = sum(ord(c) for c in nombre)
    indice_arbol = suma_ascii % len(arboles)
    resultado_nombre_arbol.configure(text="Tu nombre de árbol es: " + arboles[indice_arbol])

# Crear la ventana principal y los widgets
ventana = tk.Tk()
ventana.title("Generador de nombres de árboles")
etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:")
entrada_nombre = tk.Entry(ventana)
boton_generar = tk.Button(ventana, text="Generar nombre de árbol", command=generar_nombre_arbol)
resultado_nombre_arbol = tk.Label(ventana, text="")

# Ubicar los widgets en la ventana
etiqueta_nombre.pack()
entrada_nombre.pack()
boton_generar.pack()
resultado_nombre_arbol.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()









