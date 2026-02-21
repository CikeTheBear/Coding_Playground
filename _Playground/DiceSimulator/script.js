// ==========================================
// PARTE 1: LÓGICA DE LOS DADOS
// ==========================================
const inputCantidad = document.getElementById('diceCount');
const inputCaras = document.getElementById('diceSides');
const botonTirar = document.getElementById('rollBtn');
const contenedorResultados = document.getElementById('resultsContainer');

botonTirar.addEventListener('click', function () {
    const cantidad = parseInt(inputCantidad.value);
    const caras = parseInt(inputCaras.value);
    contenedorResultados.innerHTML = '';

    for (let i = 0; i < cantidad; i++) {
        const nuevoDado = document.createElement('p');
        contenedorResultados.appendChild(nuevoDado);

        const resultadoFinal = Math.floor(Math.random() * caras) + 1;

        // Animación
        const agitador = setInterval(function () {
            nuevoDado.innerText = Math.floor(Math.random() * caras) + 1;
        }, 50);

        setTimeout(function () {
            clearInterval(agitador);
            nuevoDado.innerText = resultadoFinal;
            nuevoDado.style.border = "2px solid #007bff";
            nuevoDado.style.backgroundColor = "#fff";
        }, 1000);
    }
});

// ==========================================
// PARTE 2: PERSISTENCIA (GUARDAR DATOS)
// ==========================================
const inputsPersonaje = document.querySelectorAll('.character-sheet input, .character-sheet textarea');

function guardarDato(evento) {
    const input = evento.target;
    // Solo guardamos si el input tiene un ID y NO es el selector de archivos
    if (input.id && input.type !== 'file') {
        localStorage.setItem(input.id, input.value);
    }
}

function cargarDatos() {
    inputsPersonaje.forEach(input => {
        if (input.id && input.type !== 'file') {
            const valorGuardado = localStorage.getItem(input.id);
            if (valorGuardado) {
                input.value = valorGuardado;
            }
        }
    });
}

inputsPersonaje.forEach(input => {
    input.addEventListener('input', guardarDato);
});

cargarDatos(); // Cargar textos al iniciar

// ==========================================
// PARTE 3: SUBIDA DE IMAGEN (FILE UPLOAD)
// ==========================================
const inputSubir = document.getElementById('imageUpload');
const displayImagen = document.getElementById('imageDisplay');

// Función para mostrar la imagen en pantalla
function mostrarImagen(origen) {
    displayImagen.innerHTML = ''; // Limpia el texto "Sin imagen"
    
    const img = document.createElement('img');
    img.src = origen;
    img.className = "character-image"; // Clase CSS para ajustar tamaño
    
    displayImagen.appendChild(img);
}

// Escuchar cambios en el input de archivo
inputSubir.addEventListener('change', function(evento) {
    const archivo = evento.target.files[0];

    if (archivo) {
        const lector = new FileReader();

        lector.onload = function(e) {
            const resultadoBase64 = e.target.result;
            
            // 1. Mostrar
            mostrarImagen(resultadoBase64);
            
            // 2. Guardar
            try {
                localStorage.setItem('savedImage', resultadoBase64);
            } catch (error) {
                console.error("Imagen muy grande para guardar", error);
                alert("Imagen mostrada, pero es muy pesada para guardarse automáticamente.");
            }
        };

        lector.readAsDataURL(archivo);
    }
});

// Cargar imagen guardada al iniciar
const imagenGuardada = localStorage.getItem('savedImage');
if (imagenGuardada) {
    mostrarImagen(imagenGuardada);
}

console.log("Sistema completo cargado.");