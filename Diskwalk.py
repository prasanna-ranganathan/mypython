#!/usr/bin/env python

import os

class diskwalk(object):
  """API for getting directory  walking collections"""
  def __init__(self,path):
    self.path = path


  def enumeratepaths(self):
    """Returns the path to all the files in a directory as a list"""
    path_collections = []
    for dirpath,dirnames,filenames in os.walk(self.path):
      for file in filenames:
        fullpath = os.path.join(dirpath,file)
      path_collections.append(fullpath)
    return path_collections

  def enumeratedir(self):
    """Returns the dirs in a directory as a list"""
    dir_collections = []
    for dirpath,dirnames,filenames in os.walk(self.path):
      for dir in dirnames:
        dir_collections.append(dir)
    return dir_collections

  def enumerateFiles(self):
    """Returns the files in a directory as a list"""
    File_collections = []
    for dirpath,dirnames,filenames in os.walk(self.path):
      for file in filenames:
        File_collections.append(file)
    return File_collections

if __name__ == '__main__':
  import sys
  try:
    diskwalk(sys.argv[1])
  except:
    print "Usage: diskwalk <path>"


