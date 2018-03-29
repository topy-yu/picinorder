#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import time
import os
import hashlib
import shutil

import filetype
import exifread

def md5sum(fname):
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:
            fh.seek(0)
            
    m = hashlib.md5()
    if isinstance(fname, basestring) \
            and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    elif fname.__class__.__name__ in ["StringIO", "StringO"] \
            or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()

class picinorder:

  def __init__(self, source="", target=""):
  
    self.source_path = source
    self.target_path = target
    
    self.create_logger()
    
  def check_precondition(self):
  
    if not self.source_path or not self.target_path:
      self.logger.error("Both source path and target path should be valid. ")
      return False
  
    if os.path.abspath(self.source_path).startswith(os.path.abspath(self.target_path)) or \
        os.path.abspath(self.target_path).startswith(os.path.abspath(self.source_path)):
      self.logger.error("Source path and target path should not include each other. ")
      return False
      
    return True
    
  def copy_files(self):
  
    if not self.check_precondition():
      return
      
    self.logger.info("Start to walk through %s..."%self.source_path)
    for dirpath, dirnames, filenames in os.walk(self.source_path):
      for file in filenames:
        try:
          self.handle_file(os.path.join(dirpath, file))
        except Exception, e:
          self.logger.error(str(e))
    self.logger.info("Walked through %s."%self.source_path)
  
  def copy_file(self, source_file_path, target_file_path):
    
    if not os.path.exists(os.path.dirname(target_file_path)):
      os.makedirs(os.path.dirname(target_file_path))
    
    if not os.path.exists(target_file_path):
      shutil.copy(source_file_path, target_file_path)
      self.logger.debug("copy %s to %s. "%(source_file_path, target_file_path))
    elif md5sum(source_file_path) == md5sum(target_file_path):
      self.logger.debug("skip %s, as it's same as %s. "%(source_file_path, target_file_path))
    else:
      self.logger.warning("cannot copy %s, as a different file %s exists. "%(source_file_path, target_file_path))
  
  def handle_other_file(self, file_path):
  
    relative_path = os.path.relpath(file_path, self.source_path)
    relative_path = os.path.join("other", relative_path)
    target_file_path = os.path.join(self.target_path, relative_path)
    
    self.copy_file(file_path, target_file_path)
    
  def get_new_name(self, file_path):
    
    return os.path.basename(file_path)
    
  def handle_image_file_with_data(self, file_path, data_split):
  
    YYYY = data_split[0]
    MM = data_split[1]
    DD = data_split[2]
    HH = data_split[3]
    mm = data_split[4]
    SS = data_split[5]
    
    target_file_path = os.path.join(self.target_path, "image")
    target_file_path = os.path.join(target_file_path, YYYY)
    target_file_path = os.path.join(target_file_path, MM)
    target_file_path = os.path.join(target_file_path, DD)
    target_file_path = os.path.join(target_file_path, self.get_new_name(file_path))
    
    self.copy_file(file_path, target_file_path)
  
  def handle_image_file_without_data(self, file_path):
  
    relative_path = os.path.relpath(file_path, self.source_path)
    relative_path = os.path.join("image", relative_path)
    target_file_path = os.path.join(self.target_path, relative_path)
    
    self.copy_file(file_path, target_file_path)
    
  def handle_image_file(self, file_path):
  
    fd = open(file_path, 'rb')
    data = exifread.process_file( fd )
    
    if data.has_key('EXIF DateTimeOriginal'):
      #DateTimeOriginal exists
      data_split = str(data['EXIF DateTimeOriginal']).replace(':', ' ').split()
      if data_split[0] != "0000":
        #DateTimeOriginal is valid
        self.handle_image_file_with_data(file_path, data_split)
      else:
        #DateTimeOriginal is not valid
        self.handle_image_file_without_data(file_path)
    else:
      #DateTimeOriginal not exists
      self.handle_image_file_without_data(file_path)

  def handle_file(self, file_path):
  
    self.logger.debug("handle_file %s"%file_path)
    file_ext = filetype.guess_extension(file_path)
    
    if file_ext is None:
      self.handle_other_file(file_path)
      return
    
    if file_ext == "jpg":
      self.handle_image_file(file_path)
      return
    
    self.handle_other_file(file_path)
      
  def set_logging_level(self, level):
  
    self.logger.setLevel(level)
    
  def create_logger(self):
  
    #logging.basicConfig()
  
    self.logger = logging.getLogger("Picinorder")
    self.logger.setLevel(logging.DEBUG)
    
    if not os.path.exists("log"):
      os.mkdir("log")
    log_file = os.path.join("log", "Picinorder_" + time.strftime('%Y%m%d%H%M%S') + ".log")
    fh_debug = logging.FileHandler(log_file)
    fh_debug.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh_debug.setFormatter(formatter)
    
    self.logger.addHandler(fh_debug)
    
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    
    self.logger.addHandler(sh)
    
  def test(self):
  
    self.logger.info("message")
    self.logger.debug("debug")
    
  def generate_report(self, path='.'):

    md5_dict = dict()

    for dirpath, dirnames, filenames in os.walk(path):
      for name in filenames:
        md5_result = md5sum(os.path.join(dirpath, name))
        self.logger.debug('%s '%(md5_result)+os.path.join(dirpath, name))
        if not md5_dict.has_key(md5_result):
          md5_dict[md5_result] = [os.path.join(dirpath, name)]
        else:
          md5_dict[md5_result].append(os.path.join(dirpath, name))
          self.logger.warning('Same file detected %d time(s): '%len(md5_dict[md5_result]))
          for i in md5_dict[md5_result]:
            self.logger.debug("  " + i)

  def generate_tree_helper(self, fpath, level=0, file_list=None):
  
    if file_list == None:
      file_list = []

    files = os.listdir(fpath)
    for file in files:
      file_path = os.path.join(fpath, file)
      if os.path.isdir(file_path):
        self.logger.debug("|-" + "-"*level + file)
        self.generate_tree_helper(file_path, level+1)
      else:
        self.logger.debug("|-" + "-"*level + file)
        file_list.append(file)
    return file_list
    
  def generate_tree(self, path='.'):
  
    self.generate_tree_helper(path)
  

    
