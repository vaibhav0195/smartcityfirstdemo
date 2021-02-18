"""
	This file contains details of application server. Things like initialising database connections, creating Flask application and running tornado server are done here.
	For production deployment, it picks configuration from 'mlocrappdemo/config/server/config.txt' which is symlinked from '/var/mlocrappdemo/config/config.txt'
"""

import logging
import logging.config
import os
import json

logging.basicConfig(format='[%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s] - %(message)s', level=logging.DEBUG)

from flask import Flask, send_from_directory
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
import trafficApi

logger = logging.getLogger(__name__)
f = open('config.json', "r")
constants = json.loads(f.read())
if __name__ == '__main__':

	logger.info('Creating Flask application context')
	# Creating Flask application object
	app = Flask(__name__) # Initialize the Flask application
	# Registering different APIs
	logger.info('Registering demo APIs blueprints')
	app.register_blueprint(trafficApi.demos)

	# @app.route('/favicon.ico')
	# def favicon():
	# 	return send_from_directory(os.path.abspath('static/'),'bird.png')

	@app.after_request
	def setHeaders(response):
		response.headers["Access-Control-Allow-Origin"] = '*'
		response.headers["Access-Control-Allow-Headers"] = '*'
		return response

	port = constants["appport"]

	logger.debug("Setting Flask application context logger as same as this server's logger")
	# app.logger.addHandler(file_handler)
	app.logger_name = 'server' #TODO: see if it works

	# Wrapping Flask application in WSGI container of tornado
	logger.info('Creating WSGI wrapper around Flask application context')
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(port)

	# Starting tornado server
	logger.info("Web application server started on port - {}".format(port))
	IOLoop.instance().start()
