from classes.trip import Trip


class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, 'name') and isinstance(new_name, str):
            self.name = new_name
        else:
            raise Exception("name must be a string")
            
    
    
    def trips(self):
        pass

    def visitors(self):
        pass

    def total_visits(self):
        pass

    def best_visitor(self):
        pass

    @classmethod
    def most_visited(cls):
        pass
