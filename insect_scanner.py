from time import sleep
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import datetime

# to start program every x minutes: 
    # "crontab -e"
    # "*/15 * * * * /usr/bin/python3 /home/gruenspecht/workspace/insect_scanner.py" --> every 15min

# Broadcom Mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

picam2 = Picamera2()

config = picam2.create_still_configuration()
picam2.configure(config)

GPIO.output(21, GPIO.HIGH)
# active time of uv-leds:
sleep(300)
picam2.start()
# activating the white led and deactivating the uv-led:
GPIO.output(21, GPIO.LOW)
GPIO.output(16, GPIO.HIGH)
sleep(5)
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
picam2.capture_file(f"/home/gruenspecht/Pictures/insectscanner/img{timestamp}.jpg")
print(f"Picture captured: img{timestamp}")
picam2.stop()
GPIO.output(16, GPIO.LOW)