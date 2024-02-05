
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.__class__.all.append(self)
            
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        from classes.visitor import Visitor
        if isinstance(value, Visitor):
            self._visitor = value
        else:
            raise Exception("Visitor must be an instance of Visitor class!")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        from classes.national_park import NationalPark
        if isinstance(value, NationalPark):
            self._national_park = value
        else:
            raise Exception("National Park must be an instance of the National Park class")
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        self._end_date = value