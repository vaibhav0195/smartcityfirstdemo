import logging
import logging.config
from responseFrame.getdirection import getLatAndLong
logging.basicConfig(format='[%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s] - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SpawingStation:
    """
    This class can be used as a sole entity which can act as a hospital or as a police station.
    """
    def __init__(self,name,startingLocation,numberOfspawns):
        """
        initialise the spawing station,
        Args:
            name: type of spawing station
            startingLocation: coords of the spawing station
            numberOfspawns: number of vans/vehicals this station can spawn
        """
        self._type = name
        self._locationpoint = startingLocation
        self._numberOfspawns = numberOfspawns
        logger.info("initialising the spawning station for type {}".format(name))

    def recieveInfo(self,location,numberofUnitsRequired,**kwargs):
        """
        function which should be called by the simulation software to send the responses to the location
        Args:
            severity: how bad is the disaster
            location: location coords of the disaster
            **kwargs:

        Returns:

        """
        if self.unitLeft() > numberofUnitsRequired:
            #TODO : update lat long according to new trafic simulation
            lat,long = getLatAndLong('',location,self._locationpoint)
            latLongList = []
            for idx in range(0,numberofUnitsRequired):
                self.sentunit()
                latLongList.append([lat,long])
            retJson = {'status':True,'latLong':latLongList,'numUnitsLeft':numberofUnitsRequired-self._numberOfspawns}
        else:
            retJson = {'status':False,'latLong':[],'numUnitsLeft':numberofUnitsRequired}
        return retJson

    def sentunit(self):
        """
        when we send a unit out just reduce the number
        Returns:

        """
        self._numberOfspawns -=1

    def unitBack(self):
        """
        when we get back a unit just increase the amount
        Returns:

        """
        self._numberOfspawns +=1

    def unitLeft(self):
        """
        returns the number of unit left in the station
        Returns:

        """
        return self._numberOfspawns

    def __str__(self):
        return self._type