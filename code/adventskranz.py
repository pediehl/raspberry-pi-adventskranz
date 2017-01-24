#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import datetime

GPIO.setup(6, GPIO.OUT) #erster Advent
GPIO.setup(13, GPIO.OUT) #zweiter Advent
GPIO.setup(19, GPIO.OUT) #dritter Advent
GPIO.setup(26, GPIO.OUT) #vierter Advent

#aktuelle Zeit ermitteln
now = datetime.datetime.now()
#Jahr aus der aktuellen Zeitangabe ermitteln
jahr = now.year

#Wochentag von Weihnachten ermitteln & Advent-Sonntage berechnen
weihnachten = datetime.datetime(jahr, 12, 24, 0, 0, 0)
wochentag = weihnachten.weekday()
vierter_advent = weihnachten - datetime.timedelta(wochentag + 1)
dritter_advent = weihnachten - datetime.timedelta(wochentag + 8)
zweiter_advent = weihnachten - datetime.timedelta(wochentag + 15)
erster_advent = weihnachten - datetime.timedelta(wochentag + 22)

#LEDS aktivieren je nach Datum / Advent-Sonntag
if(now <= weihnachten):
    if(now >= erster_advent):
        GPIO.output(6, GPIO.HIGH)
    if(now >= zweiter_advent):
        GPIO.output(13, GPIO.HIGH)
    if(now >= dritter_advent):
        GPIO.output(19, GPIO.HIGH)
    if(now >= vierter_advent):
        GPIO.output(26, GPIO.HIGH)

#Ausgabe der Uebersicht auf dem Bildschirm
print now.strftime('Die Advent-Sonntage im Jahr %Y') 
print erster_advent.strftime('1. Advent am %d.%m.%Y')
print zweiter_advent.strftime('2. Advent am %d.%m.%Y')
print dritter_advent.strftime('3. Advent am %d.%m.%Y')
print vierter_advent.strftime('4. Advent am %d.%m.%Y')
