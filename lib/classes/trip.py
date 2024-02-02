
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

    
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, new_visitor)
        from visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception("Visitor must be an instance of Visitor class!")