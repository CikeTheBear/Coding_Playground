// 1. Capturamos los elementos del HTML por su ID
const inputCantidad = document.getElementById('diceCount');
const inputCaras = document.getElementById('diceSides');
const botonTirar = document.getElementById('rollButton');
const contenedorResultados = document.getElementById('resultsContainer');

// 2. Comprobación (opcional)
console.log("Sistema cargado. Elementos capturados.");

// 3. Escuchar el clic en el botón
botonTirar.addEventListener('click', function() {
    
    // A. Leer lo que el usuario escribió en los inputs
    // Usamos parseInt() para convertir el texto a número entero
    const cantidad = parseInt(inputCantidad.value);
    const caras = parseInt(inputCaras.value);

    // B. Limpiar resultados anteriores (para que no se acumulen infinitamente)
    contenedorResultados.innerHTML = '';

    // C. Bucle: Repetir la acción tantas veces como dados haya pedido el usuario
    for (let i = 0; i < cantidad; i++) {
        
       const nuevoDado = document.createElement('p');
        contenedorResultados.appendChild(nuevoDado);

        // 2. Calcular el resultado FINAL (El verdadero)
        const resultadoFinal = Math.floor(Math.random() * caras) + 1;

        // 3. ANIMACIÓN: Cambiar el número cada 50ms (efecto ruleta)
        // Guardamos este intervalo en una variable para poder detenerlo luego
        const agitador = setInterval(function() {
            // Mientras espera, muestra números aleatorios puramente visuales
            nuevoDado.innerText = Math.floor(Math.random() * caras) + 1;
        }, 50);

        // 4. DETENER: Después de 1000ms (1 segundo)
        setTimeout(function() {
            clearInterval(agitador); // Detiene la ruleta
            nuevoDado.innerText = resultadoFinal; // Muestra el valor real
            
            // Opcional: Agregar una clase para cambiar el color al finalizar
            /*nuevoDado.style.borderColor = "#007bff"; 
            nuevoDado.style.color = "#000";*/
        }, 1000);
    }
});