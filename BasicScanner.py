import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
  try:
    connSkt = socket(AF_INET,SOC_STREAM)
    connSkt.connect((tgtHost,tgtPort))
    connSkt.send("hello\r\n")

    results = connSkt.recv(100)
    screenLock.acquire()
    print "[+] " + str(tgtPort) + "/tcp open"
  except:
    screenLock.acquire()
    print "[+] " + str(tgtPort) + "/tcp closed"
  finally:
    screenLock.release()
    connSkt.close()

def portScan(tgtHost,tgtPorts):
  try:
    tgtIP = gethostbyname(tgtHost)
  except:
    print"[+] cannot Resolve" + tgtHost + ": unknown host"
    return

  try:
    tgtName = gethostbyaddr(tgtIP)
    print "\n[+] Scan Results for: " + tgtName[0]
  except:
    print "\n[+] Scan Results for: " + tgtIP

  setDefaulttimeout(1)
  for tgtPort in tgtPorts:
    t = Thread(target=connScan,args=(trgtHost,int(tgtPort)))
    t.start()

def Main():
  parser = optparse.optionParse('usage %prog -H <target host> ' +\
            '-p <target Port>');
  parser.add_option('-H',dest='tgtHost',type='string',\
          help='specify trg host')
  parser.add_option('-P',dest='tgtPort',type='string',\
          help='specify target ports seperated by a comma')
  (optios,args) = parser.parse_args()
  if(options.tgtHost == None) | (options.tgtPort == None):
    print parser.usage
    exit(0)
  else:
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

  portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
  Main()
