$(document).ready(function() {
    $('#productos_table').DataTable({
        ajax: productosUrl,  // esta variable la pasamos desde el template
        columns: [
            { data: 'idprod' },
            { data: 'nombre' },
            { data: 'precio' },
            { data: 'stock' },
            {
                data: 'idprod',
                render: function(data, type, row) {
                    return `
                        <a href="/editar_producto/${data}" class="btn btn-info btn-sm me-2">Editar</a>
                        <a href="/eliminar_producto/${data}" class="btn btn-danger btn-sm">Eliminar</a>
                    `;
                },
                orderable: false,
                searchable: false
            }
        ]
    });
});