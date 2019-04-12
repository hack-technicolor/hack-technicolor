#########################################################################################################################################################################################################

## IMPORTANT - Leave gateway turned off until you understand these instructions.


<b>The ISP could lock you out of the gateway by pushing an updated firmware to it through a landline, WiFi or SIM card connection, until the gateway is rooted and remote management disabled.</b>

Ensure the gateway does not have a wired or wireless internet connection. Gateways with 4G Backup, such as the DJA/DJN Series Frontier or Smart Modem, must also have the SIM removed from under the bottom 25mm x 25mm white plastic sticker. on the DJA0231, the sim is under a small rubber plug above the green phone port.

#########################################################################################################################################################################################################

## Things you will need

<b>You need the following BEFORE you go offline!</b>

- The latest version of the AutoFlashGUI software, available from GitHub either as a ZIP file: <a href="https://github.com/mswhirl/autoflashgui/archive/master.zip">master.zip</a> or you can browse the source code and change history at <a href="https://github.com/mswhirl/autoflashgui">the project page</a>. Make sure the tool runs and GUI loads *before* you go offline!

- The old RBI <a href="https://whirlpool.net.au/wiki/hw_model_1622">firmware</a> file for your gateway.

- The new RBI <a href="https://whirlpool.net.au/wiki/hw_model_1622">firmware</a> file for your gateway <b>only if you want to flash the latest version. 16.3 is the best and most stable.</b>

- An SSH client - the famous <a href="https://www.chiark.greenend.org.uk/%7Esgtatham/putty/">Putty</a> is recommended for Windows. <a href="https://winscp.net/eng/download.php">WinSCP</a> is optional.

- A copy of this web page for reference while you're offline ([*warning:*] the browser can split long command lines which won't work so best to copy code and paste into a text editor like notepad.  Don't just print to PDF, it cuts off lines and breaks things!).  

- Physical access to the gateway so you can power cycle it and unplug the WAN/DSL while you're going through this process.

- A 'happy' gateway! If it's in bridge mode or half the tiles are missing on the screen (which seems to be caused by corrupted config), reset it to <a href="/Technicolor%20Recovery">factory defaults</a> first.

#######################################################################################################################################################################################################

## Introduction

#### Known Working Models

- Technicolor TG799vac (aka Telstra Gateway Max)
- Technicolor TG799vac Xtream
- Technicolor TG789vac v2
- Technicolor TG789vac v2 HP
- Technicolor TG797n v3 (aka Telstra T-Gateway)
- Technicolor TG800vac (aka Telstra Gateway Max 2)
- Technicolor DJN2130 (aka Telstra Frontier Gateway) 
- Technicolor DJA0231 (aka Telstra Smart Modem Gen2)

Tip: avoid referring to your device by its commercial name only if it is ambiguous (ie "TG799vac"), refer to your device with its unique board mnemonic identifier XXXX-X instead to avoid ambiguity. You should be able to read this somewhere in the web configuration pages. Golden rule: same mnemonic, same device.

<b>NB: Firmware version 16.3.x works the best in terms of xDSL sync and compatibility. Use if available</b>

#######################################################################################################################################################################################################

## The Basics

Devices mentioned above are very capable pieces of equipment each with different feature set which may include: 802.11ac, MU-MIMO, ADSL2/VDSL2/eVDSL modem, DECT base station, <a href="https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station">FXS</a> ports, and <a href="https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station">FXO port</a>, 4G backup, etc.
They are known to get high sync speeds for VDSL2, have high quality internal PCB and power supply and their power consumption is quite good, for example the 799 Xtream uses about 12 watts with WiFi on (typical router config) and 9 watts with WiFi off (typical bridge mode config). 

