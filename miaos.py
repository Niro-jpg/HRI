import os, qi, sys
from threading import Timer
from naoqi import ALProxy

def start_intro():


   question = 'Hello. What is your name?'
   robot.say(question)
   username = raw_input()
   memProxy = ALProxy("ALMemory","localhost",9559)
   try:
      user = memProxy.getData(username)
   except:
      user = ''
   if user == '':
      question = 'A new user! Hello {0}'.format(username)
      robot.say(question)
      memProxy.insertData(username, 'registered')
   else:
      question = 'Welcome Back {0}!'.format(username)
      robot.say(question)
   time.sleep(1)   
   question ="Would you like to play a game with me?"
   robot.say(question)
   options = ['yes', 'no']
   option = stt(options, question)
   if option == 1:
      robot.say('Very well. I shall go to sleep then.')
      exit()
   #TODO from here onwards the voice becomes that of a presenter
   robot.say('Wonderful! Let us play a special game then.')
   time.sleep(1)
   robot.say('Let us play, Human-Robot Violent Interaction!')
   question = 'Choose your character :'
   robot.say(question)
   time.sleep(1)
   robot.say('Character 1')
   time.sleep(3)
   robot.say('Character 2')
   time.sleep(3)
   robot.say('Character 3')
   characters = ['1', '2', '3']
   option = stt(characters, question, t = 20)
   character = characters[option]
   robot.say('You have chosen ' + character)
   question = 'Very well! Which character shall I be then?'
   robot.say(question)
   time.sleep(1)
   robot.say('Character 1')
   time.sleep(3)
   robot.say('Character 2')
   time.sleep(3)
   robot.say('Character 3')
   opponents = ['1', '2', '3']
   option = stt(opponents, question, t = 20)
   opponent = opponents[option]
   #TODO Say opponent-specific start phrase
   robot.say('Let the battle begin!')
   exit()

def stt(vocabulary, question, t = 10):
   #timer = Timer(t, timeout, args = (question, ))
   #timer.start()
   query = raw_input()
   # answer = robot.asr(vocabulary,timeout)
   #timer.cancel()
   option = 'Invalid'
   if query!="": # valid answer
      for i in range(len(vocabulary)):
          if vocabulary[i] in query:
              option = i
              robot.say('You picked option ' + str(i))
              break
   return option

def timeout(question):
   robot.say('You have not answered. Would you like me to repeat the question?')
   repeat = raw_input()
   if repeat == 'yes':
      robot.say(question)
   else:
      sys.exit()
      
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
   start_intro()
   end()