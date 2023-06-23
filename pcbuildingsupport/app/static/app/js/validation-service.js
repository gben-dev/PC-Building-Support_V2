document.getElementById("form").addEventListener("submit", function(event) {
    var indicador = document.getElementById("txtIndicador").value;
    var fecha = document.getElementById("fecha").value;

    if (indicador == "" || fecha == "") {
        alert("Por favor, complete todos los campos antes de continuar.");
        event.preventDefault();
    }
});


