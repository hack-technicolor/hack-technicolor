
#################################################################################################################################################################################################

## IMPORTANT - Read before Attempting!

!!! caution "DISCLAIMER"
    In some cases there is no way of knowing your exact situation and taking the wrong actions could get things worse and potentially brick your gateway. Anyone following this guide accepts full responsibility for the outcomes.

This guide is based upon most frequent troubles                   where you experience your device being stuck in different states.


#################################################################################################################################################################################################

## 0. Wipe custom data partition

Technicolor gateways platformas are usually built on a firmware+data design, which consists of (a couple of) read-only filesystems (squashfs) stored in *firmware banks* plus a writable filesystem (jffs2) for user dafa storage.

In modern Homeware firmwares, based on a fork of OpenWrt, the user data partition consists of an overlay which contents get applied every time on top of the original root filesystem, stored as read-only firmware in the booted bank. For dual-bank gateways, the user data partition contains a distinct overlay for each firmware bank.

The space available into the user data partition is shared across both bank's overlays.

If you think you are not completely aware of what's going on or you don't know what you did wrong, it is strongly recommended you just completely **wipe the user data parition only**, and all you did to your device for **both banks** will be lost.

!!! note "This reset method is not available if..."    
	- you have lost any kind of access to root shell by either SSH, or telnet, or serial console, and you have no more ways of executing a custom command as root
    - the gateway bootloops or fails to boot properly

1. Log in to root shell (whatever you have available between SSH, telnet, serial console ...)
2. Check `cat /proc/mtd` outputs and look for your user data partition name, it could be either `userfs` on older devices, or `rootfs_data` on newer ones
3. Run `mtd erase rootfs_data` or `mtd erase userfs` accordingly
4. Reboot the gateway.


#################################################################################################################################################################################################

## 1. Reset to Factory Defaults (RTFD)

If at some point you can no longer connect to the gateway or you want to make a fresh install, it may be useful to perform a "reset to factory defaults (RTFD)".

!!! note
    A RTFD deletes all changes you made to files and configurations relative to the booted bank. After the reset a reconfiguration of your gateway will be needed and wireless clients will also have to be re-associated.

This feature is iimplemented by an official tool from technicolor you can invoke in different equivalent ways. Choose between:
1. RTFD via the web interface
2. RTFD via the reset button
3. RTFD via the CLI shell
4. Manually do what RTFD does via root shell

!!! caution "Unroot prevention"
    Some un-root prevention mechanisms implemented by various modders may inject or modify default RTFD behaviour. If you installed some custom mod which has un-root prevention features, take into account that RTFD may be broken because of such modifications.

#### RTFD via the web interface

!!! note "This RTFD method is not available if..."
	- the web interface is corrupt and not accessible
	- the gateway bootloops or fails to boot properly
	- the `userfs` or `rootfs_data` jffs2 filesystem is full

1. Browse to the gateway web interface.
2. Click gateway. The gateway page appears.
3. Click Reset.
4. The gateway deletes all customized data for the booted bank and restarts.

#### RTFD via the reset button

!!! note "This RTFD method is not available if..."
	- the physical reset button of the gateway have been disabled
	- the gateway bootloops or fails to boot properly
	- the `userfs` or `rootfs_data` jffs2 filesystem is full

1. Make sure the gateway is turned on and completely booted
2. Push the Reset button for at least 7 seconds and then release it
3. The gateway deletes all customized data for the booted bank and restarts

#### RTFD via the CLI shell

!!! note "This RTFD method is not available if..."
	- you have no kind of access to CLI by either SSH, or telnet, or serial console
	- the gateway bootloops or fails to boot properly
	- the `userfs` or `rootfs_data` jffs2 filesystem is full

1. Make sure the gateway is turned on and completely booted
2. Login to the CLI, RTFD is also available in restricted shall (clash)
3. Just run `rtfd` command
4. The gateway deletes all customized data for the booted bank and restarts

#### Manually do what RTFD does

