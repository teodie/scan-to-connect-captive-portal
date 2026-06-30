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