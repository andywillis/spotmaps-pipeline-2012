from __future__ import division
import os, glob, math, sys, time
import cv

# User defined var - use double backslashes if folder is not in spotmaps folder
input = 'C:\\Users\\spotmaps\\process\\'

if os.path.isfile('newlist.txt') == True:
	os.remove('newlist.txt')

# Get the processed file list
smlist = []
for infile in glob.glob(input + '*.avi'):

	startTime = time.time()
	
	path, filename = os.path.split(infile)
	filename = filename.split('.')[0]

	print 'Analysing: ' + filename
	if filename in smlist:
		print 'Already completed.'
	if ' CD' in filename:
		print 'Disgarding ' + filename + ': file part of series'
	else:
		capture = cv.CaptureFromFile(infile)
		totalFrames = int(cv.GetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_COUNT))
		if totalFrames == 0:
			print 'Unable to read avi.'
		else:
			smlist.append(filename + '\n')
			with open('newlist.txt', 'a') as myfile:
				myfile.write(filename + '\n')
				myfile.close()