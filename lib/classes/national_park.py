from collections import Counter

class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name

        self.__class__.all.append(self)
    
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
        return len([trip for trip in self.trips()])

    def best_visitor(self):
        count = Counter(self.visitors())
        return max(count, key=count.get)

    
    @classmethod
    def most_visited(cls):
        count = Counter(cls.all)
        return max(count, key=count.get)
        
