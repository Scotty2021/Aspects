init -2 python:
    class Hint():
        def __init__( self, title, description, start_condition, complete_condition):
            self._title = title
            self._description = description
            self._start_condition = start_condition
            self._complete_condition = complete_condition

        # Return the text for the actual stage.
        @property
        def is_active( self ):
            try:
                return eval(self._start_condition)
            except NameError:
                return False    # on error its not active

        # Return the (human understandable) number of the actual stage. 
        @property
        def is_complete( self ):
            try:
                return eval(self._complete_condition)
            except NameError:
                return True     # on error its complete

        @property
        def title(self):
            return self._title

        @property
        def description(self):
            return self._description
