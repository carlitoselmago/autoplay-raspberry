absparentFolder="/media/haxoorx/"
keywords=["VIDEO","MP4","MOV","AVI","WMV","MPEG","MKV","3GP","WEBM","MATROSKA"]
forbidden=["AUDIO FILE"]

import os
import magic
import subprocess
from time import sleep


newMedia=True
fileCount=0

while True:
	fileCount=0
	
	for path, subdirs, files in os.walk(absparentFolder):
		for name in files:
			fileURI=os.path.join(path, name)
			
			if os.path.isfile(fileURI):

				fileInfo =magic.from_file(fileURI).upper()
				match=False
				#print fileInfo,"::::",fileURI
				for keyword in keywords:
					if keyword in fileInfo:
						match=True

				for forb in forbidden:
					if forb in fileInfo:
						match=False

				if match:
					fileCount+=1
					if newMedia:
						command="xdg-open "+fileURI+"  >/dev/null"
						p = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
						(output, err) = p.communicate()  
						p_status = p.wait()
						
	if fileCount==0:
		newMedia=True
	else:
		newMedia=False


	sleep(4)
					