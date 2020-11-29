# from SPARQLWrapper import SPARQLWrapper, JSON, BASIC
from sparqlHelper import SQHelper
import logging,json
logging.basicConfig(format='[%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s] - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    f = open('config.json', "r")
    constants = json.loads(f.read())
    hostname = constants['endpoint']
    portname = constants['port']
    repoID = constants['repoID']
    endpoint = "http://{}:{}/repositories/{}".format(hostname,portname,repoID)
    logger.info("connecting to sparql at {}:{}".format(hostname,portname))
    q = """SELECT DISTINCT * WHERE { 
               ?Record a <http://example.org/csv/Record>; <http://example.org/csv/taxonname> ?taxonname; 
        <http://example.org/csv/lifestage> ?lifestage
         FILTER(?lifestage = 'Adult') } """
    sq = SQHelper(hostname,portname,repoID)
    result = sq.execute(q)
    logger.info("connected to sparql")
