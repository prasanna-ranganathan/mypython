#!/usr/bin/env python

import string

s = 'The quick brown fox jumped over the lazy dog.'
print s
print string.capwords(s)

#Another method#

print ' '.join(text.title() for text in s.split())
