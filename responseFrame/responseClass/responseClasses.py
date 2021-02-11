from responseFrame.responseClass import responseBase

class PoliceCar(responseBase,):
    def __init__(self,name,location):
        super().__init__(name,location)

    def actionAtSite(self):
        return 'block'

class Firetruck(responseBase,):
    def __init__(self,name,location):
        super().__init__(name,location)

    def actionAtSite(self):
        return 'Reduce Fire'

class Ambulance(responseBase,):
    def __init__(self,name,location):
        super().__init__(name,location)

    def actionAtSite(self):
        return 'Pick and go'
