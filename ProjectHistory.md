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

Ordered wire crimper for my own custom dupont female wire since I suspect and anticipate that wiring will be headache using the cheap china maid wires.
- I have crimp my own wires
- Change the wiring and double check the connection and it works right out of the bath.

I just tweak minor details in the code like the path and its working fine.

## Next Goal
Generate QRcode image:
able to generate qrcode using qrcode library from python
Ai/Gemini write the script. able to display it since I dont have enough time to study the code.
tested on scanning and connecting to wifi network. and currently works.


Today I am trying to connect my orange pi one through internet since connecting it through cable is inconvinient.
I am using 802.11N wireless dougle that I have baught long time ago.
Steps Taken
- Inserted the dougle on he usb port of orange pi one
- Hook up my orange pi one to my computer using USB to TLL
- open putty throuch Com5 port with 115200 Baud rate
- login to my orange pi one running armbian (debian trixie)
- check if the device is detected by the board by running command lsusb and it show up as
    teodi@orangepione:~$ lsusb
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 002: ID 0bda:f179 Realtek Semiconductor Corp. RTL8188FTV 802.11b/g/n 1T1R 2.4G WLAN Adapter
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
- ip link command show now interface this is because the system cant talk to the dougle since it need a driver to talk to the kernel
- sudo apt install build-essential linux-headers-$(uname -r) failed follow to the steps on this repo (https://github.com/Mr-DS-ML-85/rtl8188fu/tree/main)
Error results:
Error: Unable to locate package linux-headers-6.18.35-current-sunxi
Error: Couldn't find any package by glob 'linux-headers-6.18.35-current-sunxi'
The apt tool is failing because Armbian names its kernel header packages differently than standard Debian. Instead of matching your exact uname -r string, the package uses a generic name for your processor family (sunxi)
- sudo apt install -y build-essential linux-headers-current-sunxi
build-essential is already the newest version (12.12).
Installing:
  linux-headers-current-sunxi
  CC      /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/staticobjs/zip.o
Installing dependencies:
  bison  flex  libelf-dev  libssl-dev  libzstd-dev  m4

Suggested packages:
  bison-doc  flex-doc  libssl-doc  m4-doc

Recommended packages:
  libfl-dev

Summary:
  Upgrading: 0, Installing: 7, Removing: 0, Not Upgrading: 26
  Download size: 20.4 MB
  Space needed: 101 MB / 56.7 GB available
  CC      /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/staticobjs/elf.o
  CC      /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/staticobjs/features.o
  CC      /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/staticobjs/btf_iter.o
  CC      /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/staticobjs/btf_relocate.o
  LD      /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/staticobjs/libbpf-in.o
  LINK    /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/libbpf/libbpf.a
  HOSTCC  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/main.o
  HOSTCC  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/rbtree.o
  HOSTCC  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/zalloc.o
  HOSTCC  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/string.o
  HOSTCC  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/ctype.o
  HOSTCC  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/str_error_r.o
  HOSTLD  /usr/src/linux-headers-6.18.35-current-sunxi/tools/bpf/resolve_btfids/resolve_btfids-in.o
  LINK     resolve_btfids
Done compiling kernel-headers (6.18.35-current-sunxi).
Done compiling kernel-headers tools (6.18.35-current-sunxi).
Armbian 'linux-headers-current-sunxi' for '6.18.35-current-sunxi': 'postinst' finishing.
Processing triggers for man-db (2.13.1-1) ...
Warning: Operation was interrupted before it could finish
 kernel headers successfully compiled and installed, but the process was interrupted right at the very end during the man-db trigger.
 the process was interrupted right at the very end during the man-db trigger.You need to fix the interrupted package state and complete the remaining installations (network-manager, git, dkms) before compiling the driver.
- sudo dpkg --configure -a (command to remove incomplete installation)
- sudo apt install -y network-manager git dkms
git is already the newest version (1:2.47.3-0+deb13u1).
Installing:
  dkms  network-manager

Installing dependencies:
  libbluetooth3  libmm-glib0  libndp0  libnm0  libteamdctl0

Suggested packages:
  menu  libteam-utils  iptables

Recommended packages:
  fakeroot  modemmanager  ppp  dnsmasq-base  polkitd  network-manager-l10n

Summary:
  Upgrading: 0, Installing: 7, Removing: 0, Not Upgrading: 26
  Download size: 2,769 kB
  Space needed: 8,671 kB / 56.5 GB available

Get:1 http://deb.debian.org/debian trixie/main armhf dkms all 3.2.2-1~deb13u1 [60.1 kB]
Get:2 http://deb.debian.org/debian trixie/main armhf libbluetooth3 armhf 5.82-1.1 [96.1 kB]
Get:3 http://deb.debian.org/debian trixie/main armhf libmm-glib0 armhf 1.24.0-1+deb13u1 [202 kB]
Get:4 http://deb.debian.org/debian trixie/main armhf libndp0 armhf 1.9-1+b1 [10.9 kB]
Get:5 http://deb.debian.org/debian trixie/main armhf libnm0 armhf 1.52.1-1 [392 kB]
Get:6 http://deb.debian.org/debian trixie/main armhf libteamdctl0 armhf 1.31-1+b2 [10.1 kB]
Get:7 http://deb.debian.org/debian trixie/main armhf network-manager armhf 1.52.1-1 [1,998 kB]
Fetched 2,769 kB in 0s (6,118 kB/s)
Selecting previously unselected package dkms.
(Reading database ... 68634 files and directories currently installed.)
Preparing to unpack .../0-dkms_3.2.2-1~deb13u1_all.deb ...
Unpacking dkms (3.2.2-1~deb13u1) ...
Selecting previously unselected package libbluetooth3:armhf.
Preparing to unpack .../1-libbluetooth3_5.82-1.1_armhf.deb ...
Unpacking libbluetooth3:armhf (5.82-1.1) ...
Selecting previously unselected package libmm-glib0:armhf.
Preparing to unpack .../2-libmm-glib0_1.24.0-1+deb13u1_armhf.deb ...
Unpacking libmm-glib0:armhf (1.24.0-1+deb13u1) ...
Selecting previously unselected package libndp0:armhf.
Preparing to unpack .../3-libndp0_1.9-1+b1_armhf.deb ...
Unpacking libndp0:armhf (1.9-1+b1) ...
Selecting previously unselected package libnm0:armhf.
Preparing to unpack .../4-libnm0_1.52.1-1_armhf.deb ...
Unpacking libnm0:armhf (1.52.1-1) ...
Selecting previously unselected package libteamdctl0:armhf.
Preparing to unpack .../5-libteamdctl0_1.31-1+b2_armhf.deb ...
Unpacking libteamdctl0:armhf (1.31-1+b2) ...
Selecting previously unselected package network-manager.
Preparing to unpack .../6-network-manager_1.52.1-1_armhf.deb ...
Unpacking network-manager (1.52.1-1) ...
Setting up dkms (3.2.2-1~deb13u1) ...
Setting up libteamdctl0:armhf (1.31-1+b2) ...
Setting up libnm0:armhf (1.52.1-1) ...
Setting up libmm-glib0:armhf (1.24.0-1+deb13u1) ...
Setting up libbluetooth3:armhf (5.82-1.1) ...
Setting up libndp0:armhf (1.9-1+b1) ...
Setting up network-manager (1.52.1-1) ...
Created symlink '/etc/systemd/system/dbus-org.freedesktop.nm-dispatcher.service' → '/usr/lib/systemd/system/NetworkManager-dispatcher.service'.
Created symlink '/etc/systemd/system/network-online.target.wants/NetworkManager-wait-online.service' → '/usr/lib/systemd/system/NetworkManager-wait-online.service'.
Created symlink '/etc/systemd/system/multi-user.target.wants/NetworkManager.service' → '/usr/lib/systemd/system/NetworkManager.service'.
Processing triggers for dbus (1.16.2-2) ...
Processing triggers for libc-bin (2.41-12+deb13u3) ...
Processing triggers for man-db (2.13.1-1) ...
teodi@orangepione:~$
- git clone https://github.com/kelebek333/rtl8188fu
teodi@orangepione:~$ git clone https://github.com/kelebek333/rtl8188fu
Cloning into 'rtl8188fu'...
remote: Enumerating objects: 997, done.
remote: Counting objects: 100% (122/122), done.
remote: Compressing objects: 100% (58/58), done.
remote: Total 997 (delta 94), reused 69 (delta 64), pack-reused 875 (from 3)
Receiving objects: 100% (997/997), 9.21 MiB | 4.13 MiB/s, done.
Resolving deltas: 100% (512/512), done.
teodi@orangepione:~$
- followed this instruction for driver installation (https://github.com/kelebek333/rtl8188fu)
- git clone https://github.com/kelebek333/rtl8188fu
- sudo dkms install ./rtl8188fu
- sudo cp ./firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/
- sudo nmtui > Activate a connection > select wifi > input password > ok
- ip link
teodi@orangepione:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: end0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether 02:81:70:18:79:b9 brd ff:ff:ff:ff:ff:ff
    altname enx0281701879b9
3: wlx00e0237fe81b: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether 00:e0:23:7f:e8:1b brd ff:ff:ff:ff:ff:ff
- remove the ethernet cable
- sudo -c4 google.com check internet connection
teodi@orangepione:~$ sudo ping -c4 google.com
PING google.com (142.250.207.46) 56(84) bytes of data.
64 bytes from nrt13s55-in-f14.1e100.net (142.250.207.46): icmp_seq=1 ttl=114 time=211 ms
64 bytes from nrt13s55-in-f14.1e100.net (142.250.207.46): icmp_seq=2 ttl=114 time=45.2 ms
64 bytes from nrt13s55-in-f14.1e100.net (142.250.207.46): icmp_seq=3 ttl=114 time=52.9 ms
64 bytes from nrt13s55-in-f14.1e100.net (142.250.207.46): icmp_seq=4 ttl=114 time=9.67 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3003ms
rtt min/avg/max/mdev = 9.673/79.731/211.156/77.609 ms
teodi@orangepione:~$
