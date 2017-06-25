var colors;
var colors_string;
var target;               
var guess_input;      
var finished = false;   
var guesses = 0;

function do_game() {
    colors = ['blue', 'cyan', 'gold', 'gray', 'green', 'magenta', 'orange', 'red', 'white', 'yellow'];
    colors_string = colors.join(", ");
    var random_number = Math.floor(Math.random(colors.length) * 10);
//    alert(random_number);
    target = colors[random_number];
//    alert(target);
    start = confirm("Ready to start playing?");
    if (start) {
        while (!finished) {
            guess_input = prompt("I am thinking of one of these colors:\n\n" + colors_string + "\n\n What color am I thinking of?");
            guesses += 1;
            finished = check_guess();
        }
    }
}

function check_guess() {
    if (colors.indexOf(guess_input) == -1) {
        alert("Sorry, I don't recognize your color.\n\n" +
              "Please try again.");
        return false;
    } else if (colors.indexOf(guess_input) > colors.indexOf(target)) {
        alert("Sorry, your guess is not correct!\n\n" +
              "Hint: your color is alphabetically higher than mine.\n\n" + 
              "Please try again.");
        return false;
    } else if (colors.indexOf(guess_input) < colors.indexOf(target)) {
        alert("Sorry, your guess is not correct!\n\n" +
              "Hint: your color is alphabetically lower than mine.\n\n" + 
              "Please try again.");
        return false;
    } else {
        document.body.style.backgroundColor = target;
        window.setTimeout(function() {
            alert("Congratulations! You have guessed the color!" + 
              "\n\nIt took you " + guesses + " guesses to finish the game!" +
              "\n\nYou can see the color in the background.");
        }, 1);
        return true;
    }

}