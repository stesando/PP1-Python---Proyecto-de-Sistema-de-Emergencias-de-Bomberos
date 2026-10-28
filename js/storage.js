const CLAVE = "favoritos";

export function obtenerFavoritos() {
    return JSON.parse(localStorage.getItem(CLAVE)) || [];
}

export function guardarFavoritos(favoritos) {
    localStorage.setItem(CLAVE, JSON.stringify(favoritos));
}

export function agregarFavorito(emergencia) {
    const favoritos = obtenerFavoritos();

    if (!favoritos.some(item => item.id === emergencia.id)) {
        favoritos.push(emergencia);
        guardarFavoritos(favoritos);
    }
}

export function quitarFavorito(id) {
    const favoritos = obtenerFavoritos()
        .filter(item => item.id !== id);

    guardarFavoritos(favoritos);
}