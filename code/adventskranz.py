#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import datetime

led_erster_advent = 6
led_zweiter_advent = 13
led_dritter_advent = 19
led_vierter_advent = 26

GPIO.setup(led_erster_advent, GPIO.OUT)
GPIO.setup(led_zweiter_advent, GPIO.OUT)
GPIO.setup(led_dritter_advent, GPIO.OUT)
GPIO.setup(led_vierter_advent, GPIO.OUT)

#aktuelle Zeit ermitteln
now = datetime.datetime.now()
#Jahr aus der aktuellen Zeitangabe ermitteln
jahr = now.year

#Wochentag von Weihnachten ermitteln & Advent-Sonntage berechnen
weihnachten = datetime.datetime(jahr, 12, 25, 0, 0, 0)
wochentag = weihnachten.weekday()
vierter_advent = weihnachten - datetime.timedelta(wochentag + 1)
dritter_advent = weihnachten - datetime.timedelta(wochentag + 8)
zweiter_advent = weihnachten - datetime.timedelta(wochentag + 15)
erster_advent = weihnachten - datetime.timedelta(wochentag + 22)

#LEDS aktivieren je nach Datum / Advent-Sonntag
if(now <= weihnachten):
    if(now >= erster_advent):
        GPIO.output(led_erster_advent, GPIO.HIGH)
    if(now >= zweiter_advent):
        GPIO.output(led_zweiter_advent, GPIO.HIGH)
    if(now >= dritter_advent):
        GPIO.output(led_dritter_advent, GPIO.HIGH)
    if(now >= vierter_advent):
        GPIO.output(led_vierter_advent, GPIO.HIGH)

#Ausgabe der Uebersicht auf dem Bildschirm
print now.strftime('Die Advent-Sonntage im Jahr %Y')
print erster_advent.strftime('1. Advent am %d.%m.%Y')
print zweiter_advent.strftime('2. Advent am %d.%m.%Y')
print dritter_advent.strftime('3. Advent am %d.%m.%Y')
print vierter_advent.strftime('4. Advent am %d.%m.%Y')
