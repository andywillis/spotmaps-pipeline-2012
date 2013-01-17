# Film colour blueprints pipeline

Python / OpenCV pipeline to process films and extract their colour information.

## Requirements

**Please note that these notes relate to a build in a Windows development environment.**

* [Python](http://python.org/) - version 2.7
* [Python Imaging Library](http://www.pythonware.com/products/pil/)
* [Numpy](http://sourceforge.net/projects/numpy/)
* [OpenCV](http://opencv.org/) - Ensure that you add the path of the OpenCV build module to your PYTHONPATH environment variable, for example: ;[root]\opencv\build\python\2.7;

## Preparation

* Run files in small batches of around 20.
* Rename the files so that they conform to the spotmap title style:  
	* Full Monty, The
	* Christmas Carol, A
	* Die Hard
* Edit the getList.py file to point to the folder containing the films.
* Edit the spotmaps.py file to:
	* point to the folder containing the films
	* the name of the contributor

## Procedure

* Run the getList.bat file to build a new list of processable files from the input folder. Note that due to the vagaries of openCV some files might be unreadable because of a format issue.
* Run the spotmaps.bat file to start the main process. Map, PNG and TIF files will be placed in the output folder.
* Zip up the files and, depending on filesize, either:
	* attach the zip file to a new email to spotmaps@lavabit.com, or
	* put the zip file somewhere it can be downloaded and email spotmaps@lavabit.com with the download location
	
## License
spotmaps &copy; 2012 Andy Willis  
Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php