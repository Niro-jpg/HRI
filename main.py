
import os, qi, sys
from threading import Timer
from naoqi import ALProxy
from intro import start_intro
from Battle import Battle


def stt(vocabulary, question, t = 10):
   global robot
   query = raw_input()
   option = 'Invalid'
   if query!="": # valid answer
      for i in range(len(vocabulary)):
          if vocabulary[i] in query:
              option = i
              break
   return option

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
   pc, oc = start_intro(robot)
   while True:
      battle = Battle(pepper = True, robot = robot, ally_monster_index = pc, enemy_monster_index = oc)
      battle.start_battle()
      question = 'Hello. What is your name?'
      question = 'Great battle! Would you like to play again?'
      robot.say(question)
      options = ['yes', 'no']
      option = stt(options, question)
      if options[option] == 'no':
         break