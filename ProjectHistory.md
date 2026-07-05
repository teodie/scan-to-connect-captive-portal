# Issue encountered

forgot how to connect to orange pi (ssh/putty)

cant login after openwrt installation because when pluging to isp router the orange pi one is not visible. issue with the ethernet port (eth0) is by default configured as
Wan.

Issue with connecting with the device since the orange pi one ip address is not visible.

Issue with changing the built-in ethernet to be Lan since I am using the webinterface

issue with the driver. I have read that it can be installed with custom build in openwrt firmware download

I dont know how to configure the ethernet port eth0 into Lan

I have re-download the image with the driver for RTl8153 driver (cheap one that I used on my piso wifi) and AX8817 driver (for future ugreen usb-to-ethernet driver)

I dont know what eth0 and eth1 means all I know is its name of physical port

I dont really understand network bridges

I Change the network file configuration to make as per the documentation for orange pi one on openwrt (https://openwrt.org/toh/xunlong/orange_pi_one followed below instruction)
Alternatively, in order to configure onboard ethernet to eth0 for LAN and USB adapter to eth1 for WAN (vi /etc/config/network):

Hindi ako maka connect sa orange pi using ssh. Turns out openWRT firewall block traffic from WAN Port which is "eth1" so to fix it I add firewall rule that allow traffic from WAN

Unable to manually run openNDS with openWRT. Even when enabled it was not running on reboot.

For the meantime I will be abandoning the openNDS with openWRT and will explore automated scraping with selenium and headless chromium.

First issue: I cant login to my orange pi one that I have used for scrapping for my piso wifi monitoring scrapping. I will try to update the shadow file and insert my password on the root

I got the code working with the assist of AI or improve google and stackoverflow. I can now change password. next would be the display and qrcode generating

Ordered the TFT display yesterday and waiting the part to arrived.

TFT ST7789 has been recieved and here are the issues I encountered so far:
- Unable to access orange pi terminal
I got an issue with the USB to TTL where when I open Putty and open serial comunication I see nothing on the terminal.
solution: I need to wait for couple of seconds then click enter to see the login text. sometimes needed to type something then enter when enter alone don't work.

- Trying to install packages with to ethernet cable
I am dumb and trying to install package orangepi.st7789 when there is no ethernet installed. I been copy pasting error code to AI and AI pointed out that it has no internet. Dumb Teodi is responsible.

- Installing the OrangePi.ST7789 took so long since the dependencies of the library on Numpy and Pillow which Unpacking and compiling is processor intensive for 512 RAM of orange pi one.

- Installation crushed since its running for 1hr
Unplugged and replugged try next approuch on downloading precompiled numpy and pillow package

## Issue:
The Board I unresponsive 
## Action Taken:
Can't access the terminal, tried multiple times. may be the previous installation damage the os or hardware on worst case scenario.
## Next Action
Will reflash os and tried again this time install pre compiled numpy which is python3-numpy

I been trying to make it work from 2AM till 9AM I got decent upto testing it out but I think there is an issue with the code pins and my physical wiring.

To summarize what problems I encounter
- SPI and GPIO permission access
- Code path miss match when accessing image or gif
- Armbian have no default SPI and GPIO user groups
- Trying to run python script outside the virtaul environment. Dumb Teodi
- Issue with Pillow not being compiled because of missing dependencies 
- Dont know how to add ram to assist on numpy and pillow unpacking and compilatioin.
# Allocate a empty 2GB file block named swapfile
sudo fallocate -l 2G /swapfile

# Lock down the file permissions for core system security
sudo chmod 600 /swapfile

# Format the empty container file layout specifically into Linux Swap
sudo mkswap /swapfile

# Dynamically link and load the file into active live system memory
sudo swapon /swapfile

- system is missing the C development header files for image formats (like JPEG and PNG) that Pillow needs to compile on your 32-bit ARM board (armv7l).