!!! note "This reset method is not available if..."
	- you have no kind of access to root shell by either SSH, or telnet, or serial console
	- the gateway bootloops or fails to boot properly
	- the `userfs` or `rootfs_data` jffs2 filesystem is full

1. Make sure the gateway is turned on and completely booted.
2. Login to root shell
3. Just run `rm -rf /overlay/bank_N` command, where **N** is either number of the bank you want to RTFD
4. All customized data for that bank is gone. You could now eventually restore some rooting scripts or previous and working backup for the current correct firmware version
5. Turn off device to reboot

#### Restore your settings

If you previously backed up your configuration, you can now restore this configuration to your gateway.


#################################################################################################################################################################################################

## 2. BOOT-P recovery mode (TFTP flashing)

This guide is useful if you need to load a different firmware on your `bank_1` firmware partition, in case of a downgrade or replace a corrupt one.

!!! note "Your firmware is unlikely to be corrupt"
    If your gateway stopped working normally after some mods or tweaks, it is very unlikely you messed up the firmware partitions since all your mods and settings are stored in the `userfs` or `rootfs_data` partition instead.
	Reloading a firmware in such situations won't make any difference unless you load a different version which is known to somehow work fine enough with your messed up mods & settings.

This should work for any known Technicolor device build on a Broadcom BCM63xx platoform. Since basically forever, Technicolor gateways have had a corrupt firmware recovery mechanism built in.  

By holding down a button at power on on the gateway, while the appropriate software is running on your PC, you can reload firmware into the first firmware bank of the gateway, `bank_1` (no one has observed it writing to `bank_2`). 

If both firmware banks contains invalid firmwares the gateway will enter BOOT-P recovery mode automatically after three failed attempts for each bank

!!! warning "Please note and take into account"
    - This will not automaticlly switch active bank for you, if active bank is `bank_2` and it stil contains a valid firmware it will still boot it instead of that one you are loading here.
 
    - Flashing via this method does not perform any factory reset, the new firmware will run on old and possibly corrupt or incompatible settings. It is therefore recommended that you perform a factory reset before flashing some firmware which is too different or not capable of managing a settings upgrade from the current one.
  
    - The firmware image is digital signed and verified upon boot, so you can't boot an incorrect image (a good thing) but you also can't load a modified image (sad face times 1000).


#################################################################################################################################################################################################

### Set up TFTP

#### Background

This guide is written for Windows but it should work on Linux too if you adapt the configuration.

**What you will need**

1. A computer running a DHCP server and TFTP server.
   This guide uses TFTP64 for windows which implements both.

2. RBI firmware file for your specific gateway board.

3. A wired ethernet connection with static IP address assigned.
   BOOT-P recovery mode does not support Wi-Fi.

5. A few cups of coffee

6. About 30min to an hour


#################################################################################################################################################################################################

### Setting up the Server

