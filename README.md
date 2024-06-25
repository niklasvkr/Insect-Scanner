# Insect-Scanner

## Instructions

### Connecting the Gate Cables

Connect the gate cables to the Raspberry Pi pins as follows:
- Purple cable: GPIO 21
- Red cable: GPIO 16

![Raspberry Pi Zero W Pinout](Raspberry-pi3-pinout.jpg)

### Setting up a Crontab Job

Open the crontab in the terminal:

```sh
crontab -e
```

Then add this line at the end of the job list:

```sh
*/15 * * * * /usr/bin/python3 /home/gruenspecht/workspace/insect_scanner.py
```
This executes the insect_scanner.py file every 15 minutes
