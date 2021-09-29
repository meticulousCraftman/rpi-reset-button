sudo apt update

echo "Installing dependency"
sudo apt install python3-gpiozero

echo "Copying service file for running the script at startup"
sudo cp reset-button.service /etc/systemd/system/
sudo systemctl enable reset-button.service
sudo systemctl start reset-button.service
