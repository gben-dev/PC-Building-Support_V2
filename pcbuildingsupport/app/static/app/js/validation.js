// Obtener el formulario
const formulario = document.querySelector('form');

// Escuchar el evento 'submit' del formulario
formulario.addEventListener('submit', function(evento) {
// Obtener las etiquetas de selección
const procesador = document.querySelector('#procesador');
const memoria_ram = document.querySelector('#memoria_ram');
const disco_duro = document.querySelector('#disco_duro');
const tarjeta_video = document.querySelector('#tarjeta_video');
const fuente_poder = document.querySelector('#fuente_poder');

// Validar que se haya seleccionado una opción en cada etiqueta de selección
if (!procesador.value || !memoria_ram.value || !disco_duro.value || !tarjeta_video.value || !fuente_poder.value) {
    // Mostrar un mensaje de error
    alert('Por favor seleccione una opción en todas las etiquetas de selección.');
    
    // Prevenir el envío del formulario
    evento.preventDefault();
}
});