import os
from flask import Blueprint, render_template, request, json
import logging
from sparqlHelper import SQHelper
from queryHash import queryHash
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
	return render_template('demos/index.html', querys=["Q1","Q2"])

@demos.route('/', methods=['POST'])
def upload_file_browse():
	logger.info("got post requst")
	queryId = json.loads(request.data)
	query = queryHash["Q1"]
	results = sqHelper.execute(query)
	return json.dumps({'success':True,'heading':results[0],'rowValues':results[1:]})
