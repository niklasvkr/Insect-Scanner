# Insect-Scanner

## Instructions

### Connecting the Gate Cables

Connect the gate cables to the Raspberry Pi pins as follows:
- Purple cable (UV-LEDs): GPIO 21
- Red cable (White-LEDs): GPIO 16

![Raspberry Pi Zero W Pinout](Raspberry-pi3-pinout.jpg)

### Setting up a Crontab Job

Open the crontab in the terminal:

```sh
crontab -e
```

Then add this line at the end of the job list:

```sh
*/15 * * * * /usr/bin/python3 /path/to/insect_scanner.py
```
This executes the insect_scanner.py file every 15 minutes

### Connecting the USB-Cables to the Powerbank

Connect the USB cables of the Raspberry and LEDs to the two USB 2.0 ports (black). This is necessary to prevent potential differences that could cause the LEDs to malfunction.
