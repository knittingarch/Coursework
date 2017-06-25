    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Your code here

        print(word)
        self.hand2 = []
        
        for i in word:
            for j in self.hand.keys():
                print(i, j)
                if i == j:
                    print('yup')
                    self.hand2.append(j)
                    self.hand.pop(j)
                    break
                else:
                    print('nope')
        print(len(self.hand2))
        if len(self.hand2) == len(word):
            return True
        else:
            return False