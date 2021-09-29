# Reset Button
Allows you to reset the gateway when the reset button is pressed.
This code is written in Python 3. This is executed as a daemon process using systemd. 

## Hardware Connection
LED - GPIO 3
Button - GPIO 4
On Raspberry Pi Zero W

## Setup
This will do everything for you.
```
./setup.sh
```

## Logs
```
sudo journalctl -u reset-button.service -f
```
