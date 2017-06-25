def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
    dict = {}

    for ch in string.ascii_lowercase:
        ch2 = ord(ch)
        if ch2 + shift <= 122:
            ch2 += shift
            dict[ch] = chr(ch2)
        else:
            ch2 = (ch2 + shift) - 26
            dict[ch] = chr(ch2)