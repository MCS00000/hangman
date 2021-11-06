import time


def countdown(t):
    while t > -1:
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print('Nākamā partija sāksies pēc: ' + timer, end ="\r")
      time.sleep(1)
      t -= 1 