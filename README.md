Picinorder
==========

### short description:
this tool is used to organize pictures

### usage:

1. change the value of source_path and target_path in main_basic.py and run main_basic.py

### requirements: 
1. copying

	- [ ] All files will be traversed in the input folder and its sub-folders. 

	- [ ] File will be treated as picture if it has an extension "jpg", "jpeg". Pictures files will be further handled by this tool. 

	- [ ] Pictures will be put in the target place based on taken time(EXIF DateTimeOriginal).

	- [ ] If the picture does not have DateTimeOriginal information, the file name shall be parsed in format YYYYMMDD_ to get the taken date. 

	- [ ] Another way to get the taken date is from the picture's path. The path will be parsed in format YYYY/MM/DD. 

	- [ ] Target place is organized with the folder and sub-folder YYYY, MM, DD, (target/YYYY/MM/DD, its taken time). If no such folder, it will be created. 

	- [ ] The pictures that taken time are unknown will be copied to folder target/picture. The original folder hierarchy shall be kept. Before this copying, check if a file with same name exists, if yes and file is not the same, add "_c" in the file name. 

1. auto-renaming

	- [ ] renaming is done automatically during copying process, if auto-renaming condition is fullfilled. 

	- [ ] Picture will be auto-renamed by YYYYMMDD_HHMMSS and its original extension. YYYYMMDD_HHMMSS is from DateTimeOriginal. 

	- [ ] If two pictures have the same file names, compare them to see if they are the same file (md5sum). If same, no need to copy and rename the second. If not, add "_c" in the file name. 

	- [ ] If a picture does not have a DateTimeOriginal, but taken date can be extracted from file name, HHMMSS will be set as 246060. A picture with HHMMSS 246060 shall be renamed with YYYYMMDD_246060_IIII. (IIII is extracted from its original file name, if it can't be done, use R with a random number between 000~999, e.g. R123) 

	- [ ] When renaming time conflict pictures, all the pictures taken in the same time (name starting with YYYYMMDD_HHMMSS_) will be checked if a same copy already exists. 

1. manual adjustment for pictures taken date unknown

	- [ ] Put the pictures you want to rename in the path YYYY/MM/DD based on the date you can recall. 

	- [ ] YYYY/MM/DD, 0 can be accepted, so it is encouraged to use that when exact date is not clear. 

1. data safty and cleaniness

	- [ ] A log file will be generated, named by its running date. 

	- [ ] All files under source path should be copied to somewhere under target path (keep the same folder hierarchy if not picture), unless there are a same copy already exists. If it can't be done, the user should be notified. 
		- "mp4" will be treated as video, and copied to target/video
		- "git" will be treated as git, and copied to target/git
		- others will be copied to target/other

	- [ ] If source path and target path should not include each other. Prevent running in such case. 

	- [ ] md5sum of any file handled should not be changed. 

1. redundant file detection

	- [ ] If a picture has DateTimeOriginal, the same copy will be find during copying process and only one copy will be kept. It's only necessary to find same file with HHMMSS 246060. 

	- [ ] The user will be notified, no further automatic action. 

1. user interface

	- [ ] User should input source path and target path

	- [ ] Task selection

	- [ ] Start button

	- [ ] Running log

	- [ ] TBD: picture presenting user interface

	- [ ] TBD: tag search user interface

	- [ ] TBD: tagging user interface

	- [ ] TBD: batch-tagging user interface

	- [ ] TBD: auto-tagging user interface

1. tagging

	- [ ] Tag of each picture will be kept in a separated database.

	- [ ] A picture could have multiple tags.

	- [ ] Tag can be added to a picture; tag can be deleted from a picture. 

	- [ ] Chinese is allowed for tag.

	- [ ] Batch-tagging is possible for folders.

	- [ ] Auto-tagging is possible based on face recognition technology.

	- [ ] Auto-tagging is possible based on other machine learning technology.

