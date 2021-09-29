# Reset Button
Allows you to reset the gateway when the reset button is pressed.
This code is written in Python 3. This is executed as a daemon process using systemd. 

## Hardware Connection
  - LED - GPIO 3
  - Button - GPIO 4


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

## Modes
  - Short Press - Deletes all WiFi credentials, restarts the device. Then wait for the device to host a hotspot.
  - Long Press (5 seconds or more) - Disconnects from existing WiFi network, tries to connect to (Qube, 12345678). Host a hotspot using your mobile phone, gateway will automatically connect to it in just a few seconds. Note that, it also stops the webthings-gateway service, to prevent it from taking over and hosting a hotspot. So this should be used only for pure debugging! 
