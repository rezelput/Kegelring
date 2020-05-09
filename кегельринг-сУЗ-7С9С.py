import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  b = None
  x = None
  y = None

  def execMain(self):

    
    brick.motor("M3").setPower(100)
    brick.motor("M4").setPower(100)
    
    while True:
      while not (brick.sensor("A1").read() > 30):
        script.wait(10)
      
      self.y = brick.sensor("A1").read()
      if (self.y < 40):
        while not (brick.sensor("D1").read() < 35):
          script.wait(10)
        
        self.x = brick.encoder("E3").read()
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M3").setPower(-(100))
        brick.motor("M4").setPower(-(100))
        
        while not (brick.encoder("E3").read() > int(self.b)):
          script.wait(10)
        
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        
        brick.motor("M4").setPower(100)
        
        script.wait(500)
        
      else:
        while not (brick.sensor("D1").read() < 150):
          script.wait(10)
        
        brick.motor("M3").brake()
        brick.motor("M4").brake()
        
        brick.motor("M3").setPower(25)
        

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
