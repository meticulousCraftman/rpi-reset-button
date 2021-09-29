from gpiozero import Button
from signal import pause
from subprocess import check_call
from gpiozero import PWMLED

button = Button(4, hold_time=4)
led = PWMLED(3)
led.on()
long_press_triggered = False

def single_press():
  global long_press_triggered
  if not long_press_triggered:
    print("Removing existing WiFi credentials")
    # Remove credentials for the current WiFi network
    check_call(["wpa_cli", "remove_network" , "0"])
    check_call(["wpa_cli", "save_config"])
    check_call(["sudo", "shutdown", "-r", "0"])
  
  # Reset long_press_trigerred variable
  long_press_triggered = False


def long_press():
  global long_press_triggered
  # Try connecting to a hotspot with the creds (Qube, 12345678)
  led.blink(on_time=1, off_time=1, fade_in_time=1, fade_out_time=1)
  print("Trying to connect to (Qube, 12345678)")
  # Unblock WiFi
  check_call(["sudo", "rfkill", "unblock", "wlan"])
  # Stop webthings-gateway service, otherwise it would create a hotspot 
  check_call(["sudo", "systemctl", "stop", "webthings-gateway.service"])
  # Copy the new wpa_supplicant file
  check_call(["sudo", "cp", "./wpa_supplicant.conf", "/etc/wpa_supplicant/wpa_supplicant.conf"])
  # reconfigure wpa_cli to connect to new network
  check_call(["sudo", "wpa_cli", "-i", "wlan0", "reconfigure"])
  print("Reconfigured WiFi network")
  long_press_triggered = True


button.when_released = single_press
button.when_held = long_press

pause()

