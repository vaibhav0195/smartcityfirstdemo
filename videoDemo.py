import os
from flask import Blueprint, render_template, request, json
import logging
from werkzeug import secure_filename
import urllib
from PIL import Image, ImageDraw
import time
from random import randint
import pandas as pd
import numpy as np
import unicodedata as uni
import cv2
import random
demos = Blueprint('videoDemo', __name__, template_folder='templates', url_prefix='/videoDemo')
imagesInfo = {}
logger = logging.getLogger(__name__)
postProcessPredictions = ""
currentName = ''
currentFolder = 'videoRender'

notAllowedWords = []
# def getImageText(image):
# 	imageWithSegments = connected_component.sortSegmentsUsingMaxYMeanIntersection(image)
# 	# print "sorted segments by yMean"
# 	linesArray = connected_component.findConnectedComponentsDetails(imageWithSegments, notAllowedWords)
#
# 	text = ''
# 	if linesArray:
# 		for line in linesArray:
# 			line = line.split(';;')[1]
# 			line = ' '.join(line.split('|'))
# 			text += line + '<br>'
# 	return text

@demos.route('/thumb', methods=['GET'])
def upload_file_thumb(type=None):
	filename = request.args.get("imageName")
	# print filename
	#folder = os.path.abspath("static/images/videoRender/")
	#filePath = os.path.join(folder,filename)
	#print filePath
	return json.dumps({'videoData': {'videoLocation': filename }})

@demos.route('/', methods=['GET'])
def newDemoScreen():
	folder = 'static/images/videoRender'
	files = [f for f in os.listdir(folder)]
	videoNames = files[:(len(files) - len(files) % 4)]
	t = [videoNames[i:i+4] for i in xrange(0, len(videoNames), 4)]
	return render_template('demos/videoDemo.html', videoNames=t, name=currentName, folder = currentFolder, firstImage = files[0])


# def saveToDB(imageProcessInfo):
# 	imageProcessInfo.save()
# 	segmentDict = []
# 	for segment in imageProcessInfo.segments_prefetch:
# 		segment.setId(None)
# 		currentSegmentDict = model_to_dict(segment, recurse=False)
# 		currentSegmentDict.update({'image':imageProcessInfo.getId()})
# 		segmentDict.append(currentSegmentDict)
# 	try:
# 		SegmentModel.insert_many(segmentDict).execute()
# 	except Exception, e:
# 		logger.error(e)
# 		logger.error('Error in saving Image Segments ')
# 	for prediction in imageProcessInfo.predictionResponses_prefetch:
# 		try:
# 			prediction.save()
# 		except:
# 			logger.error('Error in saving Image Prediction ')

@demos.route('/', methods=['POST'])
def upload_file_browse():
	folder = os.path.abspath("static/images/tempdownloaddemo/")
	if request.method == 'POST':
		file = request.files['file']
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(folder, filename))
			imagePath = os.path.join(folder, filename)
			orignalImagePathSave = 'static/images/tempdownloaddemo/'+filename
			predictions ,imagePath ,scores = runobjectDetectorOnImage.doSegmentation(imagePath=imagePath)
			predictionClasses = runobjectDetectorOnImage.doClassification(imagePath,predictions,scores)
			locationOfImage = runobjectDetectorOnImage.renderOnImage(imagePath=imagePath,pointsLoaded=predictions,scoresLoaded=scores,predictionClasses=predictionClasses)
			# print orignalImagePathSave,locationOfImage
	return json.dumps({'imageData':{'orignalImageLocation':filename,'segmentImage':filename}})

