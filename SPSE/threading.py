#!/usr/bin/env python

import threading
import Queue
import time


class Worker_thread(threading.Thread):

  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue

  def run(self):
    print "In WorkerThread"
    while True:
      counter = self.queue.get()
      with open("file.txt","w") as file:
        file.write(counter)
        time.sleep(counter)
        print "Finished Writing"
        file.close()
        self.queue.task_done()

queue = Queue.Queue()

for i in range(10):
  print "Creating WorkerThread: %d"%i
  worker = Worker_thread(queue)
  worker.setDaemon(True)
  worker.start()
  print "WorkerThread %d Created!"%i

for j in range(10):
  queue.put(j)

queue.join()

print "All tasks Done"
