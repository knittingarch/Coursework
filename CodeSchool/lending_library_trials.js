lending_library_trials.js


// JUNK CODE WHILE I WORK //

// Search Functionality



			if(bookshelf.listOfBooks[i]["title"] === title && bookshelf.listOfBooks[i]["seriesNumber"] === seriesNumber) {
				return "You're in luck!  I have " + title + " " + seriesNumber + " available!";
			} else {
				return "Sorry, I currently don't have " + title + " " + seriesNumber + " on my shelf. Check back in the future!";
			}
			

> for(var i = 0; i < bookshelf.listOfBooks.length; i++) {
... console.log(bookshelf.listOfBooks[i]["title"]+ " " + bookshelf.listOfBooks[i]["seriesNumber"]);
... }

	searchForBook: function(seriesNumber) {
		for (var i = 0; i < bookshelf.listOfBooks.length; i++) {
			if(bookshelf.listOfBooks[i]["seriesNumber"] == seriesNumber) {
				console.log("You're in luck!  I have " + seriesNumber + " available!");
			} else {
				console.log("Sorry, I currently don't have " + seriesNumber + " on my shelf. Check back in the future!");
			}
		return seriesNumber;	
		}
	}


searchForBook: function(title, seriesNumber) {
		for (var i = 0; i < bookshelf.listOfBooks.length; i++) {
			if(bookshelf.listOfBooks[i]["title"] === title) {
				console.log("You're in luck!  I have " + title + " " + seriesNumber + " available!");
			} else {
				console.log("Sorry, I currently don't have " + title + " on my shelf. Check back in the future!");
			}
		return;	
		}
	}


// Create a Constructor Function for Book

function Book (shelf, title, seriesNumber, author, artist, colorist, genre, 
		rating, collectionType, size, cover, year) {
	bookshelf["# of books"]++;
	this.bookshelf = shelf;
	this.title = title;
	this.seriesNumber = seriesNumber;
	this.author = author;
	this.artist = artist;
	this.colorist = colorist;
	this.genre = genre;
	this.rating = rating;
	this.collectionType = collectionType;
	this.size = size;
	this.cover = cover;
	this.year =year;
}

Book.prototype = {
		borrowOne: function () { 
		bookshelf["# of books"]--;
		alert("Enjoy " + this.title + " " + this.seriesNumber + "!"); 
	},
		returnOne: function () { 
		bookshelf["# of books"]++;
		alert("Hope " + this.title + " " + this.seriesNumber + " was to your liking!"); 
	}
};

var TransM1 = new Book(bookshelf, "Transmetropolitan", 1, "Warren Ellis", "Darick Robertson", "Nathan Eyring", "Dystopian", "Mature", "Trade Comic", "Medium", "Paperback", 2009);



bookshelf.deleteBook = function(title){		
	this[title].title = title;
	var temp = this[title];
	delete this[title];
	return temp;
};


function addBook(shelf, title, seriesNumber, author, artist, colorist, genre, year, collectionType, size, hardness, year) {
	bookshelf["# of books"]++;
	bookshelf["book" + bookshelf["# of books"]] = {title: title, seriesNumber: seriesNumber, author: author, artist: artist, colorist: colorist, genre: genre, year: year, collectionType: collectionType, size: size, hardness: hardness, year: year};
}
