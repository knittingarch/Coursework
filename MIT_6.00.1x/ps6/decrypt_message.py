class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        
        decrypt_message(self): You may find the helper function 
        is_word(wordlist, word) and the string method split() useful. Note 
        that is_word will ignore punctuation and other special characters 
        when considering whether a word is valid.
        '''

        #Prints out 'hello' but not the value of the shift
        
        best_shift = 0
        best_shift_encrypted_message = ''
        shifted_words = []
        
        for i in range(26):
            print('Iteration #', i)
            shift = 26 - i
            test_shift = self.apply_shift(shift)
            word_list = self.get_valid_words()
            words = test_shift.split(' ')
            for word in words:
                if is_word(word_list, word):
                    shifted_words.append(word)
                    print(len(shifted_words))
                else:
                    continue
            
        
        return shifted_words
