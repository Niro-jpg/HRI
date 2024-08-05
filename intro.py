import os, qi, sys
from threading import Timer
from naoqi import ALProxy
import time

robot = None

def start_intro(new_robot):
   
   global robot 
   robot = new_robot

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
   time.sleep(0.5)   
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
   time.sleep(0.5)
   robot.say('Naruto')
   time.sleep(0.5)
   robot.say('Goku')
   time.sleep(0.5)
   robot.say('Goldrake')
   time.sleep(0.5)
   robot.say('Terminator')
   characters = ['Naruto', 'Goku', 'Goldrake', 'Terminator']
   option_c = stt(characters, question, t = 20)
   character = characters[option_c]
   robot.say('You have chosen ' + character)
   question = 'Very well! Which character shall I be then?'
   robot.say(question)
   time.sleep(0.5)
   robot.say('Naruto')
   time.sleep(0.5)
   robot.say('Goku')
   time.sleep(0.5)
   robot.say('Goldrake')
   time.sleep(0.5)
   robot.say('Terminator')
   opponents = ['Naruto', 'Goku', 'Goldrake', 'Terminator']
   option_o = stt(opponents, question, t = 20)
   opponent = opponents[option_o]
   #TODO Say opponent-specific start phrase
   robot.say('Let the battle begin!')
   return option_c, option_o


def stt(vocabulary, question, t = 10):
   global robot
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
              #robot.say('You picked option ' + str(i))
              break
   return option