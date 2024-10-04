import os, qi, sys
from threading import Timer
from naoqi import ALProxy
import time

robot = None

def user_detected():
   return True

def start_intro(new_robot):
   
   global robot 
   robot = new_robot
   while (True):
      if(user_detected()):
         break
   question = 'Hello. What is your name?'
   robot.say(question)
   username = raw_input()
   memProxy = ALProxy("ALMemory",os.getenv('PEPPER_IP'),9559)
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
   options = {'Yes' : ['Yes', 'yes', '0'],
              'No' : ['No', 'no', '1']}
   answered = False
   while not answered:
	   question ="Would you like to play a game with me?"
	   robot.say(question)
	   option, answered = stt(options, question)
   if option in options['No']:
      robot.say('Very well. I shall go to sleep then.')
      exit()
   #TODO from here onwards the voice becomes that of a presenter
   robot.say('Wonderful! Let us play a special game then.')
   time.sleep(1)
   robot.say('Let us play, Human-Robot Violent Interaction!')
   characters = {'Naruto' : ['Naruto', 'naruto', '0'],  
                         'Goku' : ['Goku', 'goku', '1'], 
                         'Goldrake' : ['Goldrake', 'goldrake', '2'], 
                         'Terminator' : ['Terminator', 'terminator', '3']}
   answered = False
   while not answered:
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
	   character, answered = stt(characters, question, t = 20)
   robot.say('You have chosen ' + character)
   answered = False
   while not answered:
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
	   opponent, answered = stt(characters, question, t = 20)
   robot.say(character + ' against ' + opponent)
   robot.say('Let the battle begin!')
   return character, opponent


def stt(vocabulary, question, t = 10, is_robot = False):
   global robot
   change_eyes_color()
   answered = False
   if is_robot == False:
      query = raw_input()
      option = 'Invalid'
      if query!="": # valid answer
         for vocab in vocabulary:
            for entry in vocabulary[vocab]:
               if entry == query:
                     option = vocab
                     answered = True
                     break
               if answered == True:
                     break
      if option == 'Invalid':
         robot.say('I do not understand')
      return option, answered
   
   
   
   vocab = []
   for v in vocabulary.keys():
      vocab += vocabulary[v]


   option = robot.asr(vocab, t)
   if option == None or option == 'none':
      option = 'Invalid'
   else:
      answered = True
   '''
   asr_proxy = ALProxy("ALSpeechRecognition", os.getenv('PEPPER_IP'),9559)
   asr_proxy.setLanguage("English")
   asr_proxy.setVocabulary(["yes","no"], False)
   asr_proxy.subscribe("TEST ASR")
   '''
   #option = asr_proxy.recognize()
   #'''
   #'''
   
   if option == 'Invalid':
      robot.say('I do not understand')
   return option, answered

def change_eyes_color():
   ledProxy = ALProxy('ALLeds',os.getenv('PEPPER_IP'),9559)
   red = 255
   green = 0
   blue = 0
   ledProxy.fadeRGB("AllLeds", red*256+ green*256, 0.5)