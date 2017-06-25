function CaretakerMedallion(caretaker) {
  this.caretaker = caretaker;
  switch(caretaker){
      case "PixelPriest": this.bronzeBanner = 'Omne initium est a pixel';
      case "FontFriar": this.circumscribedSquare = 'Venit Comic Sans';
      case "StyleSensei": this.innerRing = 'Ars autem est in aeternum';
  }
}

var friarMedallion = new CaretakerMedallion("FontFriar");

function ceremonialDagger(knight, rank) {
	this.length = 8;
	this.owner = knight;
	switch(rank){
		case "King": this.diamonds = 1;
		case "High Constable": this.amethyst = 2;
		case "Field Marshal": this.sapphires = 4;
		case "Captain": this.emeralds = 1;
		case "Knight": this.rubies = 4;
	}
}

var HCDagger = new ceremonialDagger("Philip", "High Constable");


var strength = true;
var fear = false;
var pack = {
  food: [ 'carrot',
          'mystery meat',
          'apple',
          'crust of bread',
          'spicy dried sausage',
          'carrot',
          'wedge of sharp cheese',
          'jug of milk',
          'mystery meat',
          'carrot'
  ],
  addFood: function(foodItem) {
    this.food = this.food || [];
    this.food.push(foodItem);
  },
  enoughFood: function(amount) {
    return(this.food.length >= amount);
  }
};

var surviveThisTrial = strength && !fear && pack.enoughFood(10);

console.log(surviveThisTrial);










var pocketStuff = ['Dragon Tooth', 'Adventure Diary', 'Silver Tiger Coin'];
var pocketContents = pocketStuff || [];


var isArthur = false;
var isKing = false;

isArthur && isKing ? function (){
						alert("Hail Arthur, King of the Britons!");
						console.log("Current weapon: Excalibur");
					}()
					:
					 function (){
					 	alert("Charge on, ye Knight, for the glory of the King!");
					 	console.log("Current weapon: Longsword");
					}();



swords: ["Broadsword",
		 "Katana", "Claymore",
		 "Scimitar"]

armory.retrieveSword= function (request){
	return (this.swords.indexOf(request) >= 0) ? this.swords.name : undefined;
	};		 					