1. Download the latest normal edition of [TFTP64](http://tftpd32.jounin.net/tftpd32_download.html) and install it.

- Get the [firmware](https://whirlpool.net.au/wiki/hw_model_1622) (.rbi) file you want to load into the gateway and place it in the TFTP64 folder.  You may use another folder and change the settings appropriately if you wish.

- Connect the Ethernet port on your PC to one of the LAN ports on the gateway (usually LAN1).

- Turn the gateway off.

- On the PC ensure the network card you wish to use is set to DHCP: 

- Press Windows+R to run `ipconfig /all | find "DHCP Enabled"` or check multiple cards with `ipconfig /all`. [Microsoft help page](https://support.microsoft.com/en-us/help/15089/windows-change-tcp-ip-settings). 
(Unless you are using Static IPs on your network this will already be done.  After the next few steps, the network card will receive an address from the TFTPD64 DHCP server.)

- Start TFTP64.

- Click Settings.

- On the GLOBAL tab enable only the following: TFTP Server, DHCP Server.

![TFTP64](images/TFTPD_100_GLOBAL.png)

- On the TFTP tab the default options should be OK (base directory should be `.` )

![TFTP64](images/TFTPD_200_TFTP.png)

- On the DHCP Server tab: 

	- 	IP pool start address 10.0.0.100

	-	Size of pool: 20

	-	Boot file: the firmware filename to flash i.e. vant-f_CRF687-16.3.7567-660-RG.rbi

	-	Def Router (Opt 3): 10.0.0.99

	-	Mask (Opt 1): 255.255.255.0

	- 	DNS Servers (Opt 6): 10.0.0.99

- Check against:

![TFTP64](images/TFTPD_300_DHCP.png)

- Click OK

- Accept the you will need to restart message.

- On the main screen Change the 'Server Interfaces' selection to your Ethernet network card.

- Close TFTPD64.

- Re-open TFTPD64.

- If you get a firewall warning, allow access on both private **and public** networks. Please note the temporary network between your PC and device in BOOT-P mode will always be of public type by default.

- If you don't get any firewall warning and you don't remember if you have already allowed access for TFTP64 in past, please, check firewall settings to confirm it's allowed already or temporally disable firewall.

- The server interface should now show an IP in the 10.0.0.x range and after a few seconds: the PC gets an IP from the TFTP64 program via DHCP.

![TFTP64](images/TFTPD_400_Main.png)

You are now ready to try booting the gateway to do the flash!

#################################################################################################################################################################################################

### Flashing the Firmware

** Required steps **

1. Set up TFTP to send firmware in BOOTP mode, please initially see above, or [this guide](https://www.jonathandavis.me.uk/2013/12/flashing-generic-firmware-on-a-technicolor-tg582n/).

2. Ensure TFTP is on the log viewer tab.

3. Connect one end of the network cable to any LAN port on the gateway DO NOT use the WAN port, and the other end to the nic on the pc.

4. Place gateway into BOOTP mode, this is achieved by turning it off, holding the reset button down and powering on.
	- For TG789vac and TG799vac wait for the ethernet light to flash.
	- For TG800vac count to about 5.
	- TFTP may detect the sooner though.


5. Let the firmware flash, a download progress bar will show. When completed, the gateway will start flashing the received firmware. Wait for the gateway to reboot.
	- It may take a few attempts for TFTP to connect and send the firmware, and you may have to put the gateway into BOOTP mode again if you send no firmwares for a while.
	

6. After gateway has rebooted, wait for approx 4-10min.

From here, gateway has the firmware you flashed into its `bank_1` partition.

!!! note "A few things to note"
- Again, the gateway will not boot from this new firmware if `bank_2` is active and contains a valid firmware. Would you like to force it booting from `bank_1` instead? Read below chapters.

- TFTP does not always play nice & may require a few loads to get working, as well as mentioned above, BOOT-P mode can be a pain.

- This guide and process will not work if your device is bricked at bootloader stage.

- If you did not perform RTFD for `bank_1` before TFTP flashing and the new firmware is not fully compatible with previous one, you may now have booted into an unstable setup. If so, you either need to perform RTFD now or wipe user data partition. Read above chapters.

#################################################################################################################################################################################################

## 3. Booting from passive bank

#################################################################################################################################################################################################

Dual-banks gateways work very similar to a dual-boot system. You have a data partition where to store personal data and two OS partitions each one with a different OS. Here we have a data aprtition and two firmware banks.

When you power on your device it starts loading by default the firmware into the so called *active bank*. With no surprise, the other one gets called *passive bank*. Of course only one bank at time can be the active one.

!!! hint "BOOT-P flashes into bank_1 only"
    BOOT-P recovery mode allows flashing a valid firmware into `bank_1` only, and will do so even if the active bank is currently `bank_2`, and will not set `bank_1` as active if it is not.

The process of switching active bank is called *switchover*. Ordinary firmware upgrades gets installed into the passive bank, and a switchover occurs at the end of the upgrade process if all went fine. This meaqs your gateway frequently changes active bank, and if you never unlocked it you are unlikely to know which one is currently active.

Whenever the gateway fails to load or crashes three times in a row, the bootloader will enter *failboot* mode and will try booting fron the passive bank, without setting it as active. If the firmware in passive bank fails too, then the bootloader will automatically enter BOOT-P recovery mode. However, it is still possible that some non critical services stops working as expected whithout crashing the whole system, and therefore not causing a failboot from the passive bank.

If you want your device to forcefully boot from the passive bank, which is not currently active, you therefore have two options:
- Set is as active (switchover)
- Trigger a failboot

## Switchover

If you have got shella access into the gateway, this is really trivial as you only need to run the `switchover` command, or manually update contents of `/proc/banktable/active`.

If you have no shell access, but you have the possibility to run a formware upgrade (for example via web interface, AutoFlashGUI or CWMP) as previously stated, a switchover will be executed automatically at the end of the process.

If none of the above options are viable in your situation, unfortunately you must opt for failboot instead.

## Failboot

Failboot comes handy whenever you are locked out from your gateway and you want to forcefully boot the passive bank for any reason.
For example on a Telstra Frontier gateway with v17.2.0261-820-RA loaded, it may be possible to trigger a failboot and boot the old Type 2 16.3 image, which could be still there from into the previous bank by using the timed reset method, and then proceed with the usual rooting guides.

Here you find some alternative ways of triggering a failboot (again, it is a triple boot failure on the active bank). It is really simpler to success if you meanwhile read bootlogs from serial console where you see bootloader messages about each failed attempt. Pick your poison.

#### Timed button action

This is the button pressing sequence for the DJN2130 Telstra Frontier gateway with v17.2.0261-820-RA loaded. Timing for different gateways and very different firmwares may vary.

The sequence is (Minutes:Seconds):

|Step |	Period     | Time   |	Action
|-----|:-----------|:-------|:--------------------------------------------------
| 0	  |    0	   |  0	    | Power on
| 1	  |00:35	   |  00:35	| Press reset
| 2	  |00:11	   |  00:46	| Release
| 3	  |00:47	   |  01:33	| Press reset
| 4   |00:11	   |  01:44	| Release
| 5	  |00:47	   |  02:31	| Press reset
| 6	  |00:11	   |  02:42	| Release
| 7	  |00:50	   |  03:32	| Press reset
| 8	  |00:11	   |  03:43	| Release
| 9	  |06:00	   |    -    | Browse to 192.168.0.1 and confirm firmware version


#################################################################################################################################################################################################

#### Crazy power switching

If you power on your device, and rapidly toggle power switch on and off fast enough it never miss the required power to remain on,
the inner circuits will fail to load and pass firmware validation and corruption checks. Once such checks fail, device will reboot for a new boot attempt. Repeat such that the first three boot attempts fail, then let the fourth attempt to complete.

#### Potentiometer

**You will need** 

- A 3 watt and 100 Ohm Potentiometer 

![Pot](images/pot_bankswitch.jpg)

You only use the middle and outside poles and you split the positive cable to the middle pole from the power supply then the outside right pole looking down at the 3 poles from the knob side to the plug going to the gateway.

Once powered on around 10-15 seconds into the boot cycle you want to turn it around 1/3 turn and just a little more and wait for the led to flash blue then turn it back up and do this 3 times then it will boot on other bank.


#################################################################################################################################################################################################

#### Automatic monitoring of serial console

A Python program written by Mark Smith is available at [GitHub](https://github.com/mswhirl/bouncer) that you can run on a Raspberry Pi which can monitor the serial console output from the gateway and then automatically cycle the power to the gateway to cause a brown-out condition during boot, to reliably force a temporary bank switch. 

Please see the pictures for the physical setup, and the comments at the top of bouncer.py for more technical details (it may require timing tweaks for different models).

If you do any electronics and have some relays and transistors lying around, you probably already have everything required for this just lying around!