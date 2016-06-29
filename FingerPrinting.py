#!/usr/bin/env python

import platform

"""
FingerPrinting the Following Operating System:
*MAC OS X
*LINUX
*UNIX
*WINDOWS
"""

class OpSystype(object):
  """DeterMinies OS Type using platform module"""
  def __getattr__(self,attr):
    if attr == "osx":
      return "OSX"
    elif attr == "rhel":
      

