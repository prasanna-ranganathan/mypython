#!/usr/bin/env python
#source link: http://stackoverflow.com/questions/4260116/find-size-and-free-space-of-the-filesystem-containing-a-given-file?answertab=oldest#tab-top"
import os
def get_mount_point(pathname):
    "get the mount point of the filesystem"
    pathname = os.path.normcase(os.path.realpath(pathname))
    parent_device = path_device = os.stat(pathname).st_dev
    while parent_device == path_device:
        print "parent_device: ",parent_device,"path_device",path_device
        mount_point = pathname
        print "Debug 1: ", mount_point
        pathname = os.path.dirname(pathname)
        print "Debug 2:  ",pathname
        if pathname == mount_point:
            break
        parent_device  = os.stat(pathname).st_dev
        print "parent stat: ",parent_device," path stat: ",path_device
    return mount_point

if __name__ == '__main__':
    print get_mount_point(raw_input())
