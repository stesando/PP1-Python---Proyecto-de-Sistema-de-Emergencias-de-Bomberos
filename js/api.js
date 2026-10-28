const URL = "http://127.0.0.1:8000/emergencias";

export async function obtenerEmergencias() {
    const respuesta = await fetch(URL);
    return await respuesta.json();
}

export async function crearEmergencia(emergencia) {
    const respuesta = await fetch(URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emergencia)
    });

    return await respuesta.json();
}

export async function editarEmergencia(id, emergencia) {
    const respuesta = await fetch(`${URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emergencia)
    });

    return await respuesta.json();
}

export async function eliminarEmergencia(id) {
    await fetch(`${URL}/${id}`, {
        method: "DELETE"
    });
}
export async function obtenerEmergencia(id) {
    const respuesta = await fetch(`${URL}/${id}`);
    const datos = await respuesta.json();

    return datos;
}

export async function crearEmergencia(emergencia) {
    const respuesta = await fetch(URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(emergencia)
    });

    return await respuesta.json();
}