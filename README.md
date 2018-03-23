Picinorder
==========

### short description:
this tool is used to organize pictures

### usage:

1. change the value of source_path and target_path in main_basic.py and run main_basic.py

### requirements: 
1. copying

	(X) All files will be traversed in the input folder and its sub-folders. 

	(X) File will be treated as picture if it has an extension "jpg", "jpeg". Pictures files will be further handled by this tool. 

	(X) Pictures will be put in the target place based on taken time(EXIF DateTimeOriginal).

	(X) If the picture does not have DateTimeOriginal information, the file name shall be parsed in format YYYYMMDD_ to get the taken date. 

	(X) Another way to get the taken date is from the picture's path. The path will be parsed in format YYYY/MM/DD. 

	(X) Target place is organized with the folder and sub-folder YYYY, MM, DD, (target/YYYY/MM/DD, its taken time). If no such folder, it will be created. 

	(X) The pictures that taken time are unknown will be copied to folder target/picture. The original folder hierarchy shall be kept. Before this copying, check if a file with same name exists, if yes and file is not the same, add "_c" in the file name. 

1. auto-renaming

	(X) renaming is done automatically during copying process, if auto-renaming condition is fullfilled. 

	(X) Picture will be auto-renamed by YYYYMMDD_HHMMSS and its original extension. YYYYMMDD_HHMMSS is from DateTimeOriginal. 

	(X) If two pictures have the same file names, compare them to see if they are the same file (md5sum). If same, no need to copy and rename the second. If not, add "_c" in the file name. 

	(X) If a picture does not have a DateTimeOriginal, but taken date can be extracted from file name, HHMMSS will be set as 246060. A picture with HHMMSS 246060 shall be renamed with YYYYMMDD_246060_IIII. (IIII is extracted from its original file name, if it can't be done, use R with a random number between 000~999, e.g. R123) 

	(X) When renaming time conflict pictures, all the pictures taken in the same time (name starting with YYYYMMDD_HHMMSS_) will be checked if a same copy already exists. 

1. manual adjustment for pictures taken date unknown

	(X) Put the pictures you want to rename in the path YYYY/MM/DD based on the date you can recall. 

	(X) YYYY/MM/DD, 0 can be accepted, so it is encouraged to use that when exact date is not clear. 

1. data safty and cleaniness

	(X) A log file will be generated, named by its running date. 

	(X) All files under source path should be copied to somewhere under target path (keep the same folder hierarchy if not picture), unless there are a same copy already exists. If it can't be done, the user should be notified. 
	- "mp4" will be treated as video, and copied to target/video
	- "git" will be treated as git, and copied to target/git
	- others will be copied to target/other

	(X) If source path and target path should not include each other. Prevent running in such case. 

	(X) md5sum of any file handled should not be changed. 

1. redundant file detection

	(X) If a picture has DateTimeOriginal, the same copy will be find during copying process and only one copy will be kept. It's only necessary to find same file with HHMMSS 246060. 

	(X) The user will be notified, no further automatic action. 

1. user interface

	(X) User should input source path and target path

	(X) Task selection

	(X) Start button

	(X) Running log

	(X) TBD: picture presenting user interface

	(X) TBD: tag search user interface

	(X) TBD: tagging user interface

	(X) TBD: batch-tagging user interface

	(X) TBD: auto-tagging user interface

1. tagging

	(X) Tag of each picture will be kept in a separated database.

	(X) A picture could have multiple tags.

	(X) Tag can be added to a picture; tag can be deleted from a picture. 

	(X) Chinese is allowed for tag.

	(X) Batch-tagging is possible for folders.

	(X) Auto-tagging is possible based on face recognition technology.

	(X) Auto-tagging is possible based on other machine learning technology.



