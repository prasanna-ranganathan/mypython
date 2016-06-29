import re

def Main():
    line = "I think i understand Regular Expression"
    matchResult = re.match(r'think',line,re.M|re.I)
    if matchResult:
        print 'Match Found:' + matchResult.group()
    else:
        print "Match Not Found"

    searchResult = re.search(r'think',line,re.M|re.I)
    if searchResult:
        print "search found " + searchResult.group()
    else:
        print "Oops!!"

if __name__ == '__main__':
    Main()