The guide was originally written for gateways provided directly by Telstra and as such, has Telstra branded firmware.
Usually, there is no ‘generic’ firmware available that will just give you access to the gateway as any other device you would purchase. This kind of sucks as if you decide to use this device with anyone other than Telstra, you lose access to the VoIP functionality and therefore also DECT base station, FXS/FXO ports.
That was the motivation to get into this device and re-enable as many features as possible. For some other devices, an alternative no-brand firmware (MST) is available where no configurations options are locked out, but getting root access to it will still open a wider window of possibilities.

The default IP address of the gateway varies by firmware, it could be `10.0.0.138`, `192.168.0.1`, `192.168.1.1`, `10.1.1.1` and so on. Your best option is to get an IP address by DHCP the first time you connect and see what you get as default gateway.

#######################################################################################################################################################################################################

### Gaining Root Access

These instructions were built for the TG799vac, so if you are doing this for a different gateway be sure to use the correct firmwares.
In this example, 16.3 is the older Type 2 firmware, 17.2 is the newer Type 1 firmware.

Run up the AutoFlashGUI tool and flash vant-f_CRF683-17.2.188-820-RA.rbi to your gateway.

![17.2 AFG](images/flashgui_17.2.png)

This will take about 3-4 minutes. The flasher will try and root your gateway but it will fail (silently); this is expected. If the flash fails to push the firmware in, try again (is the username and password correct?), and if it still fails with some permission error in the console, you may have been locked out of flashing via the web interface: bad luck. Maybe a PXE firmware load can help but you require good luck at this point. Ask for help in the whirlpool thread! (Note that firmware before v15.x may require some manual work, see the advanced topic "My firmware is so old that AutoFlashGUI can't authenticate to the gateway!" )

Now use AutoFlashGUI to flash in vant-f_CRF687-16.3.7567-660-RG.rbi and allow it to run through including getting root.

![16.3 AFG](images/flashgui_16.3.png)

At this point we are ready to do the procedure to activate root on 17.2 and switch over to it. This procedure works by allowing us to mod the inactive (but newer) image's file system and config, then switch back to it without doing a factory reset or official upgrade. Note that if you factory reset while on 17.2 you will need to run the entire procedure from where you flashed v16.3 to get root back, and it could upgrade and lock you out permanently in that reset state if it has internet access!

Fire up your SSH client and connect to the gateway IP on port 22.

Run the following command to look at your installed firmwares state:
`find /proc/banktable -type f -print -exec cat {} ';'`

It should look something like this:
```
/proc/banktable/notbootedoid
59b21e26bc549719f7f1bedd
/proc/banktable/bootedoid
5940db6a20338215a4c97c89
/proc/banktable/passiveversion
17.2.0188-7021004-20170908063550-00f42f11f9c253e3f1001b1558043e970a3d9b5d
/proc/banktable/activeversion
16.3.7567-2521030-20170614084458-887a8c777ed8527277d7137ed9149816c889cf1d
/proc/banktable/inactive
bank_2
/proc/banktable/active
bank_1
/proc/banktable/notbooted
bank_2
/proc/banktable/booted
bank_1
```

These gateways use two flash partitions (bank_1 and bank_2) which can be upgraded/used almost independently. They are digital-signature verified before boot so you can't edit the rom image in the flash (yes, we tried).  The config is stored in the matching folder in /overlay i.e. /overlay/bank_2 (hint: you can see your modified config files in here if you want to back stuff up or see what changes you made).  When a proper factory reset is done, the overlay partition is formatted (but not securely wiped; see section later).

Run the following to set 17.2 up for temporary root and switch back to it:
```
rm -rf /overlay/`cat /proc/banktable/inactive`
mkdir /overlay/`cat /proc/banktable/inactive`
chmod 755 /overlay/`cat /proc/banktable/inactive`
mkdir /overlay/`cat /proc/banktable/inactive`/etc
chmod 775 /overlay/`cat /proc/banktable/inactive`/etc
echo "echo root:root | chpasswd" > /overlay/`cat /proc/banktable/inactive`/etc/rc.local
echo "dropbear -p 6666 &" >> /overlay/`cat /proc/banktable/inactive`/etc/rc.local
chmod +x /overlay/`cat /proc/banktable/inactive`/etc/rc.local
echo `cat /proc/banktable/inactive` > /proc/banktable/active
sync
cat /overlay/`cat /proc/banktable/active`/etc/rc.local
```

