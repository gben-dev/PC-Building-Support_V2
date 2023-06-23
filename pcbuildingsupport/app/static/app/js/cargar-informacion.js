$("#btnInformacion").click(function (event) {
    event.preventDefault();
    var pokemon = $("#txtIndicador").val().toLowerCase();
    
    $.ajax({
        url: "https://pokeapi.co/api/v2/pokemon/" + pokemon,
        error: function () {
        $("#info").html("<span>Pokemon no encontrado. Vuelve a buscar.</span>");
        },
        dataType: "json",
        success: function (data) {
        console.log(data);
        var $nombre_pokemon = data.name.toUpperCase();
        var $imagen_pokemon = data.sprites.front_default;
        var $tipo_pokemon = data.types.map(function(type) { return type.type.name.toUpperCase() }).join(", ");
        var $habilidades_pokemon = data.abilities.map(function(ability) { return ability.ability.name.toUpperCase() }).join(", ");

        $("#info").empty();
        $("#info")
            // .append("<img src='" + $imagen_pokemon + "'/>")
            // .append("<span>Nombre:</span> " + $nombre_pokemon)
            // .append("<span>Tipo:</span> " + $tipo_pokemon)
            // .append("<span>Habilidades:</span> " + $habilidades_pokemon);

        .append(`
            <img src="${$imagen_pokemon}" alt="${$nombre_pokemon}">
            <div>
                <span>Nombre: ${$nombre_pokemon}</span>
                <span>Tipo: ${$tipo_pokemon}</span>
                <span>Habilidades: ${$habilidades_pokemon}</span>
            </div>`);
        },
        type: "GET",
    });
});
