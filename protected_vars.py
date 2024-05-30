import sys

class Example:
    def __init__(self, var1=0, var2=True, var3='Hello') -> None:
        self.var1 = 0
        self._var2 = True
        self.__var3 = 'Hello'


# Example code to showcase logging functionality
if __name__ == '__main__':
    ex = Example()
    try:
        print(ex.__var3)
    except:
        print(sys.exc_info())
    # Erzeugt einen Fehler, da externer Zugriff auf geschützte Attribute nicht zulässig ist