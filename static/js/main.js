const btnEliminar = document.querySelectorAll('.btn-delete')

if (btnEliminar) {
    const btnarray = Array.from(btnEliminar);
    btnarray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('¿Esta seguro que desea eliminar?')) {
                e.preventDefault();
            }
        });
    });
}