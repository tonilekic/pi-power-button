#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

switchPin = 3

def wait_for_falling_edge(gpioNumber):
    while GPIO.input(gpioNumber):
        time.sleep(.01)

GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin, GPIO.IN)
wait_for_falling_edge(switchPin)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
