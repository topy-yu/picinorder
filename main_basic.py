#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

import picinorder

if __name__ ==  '__main__':

  source = "D:\\userdata\\l2yu\\Desktop\\tool\\Picinorder\\source"
  target = "D:\\userdata\\l2yu\\Desktop\\tool\\Picinorder\\target"
  
  pi = picinorder.picinorder(source, target)
  import logging
  pi.set_logging_level(logging.DEBUG)
  pi.copy_files()

  #pi.generate_report(source)
  #pi.generate_tree(source)
  
  print "Done!"
