#!/usr/bin/env python

from cStringIO import StringIO
import re


vhost_start = re.compile(r'<VirtualHost\s+(.*?)>')
vhost_end   = re.compile(r'</VirtualHost')
docroot_re = re.compile(r'(DocumentRoot\s+)(\S+)')

def replace_docroot(conf_string,chost,new_docroot):
    conf_file = StringIO(conf_string)
    in_vhost = False
    for line in conf_file:
        vhost_start_match = vhost_start.search(line)
        if vhost_start_match:
            curr_host = vhost_start_match.groups()[0]
            in_vhost = True
        if in_vhost and (curr_host == vhost):
            doc_match = docroot_re.search(line)
            if doc_match:
                sub_line = docroot_re.sub(r'\1%s' % new_docroot,line)
                line = sub_line
        vhosts_end_match = vhost_end.search(line)
        if vhosts_end_match:
            in_vhost = False
        yield line


if __name__ == '__main__':
    import sys
    conf_file = sys.argv[1]
    vhost = sys.argv[2]
    docroot = sys.argv[3]
    conf_string = open(conf_file).read()
    for line in replace_docroot(conf_string,vhost,docroot):
        print line,


