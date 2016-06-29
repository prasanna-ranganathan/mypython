#!/usr/bin/env python

import os,sys

def get_mount_point(pathname):
    """ Get the Mount point of th efilesystem containg pathname"""
    pathname = os.path.normcase(os.path.realpath(pathname))
    parent_device = path_device = os.stat(pathname).st_dev
    while parent_device == path_device:
        mount_point = pathname
        pathname = os.path.dirname(pathname)
        if pathname == mount_point:
            break
        parent_device = os.stat(pathname).st_dev
    return mount_point


def get_mounted_device(pathname):
    """Get the device mounted at pathnaem"""
    try:
        with open("/proc/mounts","r") as ifp:
            for line in ifp:
                feilds = line.rstrip("\n").split()
                if feilds[1] == pathname:
                        return feilds[0]
    except EnvironmentError:
        pass
    return None

def get_fs_freespace(pathname):
    """Get freespace of the filesystem containg pathname"""
    stat = os.statvfs(pathname)
    return stat.f_bfree * stat.f_bsize

def usage():
    print "Usage: ./DiskUsage.py <pathname>"

def main(pathname):
    try:
        print get_mount_point(pathname)
        print get_mounted_device(pathname)
        print "Free: ",get_fs_freespace(pathname)
    except:
        Usage()
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1])
