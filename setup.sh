sudo ./track.sh
sudo apt update
sudo apt install -y python3-pip firefox
sudo pip3 install selenium
sudo mv geckodriver /usr/local/bin/geckodriver
sudo chmod 400 a.pem
sudo nohup python3 code.py &
