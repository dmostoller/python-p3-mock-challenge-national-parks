from classes.trip import Trip


class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 15:
            self.name = new_name
        else:
            raise Exception("name must be a string between 1 and 15 characters in leng")


    def trips(self):
        pass

    def national_parks(self):
        pass
