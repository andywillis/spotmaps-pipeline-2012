from __future__ import division
import os, glob, math, sys, time
import cv
from PIL import Image, ImageDraw
from numpy import *

os.system('cls')

# User defined vars - use double backslashes if folder is not in spotmaps folder
input = 'C:\\Users\\spotmaps\\process\\'
contributor = 'Andy Willis'

# Output and log files
output = 'output/'
log = 'log/spotmap.log'

# Init log file
if os.path.isfile(log) == True:
	os.remove(log)
	
# Get the file list
newlist = []
if os.path.isfile('newlist.txt') == False:
	smcf = open('newlist.txt','w')
	smcf.write('')
else:
	smcf = open('newlist.txt','r')
	line = smcf.readline()
	while line:
		newlist.append(line.rstrip('\n'))
		line = smcf.readline()
smcf.close()
print 'Retrieved new file information.'

# Get the processed file list
processedlist = []
if os.path.isfile('processedFiles.txt') == False:
	smcf = open('processedFiles.txt','w')
	smcf.write('')
else:
	smcf = open('processedFiles.txt','r')
	line = smcf.readline()
	while line:
		processedlist.append(line.rstrip('\n'))
		line = smcf.readline()
smcf.close()
print 'Retrieved processed files information.'

for infile in glob.glob(input + '*.avi'):

	startTime = time.time()
	
	path, filename = os.path.split(infile)
	filename = filename.split('.')[0]
	
	if filename in processedlist:
		print filename + ' - already completed.'
	else:
		if filename in newlist:
			capture = cv.CaptureFromFile(infile)
			totalFrames = int(cv.GetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_COUNT))
			if totalFrames == 0:
				print filename + ' - unable to read avi.'
				with open('processedFiles.txt', 'a') as myfile:
					myfile.write(spotmap['title'] + '\n')
					myfile.close()
			else:
				try:
					print '********'
					fps = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FPS ))
					print 'Analysing: ' + filename + ' / ' + str(totalFrames) + ' frames' + ' / ' +	str(fps) + ' fps'
					numberOfSpots = int(math.floor(totalFrames/fps))
					numberOfMinutes = int(math.ceil(numberOfSpots/60))
					trimFrames = numberOfSpots * fps
					missing = 60-numberOfSpots%60
					completeNumberOfSpots = numberOfSpots + missing
					if missing == 60: missing = 0

					# Build rgbArray, 4 columns because we're using RGBA instead of plain RGB.
					rgbData = zeros((completeNumberOfSpots, 3),dtype=int32)
					frame = 1
					spot = 1
					frameInSecond = 1
					spotR = spotG = spotB = 0
					while frame <= trimFrames:
						snapshot = cv.QueryFrame(capture)
						point = cv.CreateImage((1,1), cv.IPL_DEPTH_8U, 3)
						cv.Resize(snapshot, point, cv.CV_INTER_AREA)
						r = int(point[0,0][2])
						g = int(point[0,0][1])
						b = int(point[0,0][0])
						if frameInSecond > 1:
							spotR = spotR + r
							spotG = spotG + g
							spotB = spotB + b
						if frameInSecond == fps:
							percent = spot/numberOfSpots*100
							sys.stdout.write("Completed: %d%% \r" % (percent))
							spotR = int(spotR/fps)
							spotG = int(spotG/fps)
							spotB = int(spotB/fps)
							# NOTE: the full opacity value here '1' not '255' since the color array is used for Canvas rather than Python.
							rgbData[spot-1] = (spotR, spotG, spotB)
							frameInSecond = 0
							spot += 1
							spotR = spotG = spotB = 0
						frame += 1
						frameInSecond += 1
					second = 1
					while second <= missing:
						rgbData[spot-1] = (spotR, spotG, spotB)
						spot += 1
						second += 1

					# Build image
					spotW = 50
					spotH = 50
					spotG = 2
					canvasW = (spotW * 60) + (59 * spotG)
					canvasH = (spotH * numberOfMinutes) + (numberOfMinutes-1 * spotG)
					print 'Canvas is ' + str(canvasW) + ' x ' + str(canvasH)
					im = Image.new('RGB',(canvasW,canvasH),(255,255,255))
					draw = ImageDraw.Draw(im)
					x = 0
					y = 0
					spot = 1
					minute = 1
					second = 1
					while spot <= completeNumberOfSpots:
						if second == 61:
							x = 0
							y += spotH + spotG
							second = 1
						draw.rectangle((x, y, x + spotW, y + spotH),fill=(rgbData[spot-1][0], rgbData[spot-1][1], rgbData[spot-1][2]))
						x += spotW + spotG
						spot += 1
						second += 1
					second = 1
					imageName = filename + '.tif'
					im.save(output + imageName, 'TIFF')

					# Build thumbnail
					imageThumbName = filename + '_thumb.png'
					im_thumb = im.resize((int(math.ceil(im.size[0]/100*8)),int(math.ceil(im.size[1]/100*8))),Image.ANTIALIAS)
					im_thumb.save(output + imageThumbName, 'PNG')

					# Save information
					jsonName = filename + '.map'
					mapFile = open(output + jsonName, 'w')
					mapFile.write('{')
					mapFile.write('"title": "' + filename + '",')
					mapFile.write('"numberOfSpots": ' + str(completeNumberOfSpots) + ',')
					mapFile.write('"contributor": "' + contributor + '",')
					mapFile.write('"rgba": "')
					mapFile.write(str(rgbData.tolist()) + '"')
					mapFile.write('}')
					mapFile.close()

					# Update the processed files list
					with open('processedFiles.txt', 'a') as myfile:
						myfile.write(filename + '\n')
						myfile.close()
					endTime = time.time()-startTime
					minutes = str("%.2f" % (endTime / 60))
					msg1 = 'Completed in ' + minutes + ' minutes.'
					print msg1
					with open(log, 'a') as myfile:
						myfile.write(filename + ': ' + msg1 + '\n')
						myfile.close()
					print '********'
				except:
					msg2 = 'Error processing file'
					print msg2
					with open(log, 'a') as myfile:
						myfile.write(msg2 + ': ' + filename + '\n')
						myfile.close()
					print '********'
		else:
			msg3 = filename + ' - cannot be processed.'
			print msg3
			with open(log, 'a') as myfile:
				myfile.write(msg3 + '\n')
				myfile.close()