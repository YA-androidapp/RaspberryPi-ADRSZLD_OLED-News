# RaspberryPi-ADRSZLD_OLED-News

---

```bash
sudo apt update -y && sudo apt upgrade -y

sudo apt install fonts-takao
sudo apt install git
sudo apt install python3-pip

python3 -m pip install adafruit-circuitpython-ssd1306
python3 -m pip install adafruit-blinka
python3 -m pip install feedparser
python3 -m pip install pillow

sudo raspi-config
# 3 Interface Options    Configure connections to peripherals
# I4 SPI           Enable/disable automatic loading of SPI kernel module

git clone https://github.com/bit-trade-one/RasPi-Zero-One-Series.git
cd RasPi-Zero-One-Series/3rd/ADRSZLD_OLED_Display/RaspberryPi_OS_Bullseye
python3 adrszLD_test.py
```

---

Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
