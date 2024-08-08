import time
import os, qi
from naoqi import ALProxy
import almath

def damage(battle):
   moveProxy = ALProxy("ALMotion","localhost",9559)
   jointNames = ['RShoulderPitch', 'LShoulderPitch', "HeadYaw", "HeadPitch"]
   angles = [119.5*almath.TO_RAD, 119.5*almath.TO_RAD, 1.6, -0.2]
   times = len(angles) * [1.0]
   isAbsolute = True
   moveProxy.angleInterpolation(jointNames, angles, times, isAbsolute)
   initial_posture = "Stand"
   postureProxy = ALProxy('ALRobotPosture', 'localhost', 9559)
   speed = 0.7 
   postureProxy.goToPosture(initial_posture,  speed)

def rasengan(battle):
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


def default_an(battle):
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

def spiritball(battle):
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


def come_with_me_if_you_want_to_live(battle):

    moveProxy = ALProxy("ALMotion","localhost",9559)
    jointNames = ['RElbowRoll', 'RElbowYaw', 'RHand', 'RShoulderPitch', 'RShoulderRoll', 'RWristYaw']
    isAbsolute = True
    angles = [0.5*almath.TO_RAD, 70.5*almath.TO_RAD, 0.98, 36.8*almath.TO_RAD, -8.5*almath.TO_RAD, 104.5*almath.TO_RAD] 
    times = len(angles) * [2.0]
    moveProxy.angleInterpolation(jointNames, angles, times, isAbsolute)
    time.sleep(0.5)
    battle.robot_print('The opponent`s move confuses you')
    battle.robot_print('You are so confused to hit yourself!')
    time.sleep(0.5)
    initial_posture = "Stand"
    postureProxy = ALProxy('ALRobotPosture', 'localhost', 9559)
    speed = 0.7 
    postureProxy.goToPosture(initial_posture,  speed)


def space_thunder(battle):
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
    damage()


#if __name__ == "__main__":
    #damage()
    #rasengan()
    #default_an()
    #spiritball()
    #come_with_me_if_you_want_to_live()
    #space_thunder()