import time
import os, qi
from naoqi import ALProxy
import almath

def move_head():
   pip = os.getenv('PEPPER_IP')
   pport = 9559
   connection_url = "tcp://" + pip + ":" + str(pport)
   app = qi.Application(["App", "--qi-url=" + connection_url ])
   app.start()
   session = app.session
   memory_service = app.session.service("ALMemory")
   motion_service = session.service("ALMotion")
   jointNames = ["HeadYaw", "HeadPitch"]
   angles = [1.6, -0.2]
   times = [5.0, 5.0]
   isAbsolute = True
   motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)
   rp_service = session.service("ALRobotPosture")
   initial_posture = "Stand"
   speed = 0.7
   rp_service.goToPosture(initial_posture, speed)

def move_arm():
    moveProxy = ALProxy("ALMotion","localhost",9559)
    jointNames = ["RElbowRoll", "RElbowYaw", 'RHand', 'RShoulderPitch', 'RShoulderRoll', 'RWristYaw']
    angles = [75.5*almath.TO_RAD, 106.8*almath.TO_RAD, 0.98, 88.0*almath.TO_RAD, -88.9*almath.TO_RAD, 57.6*almath.TO_RAD]
    times = len(angles) * [3.0]
    isAbsolute = True
    moveProxy.angleInterpolation(jointNames, angles, times, isAbsolute)
    angles2 = [5.9*almath.TO_RAD, 97.0*almath.TO_RAD, 0.98, 8.5*almath.TO_RAD, -15.5*almath.TO_RAD, -9.6*almath.TO_RAD]
    times2 = len(angles) * [2.0]
    moveProxy.angleInterpolation(jointNames, angles2, times2, isAbsolute)
    time.sleep(0.5)
    initial_posture = "Stand"
    postureProxy = ALProxy('ALRobotPosture', 'localhost', 9559)
    speed = 0.7 
    postureProxy.goToPosture(initial_posture,  speed)


def default_an():
    moveProxy = ALProxy("ALMotion","localhost",9559)
    jointNames = ['RElbowRoll', 'RElbowYaw', 'RHand', 'RShoulderPitch', 'RShoulderRoll', 'RWristYaw']
    isAbsolute = True
    angles = [5.9*almath.TO_RAD, 97.0*almath.TO_RAD, 0.02, 8.5*almath.TO_RAD, -15.5*almath.TO_RAD, -70.3*almath.TO_RAD] 
    times = len(angles) * [2.0]
    moveProxy.angleInterpolation(jointNames, angles, times, isAbsolute)
    time.sleep(0.5)
    initial_posture = "Stand"
    postureProxy = ALProxy('ALRobotPosture', 'localhost', 9559)
    speed = 0.7 
    postureProxy.goToPosture(initial_posture,  speed)

def arms_up():
    moveProxy = ALProxy("ALMotion","localhost",9559)
    jointNames = ["RElbowRoll", "RElbowYaw", 'RHand', 'RShoulderPitch', 'RShoulderRoll', 'RWristYaw', "LElbowRoll", "LElbowYaw", 'LHand', 'LShoulderPitch', 'LShoulderRoll', 'LWristYaw']
    angles = [5.9*almath.TO_RAD, 99.2*almath.TO_RAD, 0.98, -82.1*almath.TO_RAD, -6.0*almath.TO_RAD, -94.7*almath.TO_RAD, -5.9*almath.TO_RAD, -99.2*almath.TO_RAD, 0.98, -82.1*almath.TO_RAD, -6.0*almath.TO_RAD, 94.7*almath.TO_RAD]
    times = len(angles) * [3.0]
    isAbsolute = True
    moveProxy.angleInterpolation(jointNames, angles, times, isAbsolute)
    angles2 = [5.9*almath.TO_RAD, 99.2*almath.TO_RAD, 0.98, -119.5*almath.TO_RAD, -6.0*almath.TO_RAD, -94.7*almath.TO_RAD, -5.9*almath.TO_RAD, -99.2*almath.TO_RAD, 0.98, -119.5*almath.TO_RAD, -6.0*almath.TO_RAD, 94.7*almath.TO_RAD]
    times2 = len(angles) * [2.0]
    moveProxy.angleInterpolation(jointNames, angles2, times2, isAbsolute)
    angles3 = [5.9*almath.TO_RAD, 99.2*almath.TO_RAD, 0.98, 31.9*almath.TO_RAD, -6.0*almath.TO_RAD, -94.7*almath.TO_RAD, -5.9*almath.TO_RAD, -99.2*almath.TO_RAD, 0.98, 31.9*almath.TO_RAD, -6.0*almath.TO_RAD, 94.7*almath.TO_RAD]
    times3 = len(angles) * [2.0]
    moveProxy.angleInterpolation(jointNames, angles3, times3, isAbsolute)
    initial_posture = "Stand"
    postureProxy = ALProxy('ALRobotPosture', 'localhost', 9559)
    speed = 0.7 
    postureProxy.goToPosture(initial_posture,  speed)

if __name__ == "__main__":
    #move_head()
    #move_arm()
    #default_an()
    arms_up()