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
* Use a text editor to
	* edit the getList.py file to point to the folder containing the films.
	* edit the spotmaps.py file to:
		* point to the folder containing the films
		* the handle/name of the contributor

## Procedure

* Run the getList.bat file to build a new list of processable files from the input folder. Note that due to the vagaries of openCV some files might be unreadable because of a format issue.
* Run the spotmaps.bat file to start the main process. Map, PNG and TIF files will be placed in the output folder.
* Zip up the files - including the processedFiles.txt file - and, depending on filesize, either:
	* attach the zip file to a new email to spotmaps@lavabit.com, or
	* put the zip file somewhere it can be downloaded and email spotmaps@lavabit.com with the download location
	
## Note

**Do not delete the processedFiles.txt file from the folder as this is added to and used with each new process.**
	
## License
spotmaps &copy; 2012 Andy Willis. [MIT licensed](http://www.opensource.org/licenses/mit-license.php)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.