import os
from flask import Blueprint, render_template, request, json
import logging
from sparqlHelper import SQHelper
from queryHash import queryHash,queryQuestion
demos = Blueprint('queries', __name__, template_folder='templates', url_prefix='/queries')
imagesInfo = {}
f = open('config.json', "r")
# Reading from file
constants = json.loads(f.read())
hostname  = constants['endpoint']
portname  = constants['port']
repoID	  = constants['repoID']
sqHelper  = SQHelper(hostname,portname,repoID)
logger = logging.getLogger(__name__)
logger.info("connecting to sparql server at {}:{}".format(hostname,portname))

@demos.route('/', methods=['GET'])
def newDemoScreen():
	return render_template('demos/index.html', querys=queryQuestion)

@demos.route('/', methods=['POST'])
def upload_file_browse():
	logger.info("got post requst")
	queryData = json.loads(request.data)
	queryId   = queryData["queryHash"].split(':')[0]
	queryParams   = queryData["queryParams"]
	if queryId not in ["Q2","Q3","Q10"]:
		if queryId == "Q4":
			query = queryHash[queryId]%(queryParams)
		else:
			query = queryHash[queryId]%(queryParams,queryParams)
	else:
		query = queryHash[queryId]
	results = sqHelper.execute(query)
	if len(results) == 0:
		rowValues = []
		heading  = []
	else:
		heading = results[0]
		rowValues = results[1:]
	return json.dumps({'success':True,'heading':heading,'rowValues':rowValues})
