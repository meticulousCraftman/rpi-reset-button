sudo apt update
sudo apt install python3-gpiozero
sudo cp reset-button.service /etc/systemd/system/
sudo systemctl enable reset-button.service
sudo systemctl start reset-button.service
