from SPARQLWrapper import SPARQLWrapper, JSON, BASIC
import logging,json
logging.basicConfig(format='[%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s] - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SQHelper:
    """
    Helper class to run the sparql query over the graphdb endpoints
    """
    def __init__(self,hostName,portName,repoName):
        self._hostName = hostName
        self._hostName = portName
        self._hostName = repoName
        self._endpoint = "http://{}:{}/repositories/{}".format(
            hostName,portName,repoName
        )
        self.connect()

    def connect(self):
        db = SPARQLWrapper(self._endpoint)
        self._db = db

    def execute(self,query):
        """
        execute the query and return a 2d list as result.
        First row of the results are the headers and the rows after it are the values.
        Args:
            query: query to execute.

        Returns:

        """
        self._db.setHTTPAuth(BASIC)
        self._db.setCredentials('login', 'password')
        self._db.setReturnFormat(JSON)
        self._db.setQuery(query)
        self._db.setMethod("POST")
        result = self._db.queryAndConvert()
        return self.convertJson(result)

    def convertJson(self,result):
        """
        convert json result to the array
        return array of results
        Args:
            result: result from query

        Returns:

        """
        returnResult = []
        jsonResults = result['results']['bindings']
        for jsonResult in jsonResults:
            keys = jsonResult.keys()
            if len(returnResult) == 0:
                returnResult.append(list(keys))
            tempResult = []
            for key in keys:
                tempResult.append(jsonResult[key]['value'])
            returnResult.append(tempResult)
        return returnResult