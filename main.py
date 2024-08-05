
import os, qi, sys
from threading import Timer
from naoqi import ALProxy
from intro import start_intro
from Battle import Battle

if __name__=="__main__":
   pdir = os.getenv('PEPPER_TOOLS_HOME')
   sys.path.append(pdir+ '/cmd_server')
   import pepper_cmd
   from pepper_cmd import *
   if robot == None:
        robot = PepperRobot()
        robot.connect()
   robot.begin()

   pip = os.getenv('PEPPER_IP')
   pport = 9559
   connection_url = "tcp://" + pip + ":" + str(pport)
   start_intro(robot)
   while True:
        
     battle = Battle(pepper = True, robot = robot)
     battle.start_battle()
     break
   end()