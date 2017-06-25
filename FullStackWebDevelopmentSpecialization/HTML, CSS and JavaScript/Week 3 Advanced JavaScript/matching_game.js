var numberOfFaces = 5;
        
function generateFaces() {
    var theLeftSide = document.getElementById("leftside");
    var theRightSide = document.getElementById("rightside");
    var theBody = document.getElementsByTagName("body")[0];
            
    for (i = 1; i <= numberOfFaces; i++) {
        var randomTopPosition = Math.random() * 400;
        randomTopPosition = Math.floor(randomTopPosition);
        var randomLeftPosition = Math.random() * 400;
        randomLeftPosition = Math.floor(randomLeftPosition);
        var smiley = document.createElement("img");
        smiley.setAttribute("src", "http://home.cse.ust.hk/~rossiter/mooc/matching_game/smile.png");
        smiley.style.top = randomTopPosition + 'px';
        smiley.style.left = randomLeftPosition + 'px';
        theLeftSide.appendChild(smiley);
        leftSideImages = theLeftSide.cloneNode(true);
        leftSideImages.removeChild(leftSideImages.lastChild);
        theRightSide.appendChild(leftSideImages);
    }

    theLeftSide.lastChild.onclick = function (event) {
        event.stopPropagation();
        numberOfFaces += 5;
        while (theLeftSide.firstChild){
            theLeftSide.removeChild(theLeftSide.firstChild);
            theRightSide.removeChild(theRightSide.firstChild);
        }
        generateFaces();
    }
            
    theBody.onclick = function gameOver() {
        alert("Oh no! Game Over!");
        theBody.onclick = null;
        theLeftSide.lastChild.onclick = null;
    }
}