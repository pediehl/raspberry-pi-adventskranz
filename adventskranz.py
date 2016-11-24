from gpiozero import LED
import datetime

led_erster_advent = LED(6)
led_zweiter_advent = LED(13)
led_dritter_advent = LED(19)
led_vierter_advent = LED(26)

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
        led_erster_advent.on()
    if(now >= zweiter_advent):
        led_zweiter_advent.on()
    if(now >= dritter_advent):
        led_dritter_advent.on()
    if(now >= vierter_advent):
        led_vierter_advent.on()

#Ausgabe der Uebersicht auf dem Bildschirm
print now.strftime('Die Advent-Sonntage im Jahr %Y') 
print erster_advent.strftime('1. Advent am %d.%m.%Y')
print zweiter_advent.strftime('2. Advent am %d.%m.%Y')
print dritter_advent.strftime('3. Advent am %d.%m.%Y')
print vierter_advent.strftime('4. Advent am %d.%m.%Y')
