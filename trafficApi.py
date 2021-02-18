import os
from flask import Blueprint, render_template, request, json
import logging
from simulationClass.getVehicles import Routes

demos = Blueprint('queries', __name__, template_folder='templates', url_prefix='/trafficApi')
logger = logging.getLogger(__name__)
routesPath = '/home/yoda/Downloads/google_transit_dublinbus/shapes.txt'
route = Routes(routesPath)

@demos.route('/getLocationVehicles', methods=['GET'])
def newDemoScreen():
    logger.info('got the vehicle request')
    vehicleInfo = route.getVehicleInformation()
    returnList = []
    for i in vehicleInfo:
        returnList.append(vehicleInfo[i].toJson())
    return json.dumps({"status":"ok","routes":returnList})
