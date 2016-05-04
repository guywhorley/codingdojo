/*
* file: pacman.js:
* desc: logic for my pacman game, practicing html and css.
* author: Guy Whorley
*/
$(function() {

/*-- Initialize game world
  --------------------------------------*/
var score=0;
var totalCount = 67;
var player = {
    row: 5,
    col: 11
};  //store player coords

var minRow = 1;
var maxRow = 10;
var minCol = 1;
var maxCol = 10;

var world = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2],
    [2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 2],
    [2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2],
    [2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 3],
    [2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2],
    [2, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2],
    [2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2],
    [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
    [2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
];

/*-- play pacman
  ---------------------------------------*/
resetGame();

document.onkeydown = function(e) {
    //current player position
    var row = player.row;
    var col = player.col;
    var newRow = player.row;
    var newCol = player.col;
    var bgUrl = "url('images/Pacman-"; // face pacman the correct direction
    //log.debug("player keypress: " + e.keyCode + " orig-coords("+row+","+col+")");
    //log.debug("Current Score: " + score);
     if (e.keyCode==37) { //left
         bgUrl += "left.gif')";
        newCol--;
    } else if (e.keyCode==39) { //right
        bgUrl += "right.gif')";
        newCol++;
    } else if (e.keyCode==38) { //up
        bgUrl += "up.gif')";
        newRow--;
    } else if (e.keyCode==40) { //down
        bgUrl += "down.gif')";
        newRow++;
    } //row-col adjust

    if (newCol < minCol || newCol > maxCol) {
        //log.warn("out-of-bounds column (" + newRow +", "+ newCol+")");
    } else if (newRow < minRow || newRow > maxRow) {
        //log.warn("out-of-bounds row (" + newRow +", " + newCol + ")");
    } else { //valid move - check for blocks and coins
        var srcId = "#sq-" + row + "" + col;
        var destId = "#sq-" + newRow + "" + newCol;
        var destClass = $(destId).attr("class");
        if (destClass === "block") {
            //log.info("Hitting block. Ignoring move.");
        } else if (destClass === "coin") {
            score++;
            $('h1').text("Score: " + score);
            $(srcId).removeClass();
            $(srcId).removeAttr("style");
            $(destId).css("background", bgUrl);
            $(destId).removeClass().addClass("pacman");
            document.getElementById("chomp").play();
            $('#scr-box').text("Score: " + score);
            player.row = newRow;
            player.col = newCol;
            if (score > totalCount) { isWinner(); }
        } else { //empty - move but don't collect coin
            $(srcId).removeClass();
            $(srcId).removeAttr("style");
            $(destId).removeClass().addClass("pacman");
            $(destId).css("background", bgUrl);
             player.row = newRow;
             player.col = newCol;
        } //mv onto empty space
    } //valid moves
}; //move

//reset game to default state
function resetGame() {
    score = 0;
    $('#score-box').text("Score: 0");
    player.row = 5;
    player.column = 11;
    $("#gamescreen").append(createWorld(world));
} //reset game

// check if winner
function isWinner() {
    document.getElementById("end-game").play();
    var msg="<p id='play-again'>You won! Great Job. Click <a href=''>here</a> to play again.</p>";
    $('#scr-box').after(msg);
    $('#scr-box').text("Score: " + score);
    $('#play-again').click(function() {
        location.reload();
    });
} //isWinner

// Create the world - populate the board
function createWorld(world) {
    var output = " ";
    for (var i=0; i<world.length; i++) {
        output += "<div class='game-row'>\n\t";
        for (var j=0; j<world[i].length; j++) {
            var curr = world[i][j];
            var idStr = "sq-" + i + "" + j;
            if (curr == 2) { output += "<div id='" + idStr + "' class='block'></div>\t"; }
            else if (curr == 1) { output += "<div id='"+idStr+"' class='coin'></div>\t";}
            else if (curr == 3) { output += "<div id='"+idStr+"' class='pacman'></div>\t"; }
            else if (curr == 4) { output += "<div id='"+idStr+"' class='empty'></div>\t"; }
        } //j
        output += "</div>\n";
    } //i
    output += "</div>";
    return output;
 } //displayWorld
});
