class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        self.status = status
        statuses = ["citizen", "legal_resident", "illegal_resident"]
        if status not in statuses:
            raise ValueError
        else:
            self.status = status

    def getStatus(self):
        """
        Returns the status
        """
        return self.status
        

b = USResident('jon cage', 'non-resident')
print(b.getStatus())


class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        self.status = status
        statuses = ["citizen", "legal_resident", "illegal_resident"]
        if status in statuses:
            self.status = status
        raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status
        




class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        self.status = status
        statuses = ["citizen", "legal_resident", "illegal_resident"]
        try:
            if status in statuses:
                self.status = status
        except:
            if status not in statuses:
                raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status

7.5 Points Only 
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        self.status = status
        statuses = ["citizen", "legal_resident", "illegal_resident"]
        if status not in statuses:
            raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status