Now check it all looks right - you should get this output from the last command:
```
echo root:root | chpasswd
dropbear -p 6666 &
```
Reboot and wait 3 to 4 minutes for the gateway to boot into 17.2.

Log in to the gateway with SSH on port 6666 using root/root. At this point you have temporary root, but you can't stop at this point! Go on and proceed to permanent root access setup section below.

#####################################################################################################################################################################################################################

#### Type 2 Procedure

Run AutoFlashGUI and select the option for your gateway (in this case "Telstra TG799 17.2.0261 Type 2").

Check "Target IP:" 10.0.0.138 ( or whatever is the default ip of your device ).

Some gateways will not need new firmware flashed. If the Telstra TG799vac gateway is not already on 17.2.0261 firmware version, select the "Flash firmware?" checkbox and put in the firmware file name i.e vant-f_CRF852-17.2.0261-820-RA.rbi . <a href="https://mswhirl.github.io/tcolmodimages/flashgui_16.3.png">Example screenshot</a> (pick the correct options and filename as stated above).

Select "Run", wait for the process to finish.

Log in to the gateway with SSH on port 6666 using root/root. At this point you have temporary root, but you can't stop at this point! Go on and proceed to the next step.

#####################################################################################################################################################################################################################

### Setting Up Permanent root Access

Run the following in SSH to turn on more functionality and clean up.  Note that you can only paste so much into the terminal, so it has been split into blocks that should work.

```	
# Block 1
uci delete cwmpd.cwmpd_config
uci delete firewall.cwmpd
uci delete dhcp.hotspot
uci delete dhcp.fonopen
uci delete wifi_doctor_agent.acs
uci delete wifi_doctor_agent.config
uci delete wifi_doctor_agent.as_config
uci delete tls-vsparc.Config
uci delete tls-vsparc.Passive
uci delete autoreset.wifidoctor_enabled
uci delete autoreset.vsparc_enabled
uci delete autoreset.thor_enabled
uci set ddns.myddns_ipv4.enabled='0'
uci set dropbear.wan.enable='0'
uci set dropbear.lan.enable='1'
uci set dropbear.lan.PasswordAuth=on
uci set dropbear.lan.RootPasswordAuth=on
uci add_list web.ruleset_main.rules=iproutesmodal
uci set web.iproutesmodal=rule
uci set web.iproutesmodal.target='/modals/iproutes-modal.lp'
uci add_list web.iproutesmodal.roles='admin'
uci add_list web.ruleset_main.rules=systemmodal
uci set web.systemmodal=rule
uci set web.systemmodal.target='/modals/system-modal.lp'
uci add_list web.systemmodal.roles='admin'
uci add_list web.ruleset_main.rules=relaymodal
uci set web.relaymodal=rule
uci set web.relaymodal.target='/modals/relay-modal.lp'
uci add_list web.relaymodal.roles='admin'
uci add_list web.ruleset_main.rules=natalghelpermodal
uci set web.natalghelpermodal=rule
uci set web.natalghelpermodal.target='/modals/nat-alg-helper-modal.lp'
uci add_list web.natalghelpermodal.roles='admin'
```

