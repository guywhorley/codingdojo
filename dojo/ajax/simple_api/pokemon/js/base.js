$(document).ready(function() {

    function getPokemonData() {}


    function buildPokemonImages(maxNum) {
        //Build up image grid
        var target = $('#pokemon');  //save reference to target div
        for (var i = 1; i <= maxNum; i++){
            $('<a href="#" id="poke-'+String(i)+'"><img src="http://pokeapi.co/media/img/'+i+'.png"/></a>').appendTo($(target));
             //attach click event handler to this pokemon anchor tag
            $('#poke-' + i).click(function() {
                var pid = $(this).attr('id');
                    //$('#poke-data').html('<p>You clicked pokemon #' + pid + '</p>');
                    //console.log("you clicked pokemon:%s", pid);

                $.get("http://pokeapi.co/api/v1/pokemon/"+pid.substr(5)+"/", function(resp) {
                    console.log(resp);
                    // types
                    var html_str = "";
                    html_str += "<h4>Name: " + resp.name + "</h4>";
                    html_str += "<h4>Types:</h4>";
                    html_str += "<ul>";
                    for (var i=0; i<resp.types.length; i++) {
                        html_str += "<li>" + resp.types[i].name + "</li>";
                    }
                    html_str += "</ul>";
                    html_str += "<h4>Height: " + resp.height + " inches</h4>";
                    html_str += "<h4>Weight: " + resp.weight + " kilograms</h4>";
                    $('#poke-data').html(html_str);
                }, "json");
            });
        } //close for
    } //close function


    buildPokemonImages(155);

});
