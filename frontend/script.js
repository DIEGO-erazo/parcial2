function calcularEstimacion() {
    const tipo = document.getElementById("tipoVehiculo").value;
    const distanciaInput = document.getElementById("distancia").value;
    const distancia = parseFloat(distanciaInput);

    if (isNaN(distancia) || distancia <= 0) {
        alert("Por favor, ingresa una distancia válida en kilómetros.");
        return;
    }

    let tarifaBase = 0;
    let factor = 0;
    let nombreServicio = "";

    if (tipo === "motocicleta") {
        tarifaBase = 2.00;
        factor = 0.35;
        nombreServicio = "Motocicleta";
    } else if (tipo === "automovil") {
        tarifaBase = 3.50;
        factor = 0.60;
        nombreServicio = "Automóvil";
    }

    const tarifaTotal = tarifaBase + (distancia * factor);

    // Actualización del DOM
    const resultadoDiv = document.getElementById("resultado");
    const textoResumen = document.getElementById("textoResumen");
    const textoPrecio = document.getElementById("textoPrecio");

    // Limpiar clases previas de diferenciación visual
    resultadoDiv.classList.remove("servicio-moto", "servicio-auto", "hidden");

    if (tipo === "motocicleta") {
        resultadoDiv.classList.add("servicio-moto");
    } else {
        resultadoDiv.classList.add("servicio-auto");
    }

    textoResumen.textContent = `Servicio seleccionado: ${nombreServicio} (${distancia.toFixed(2)} km)`;
    textoPrecio.textContent = `Estimación Total: $${tarifaTotal.toFixed(2)}`;
}