And finally:
```
# Block 2
uci add_list web.ruleset_main.rules=diagnosticstcpdumpmodal
uci set web.diagnosticstcpdumpmodal=rule
uci set web.diagnosticstcpdumpmodal.target='/modals/diagnostics-tcpdump-modal.lp'
uci add_list web.diagnosticstcpdumpmodal.roles='admin'
uci set system.config.export_plaintext='1'
uci set system.config.export_unsigned='1'
uci set system.config.import_plaintext='1'
uci set system.config.import_unsigned='1'
uci set web.uidefault.upgradefw_role='admin'
uci add_list web.parentalblock.roles='admin'
uci commit
sed -e 's/session:hasAccess("\/modals\/diagnostics-network-modal.lp")/session:hasAccess("\/modals\/diagnostics-network-modal.lp") and \n session:hasAccess("\/modals\/diagnostics-tcpdump-modal.lp")/' -i /www/cards/009_diagnostics.lp
sed -e 's^alt="network"></div></td></tr>\\^alt="network"></div></td>\\\n <td><div data-toggle="modal" data-remote="modals/diagnostics-tcpdump-modal.lp" data-id="diagnostics-tcpdump-modal"><img href="#" rel="tooltip" data-original-title="TCPDUMP" src="/img/network_sans-32.png" alt="network"></div></td></tr>\\^' -i /www/cards/009_diagnostics.lp
sed -e 's/{"logviewer-modal.lp", T"Log viewer"},/{"logviewer-modal.lp", T"Log viewer"},\n {"diagnostics-tcpdump-modal.lp", T"tcpdump"},\n/' -i /www/snippets/tabs-diagnostics.lp
sed -e 's/if currentuserrole == "guest" /if currentuserrole == "admin" /' -i /www/docroot/modals/gateway-modal.lp
echo > /etc/rc.local
killall -q -9 hotspotd cwmpd cwmpdboot watchdog-tch wifi-doctor-agent tls-vsparc
$ # Super modders may wish to remove the next line before running.  Most people want it to free up overlay space.
opkg --force-removal-of-dependent-packages remove conf-cwmpd cwmpd autoreset-tch mappings-fon geolocation-tch
find /rom/usr/lib/ipk -type f |xargs -n1 basename | cut -f 1 -d '_' |xargs opkg --force-removal-of-dependent-packages remove
echo > /etc/dropbear/authorized_keys
/etc/init.d/dnsmasq restart
/etc/init.d/nginx restart
/etc/init.d/dropbear start
echo "Please change the root password NOW using the 'passwd' command to secure your router.  Length greater than 12 recommended, mix up alpha, digits and some punctuation for best results.  Don't use a simple password!"
```
#####################################################################################################################################################################################################################

### Change the root Password
<b>Do not ignore this step!</b> :)

Run: `passwd`



Reboot now if you're not doing any further configuration.

At this point you should now be able to SSH in with root and your password (which should no longer be root at this point!)

#####################################################################################################################################################################################################################

### My firmware is so old that AutoFlashGUI can't authenticate!

This is because they changed the web authentication method to SRPv6 with firmware v15, and this is the only method that the AutoFlashGUI tool knows how to authenticate with.  You are going to have to flash the v16.3 .rbi file via sysupgrade after using the original manual procedure to get a shell.

Visit the ‘Diagnostics’ page on the gateway, and click on the Ping & Traceroute tab. (If your gateway doesn’t display the Diagnostics tile, factory reset the gateway. The observation is that this only happens when the config is corrupted somehow.) In the IP address section, enter and run:
$ :::::::;echo root:root | chpasswd; dropbear -p 6666;

Give it 30 seconds to generate SSH host keys and then try to connect to your gateway with SSH on port 6666 with root/root.
Copy the .rbi to a USB stick (FAT32 formatted is most likely to work on old firmware) and insert it into the gateway.
If you type 'cd /mnt/' and keep hitting tab it should eventually get to the end of the USB stick path, then hit enter. (You can also run 'mount' and try to work out the path the USB stick is mounted on, or 'dmesg' to check the system log to see if there was an error automatically mounting it.)
To be on the on the safe side we will copy the rbi to RAM, then flash it. Do the following with the correct .rbi name (keeping in mind that this is case sensitive):
$ cp filename.rbi /tmp
cd /tmp
sysupgrade filename.rbi

All things going well you should see it progress along and reboot, then you can commence the current procedure.

