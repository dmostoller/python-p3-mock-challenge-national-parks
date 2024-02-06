
class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("name must be a string between 1 and 15 characters in length")

    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
