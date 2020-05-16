import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793
  x = None
  y = None

  def execMain(self):

    
    brick.motor("M4").setPower(-(50))
    
    brick.motor("M3").setPower(50)
    
    while not (brick.sensor("A2").read() < 20):
      script.wait(10)
    
    brick.encoder("E3").reset()
    
    brick.motor("M3").setPower(40)
    brick.motor("M4").setPower(40)
    
    while True:
      self.x = brick.sensor("A1").read()
      self.y = brick.sensor("A2").read()
      if (self.x < 50):
        brick.motor("M3").setPower(40)
        brick.motor("M4").setPower(40)
        
      else:
        while not (brick.sensor("A1").read() < 45):
          script.wait(10)
        
        brick.motor("M3").brake()
        brick.motor("M4").brake()
        
        brick.motor("M3").setPower(-(50))
        brick.motor("M4").setPower(-(50))
        
        while not (brick.encoder("E3").read() < 0):
          script.wait(10)
        

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
