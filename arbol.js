function obtenerArbol() {
    var nombre = document.getElementById("nombre").value;
    var url = "http://127.0.0.1:5000/arboles?nombre=" + nombre;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("resultado_nombre_arbol").innerHTML = "Tu nombre de árbol es: " + this.responseText;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}
