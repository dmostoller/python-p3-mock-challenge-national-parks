
class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, 'name') and isinstance(value, str):
            self._name = value
        else:
            raise Exception("name must be a string")
            
        
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        pass

    def best_visitor(self):
        pass

    @classmethod
    def most_visited(cls):
        pass
