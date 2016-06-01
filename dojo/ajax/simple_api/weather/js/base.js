$(document).ready(function() {

    $('form').submit(function() {
        var city = $('input[name=city]').val().trim();
        console.log("submitting form %s", city);
        var apiKey = "417bfa21a19d288bbac10483d562cac5";

        $.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&&callback=test&units=imperial&appid=" + apiKey, function(resp) {
            console.log(resp);
            var html_str = "<h1>Current Weather for " + resp.name + "</h1>";
            html_str += "<p><ul><li><b>Temperature</b>: " + resp.main.temp + " F</li>";
            html_str += "<li><b>Conditions</b>: " + resp.weather[0].description + "</li>";
            html_str += "<li><b>Wind Speed</b>: " + resp.wind.speed + " mph</li>";
            html_str += "<li><b>Relative Humidity</b>: " + resp.main.humidity + " %</li>";
            html_str += "<li><b>Maximum Daily Temperature</b>: " + resp.main.temp_max + " F</li>";
            html_str += "<li><b>Minimum Daily Temperature</b>: " + resp.main.temp_min + " F</li>";
            html_str += "</ul>";
            $('.bottom').html(html_str);
        }, 'json');

        return false; //this prevents bubble up event handling
    });
});
