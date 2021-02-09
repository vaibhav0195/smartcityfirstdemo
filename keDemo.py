import os
from flask import Blueprint, render_template, request, json
import logging
import osmnx as ox
ox.config(use_cache=True, log_console=True)
import networkx as nx
import plotly.graph_objects as go
import numpy as np

demos = Blueprint('queries', __name__, template_folder='templates', url_prefix='/queries')
imagesInfo = {}
f = open('config.json', "r")
# Reading from file
constants = json.loads(f.read())
hostname  = constants['endpoint']
portname  = constants['port']
repoID	  = constants['repoID']
logger = logging.getLogger(__name__)
logger.info("connecting to sparql server at {}:{}".format(hostname,portname))

@demos.route('/', methods=['GET'])
def newDemoScreen():
	centerpoint = (53.34497205360536, -6.254528675545078)
	G = ox.graph_from_point(centerpoint, dist=1000, network_type='drive')
	logger.info('Got the graph for {} {}'.format(centerpoint[0], centerpoint[1]))
	startingCoord = (53.345188889254004, -6.254959737948171)
	endPointCoord = (53.34521771190481, -6.2505126354147365)
	logger.info('finding the shortest path')
	origin_node = ox.get_nearest_node(G, startingCoord)
	destination_node = ox.get_nearest_node(G, endPointCoord)
	route = nx.shortest_path(G, origin_node, destination_node, weight='length')
	long = []
	lat = []
	logger.info('got the shortest path. Retreiving the lats and longs')
	for i in route:
		point = G.nodes[i]
		long.append(point['x'])
		lat.append(point['y'])
	logger.info('got the lats and longs')
	newList = []
	for idx,tData in enumerate(lat):
		newList.append([tData,long[idx]])
	return render_template('demos/firstHtml.html',data=newList)