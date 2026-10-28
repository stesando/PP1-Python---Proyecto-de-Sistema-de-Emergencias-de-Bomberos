import {
    obtenerEmergencias,
    obtenerEmergencia
} from "./api.js";


const contenedor = document.querySelector("#contenedorEmergencias");


// Mostrar todas las emergencias
async function cargarEmergencias() {

    const emergencias = await obtenerEmergencias();

    contenedor.innerHTML = "";

    emergencias.forEach(emergencia => {

        const tarjeta = document.createElement("div");

        tarjeta.innerHTML = `
            <h3>${emergencia.emergency_type}</h3>

            <p>Solicitante: ${emergencia.caller_name}</p>

            <p>Ubicación: ${emergencia.location}</p>

            <p>Unidad: ${emergencia.unit}</p>

            <p>Estado: ${emergencia.status}</p>

            <button class="btnDetalle" data-id="${emergencia.id}">
                Ver detalle
            </button>
        `;

        contenedor.appendChild(tarjeta);
    });
}


// Mostrar detalle de una emergencia
async function mostrarDetalle(id) {

    const emergencia = await obtenerEmergencia(id);

    alert(`
        Emergencia #${emergencia.id}

        Solicitante: ${emergencia.caller_name}
        Ubicación: ${emergencia.location}
        Tipo: ${emergencia.emergency_type}
        Estado: ${emergencia.status}
        Unidad: ${emergencia.unit}
    `);
}


// Detectar clic en "Ver detalle"
contenedor.addEventListener("click", async (evento) => {

    if (evento.target.classList.contains("btnDetalle")) {

        const id = Number(evento.target.dataset.id);

        await mostrarDetalle(id);
    }
});


// Iniciar aplicación
cargarEmergencias();