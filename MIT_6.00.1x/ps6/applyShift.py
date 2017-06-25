    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher = ''
        for ch in self.message_text:
            if ch in self.build_shift_dict():
                cipher += (self.build_shift_dict()[ch])
            elif ch not in string.ascii_lowercase:
                cipher += ch

        return cipher