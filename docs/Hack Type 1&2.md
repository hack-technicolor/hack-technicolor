## IMPORTANT - Leave Gateway turned off until you understand these instructions

!!! warning "Disclaimer"
    This process is not supported by the manufacturer or supplier of your Gateway. There is no way of knowing your situation and the process could break your Gateway or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Things you will need

!!! hint
    You need the following **before** you go offline

1. The latest version of the AutoFlashGUI software, available either as a [ZIP file](https://github.com/mswhirl/autoflashgui/archive/master.zip) or the source at [the project page](https://github.com/mswhirl/autoflashgui).
*Make sure the tool runs and GUI loads before you go offline!*

2. A `Type 2` RBI from [firmware repository](/Firmware%20Repository/) compatible with your Gateway. If you're on a `Type 2` firmware already and the RBI of your same firmware version is available, pick that one.

3. **Optionally**, another [firmware](/Firmware%20Repository/) file (RBI or bank dump) of any *Type* for the firmware version you would like to stay on at the end of the process for daily usage on your Gateway, like a newer one or some old one you feel more stable and comfortable with.

4. An SSH and SCP client - the famous [PuTTY](https://www.chiark.greenend.org.uk/%7Esgtatham/putty/) is fine for SSH in Windows. [WinSCP](https://winscp.net/eng/download.php) is recommended for SCP. If you have any WSL distribution installed (eg. Cygwin or WSL), or you run a Unix-based OS, you should have both SSH and SCP CLI clients available.

5. A copy of this documentation for reference while you're offline. Just keep a tab open in your browser from a mobile device ***or*** see [Hosting these Docs Locally](Host%20this%Locally/).

6. Physical access to the Gateway so you can power cycle it and unplug the WAN/DSL cable while you're going through this process.

7. A *happy* Gateway! If it's in bridge mode or half the tiles are missing (in the GUI), or it's simply not working as expected, just [recover it](/Recovery) to get it to a stock state first.

## Introduction

### Known Working Models

 | Model Number    | Mnemonic | ISP Product Names
 |:---------------:|:--------:|:--------------------------
 | TG797n v3       | DANT-O   | Telstra T-Gateway
 | TG789vac v2     | VANT-6   | -
 | TG789vac (v1)   | VANT-D   | -
 | TG799vac        | VANT-F   | Telstra Gateway Max
 | TG800vac        | VANT-Y   | Telstra Gateway Max 2
 | TG789vac v3     | VBNT-1   | -
 | TG799vac Xtream | VBNT-H   | -
 | DJN2130         | VBNT-J   | Telstra Frontier Gateway
 | TG789vac v2 HP  | VBNT-L   | MyRepublic WiFi Hub+
 | DJA0231         | VCNT-A   | Telstra Smart Modem Gen2

!!! tip "Asking about your gateway?"
    Avoid referring to your device by its commercial product name, refer to your device with its unique board mnemonic identifier `XXXX-X` to avoid any potential ambiguity.

### The Basics

#### Why Hack your Gateway?

Devices mentioned above and similar ones are very capable pieces of equipment, each with different features, which may include: 802.11ac, MU-MIMO, ADSL2/VDSL2/eVDSL modem, DECT base station, [FXS](https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station) ports, [FXO](https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station) port,  4G backup, [SFP](https://en.wikipedia.org/wiki/Small_form-factor_pluggable_transceiver) slot, etc. They are known to have a high quality internal PCB and low power consumption, for example the TG799vac Xtream uses about 12 watts with WiFi on (typical router config) and 9 watts with WiFi off (typical bridge mode config).

The guide was originally written for gateways provided by Telstra and as such, have Telstra branded firmware. Usually, there is no *generic* firmware available that will *just* give you access to the Gateway as any other device you would purchase. This kind of sucks because if you decide to use this device with a different ISP, you are likely to be blocked from doing that, or simply loose some functionality. That was the motivation to hack the device and at least re-enable as many features as possible. For some other devices, a no-brand firmware (MST) exists, where no configurations options are locked out, but getting root access to it will still open a wider window of possibilities.

The default IP address of the Gateway varies by Gateway model, it could be `10.0.0.138`, `192.168.0.1`, `192.168.1.1`, `10.1.1.1` and so on. Your best option is to get an IP address by DHCP the first time you connect and see what your default Gateway is.

## Gaining Root Access

!!! caution "Make sure your Gateway is offline!"
    The ISP could lock you out of the Gateway by pushing a firmware update or configuration script through a landline, WiFi or SIM card connection, until the Gateway is rooted and remote management disabled.

Ensure the Gateway does not have a wired or wireless internet connection. Gateways with 4G Backup, must also have the SIM removed from under the 25mm x 25mm white plastic sticker on the bottom. On the DJA0231, the SIM is under a rubber plug above the green port.

!!! info
    These instructions have been written for the TG799vac (VANT-F) Gateway. So if you are doing this for a different Gateway, be sure to substitute the correct firmware files and change the other options as needed.

Now head on down to the right *Type* section, which fits your current situation.

### Type 1 - Flash of Type 2, then Root

In this example we are working with the `VANT-F` Gateway on `17.2.0261`, which is a `Type 1` firmware. `16.3.7567` is the `Type 2` firmware we are going to flash.

Run AutoFlashGUI and flash the `Type 2` firmware to your Gateway. In this case it is `vant-f_CRF687-16.3.7567-660-RG.rbi`, allowing it to finish flashing and rooting.

!!! warning "Make sure the SSH server is permanent"
    If AutoFlashGUI does not know how to set permanent root access on your model it will create a temporary SSH dropbear instance on port `6666`. You should now configure dropbear in order to run a permanent LAN-side SSH server. Read below, ([Setting up Permanent Root Access](#setting-up-permanent-ssh-server) section), then come back here.

Fire up your SSH client of choice and connect with the Username and Password: `root` to the Gateway IP on default port `22`, or `6666`.

At this point you have a rooted `Type 2` image on your Gateway but your trip is not over.

!!! hint "Upgrade now!"
    Would you like to upgrade to a newer firmware without loosing root access? If so, jump over to [Bank Planning (with firmware upgrade)](#bank-planning-with-firmware-upgrade). Continue reading here otherwise.

If you would like to stay on this `Type 2` firmware for daily usage and stay safe from possible soft-bricks or terrible issues, you now need to ensure that your *bank plan* is correct. Jump to [Bank Planning (without firmware upgrade)](#bank-planning-without-firmware-upgrade).

### Type 2 - Direct Rooting

In this example we will be working with the `VANT-F` Gateway on `16.3.7567` which is a `Type 2` firmware.

Using AutoFlashGUI, allow it to run through getting root.
If you have changed any of the default settings (eg. Gateway IP, Web Interface Password), please change the defaults in the AutoFlashGUI window.

![16.3 AFG](images/flashgui_16.3.png)

If you are unable to fill your profile correctly or AutoFlashGUI is not working, have a look on your local root communities for detailed model-specific root commands. If you manage to find a root command not listed in AutoFlashGUI, create an issue and we will get it added in. Being a `Type 2` firmware, a working root guide surely exists.

!!! warning "Is current SSH server permanent?"
    If AutoFlashGUI does not know how to set permanent root access on your model it will create a temporary SSH dropbear instance on port `6666`. You will configure  dropbear in order to run a permanent LAN-side SSH server later on following this guide.

Fire up your SSH client and connect with user `root` to the Gateway IP on default port `22`, or `6666`.

As your first step into your brand-new rooted Gateway, it is a good idea to always ensure the serial console port is enabled - this is a very useful feature in case of disasters, so just do it. Execute the following command:

```bash
sed -i '\''s/#//'\'' /etc/inittab
```

At this point you have a rooted `Type 2` image on your Gateway, but your trip is not over.

!!! hint "Upgrade now!"
    Would you like to upgrade to a newer firmware without loosing root access? If so, jump over to [Bank Planning (with firware upgrade)](#bank-planning-with-firmware-upgrade). Continue reading here otherwise.

If you would like to stay on this `Type 2` firmware for daily usage and stay safe from possible soft-bricks or terrible issues, you now need to ensure your *bank plan* is correct. Jump to [Bank Planning (without firmware upgrade)](#bank-planning-without-firmware-upgrade).

### Type 3 - Difficult Flash of Type 2, then Root

!!! info "Why are You Here?"
    Did you read the [Homepage](/)?

## Post-Root Procedures

!!! warning "Stop!"
    Do not follow any post-root procedure unless explicitly told to.

### Bank Planning (without firmware upgrade)

Run the following command to look at your Gateway's bank state:

```find /proc/banktable -type f -print -exec cat {} ';'```

Take note of `active` and `booted` banks:

```bash
xxxxx
/proc/banktable/inactive
<take note of this>
/proc/banktable/active
<take note of this>
xxxxx
```

This guide will try to set your modem to the following bank state:

```bash
/proc/banktable/inactive
bank_1
/proc/banktable/active
bank_2
```

!!! caution "Bank Planning: "On which bank should I stay to be safe?""
    It's strongly recommended to adhere to the above situation before modding your device further. The bigger picture description can be found [here](https://github.com/Ansuel/tch-nginx-gui/issues/514). The short thing is that you should really consider modding your preferred firmware version (not necessarily of `Type 2`) while booted from `bank_2` keeping `bank_1` as the active one.
    **Key Point**: it's unsafe to deeply mod firmware settings of any firmware booted from `bank_1`.

These gateways use two flash partitions (`bank_1` and `bank_2`) which can be upgraded/used almost independently.

They are signature checked before boot so you can't flip a single bit in the base firmware image in either bank if you want to see your device booting. The whole config and customized stuff is stored in the matching folder within the [overlay filesystem](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/overlayfs.txt), i.e. `/overlay/bank_2`

!!! hint
    You can see your modified config files in `/overlay` if you want to backup stuff or see what changes you made, however, all original versions of modified files are stored permanently in `/rom`, in case you would like to revert something back.

When a proper Reset to Factory Defaults is done, the overlay partition is not formatted, just the relevant `/overlay/bank_*` partition is deleted. You can learn more on such aspects by reading the [Recovery](/Recovery) page.

You now have to make sure you can boot your current firmware from the recommended bank on every reboot.

!!! danger "Notable exception: Missing RBI"
    In the unfortunate case there are no RBI firmware files available for your model, you can't be really safe because you can't exploit `BOOT-P` recovery options. In such a situation whatever bank you boot is the same. Your best option is to keep a copy of your rootable firmware on both banks. Skip the next step for optimality.

If your `active` bank is `bank_2` already, run the following commands:

```bash
# Activate bank_1
echo bank_1 > /proc/banktable/active
# Erase firmware in bank_1
mtd erase bank_1
```

If your `active` bank is `bank_1` instead, run the following commands:

```bash
# Make a temp copy of the firmware in bank_1
dd if=/dev/mtd3 of=/tmp/bank1.fw
# Flash that copy into bank_2
mtd write /tmp/bank1.fw bank_2
# Clean temp firmware copy
rm /tmp/bank1.fw
# Clean any existing overlay for bank_2 firmware
rm -rf /overlay/bank_2
# Make a temp copy of overlay for bank_1 firmware
cp -rf /overlay/bank_1 /tmp/bank_1_backup
# Free up overlay space by removing existing overlay for bank_1 firmware
rm -rf /overlay/bank_1
# Use the previously made temp copy as overlay for bank_2 firmware
cp -rf /tmp/bank_1_backup /overlay/bank_2
# Activate bank_1
echo bank_1 > /proc/banktable/active
# Erase firmware in bank_1
mtd erase bank_1
# Reboot to first valid firmware
reboot
```

On each reboot, your device will try booting `active` bank first. Since we set `bank_1` as active and we also erased `bank_1` firmware, it will boot from `bank_2`.

Now proceed to setting your own root access [password](#change-the-root-password).

### Bank Planning (with firmware upgrade)

At this point you are ready to activate root on whatever *Type* of firmware you would like, to end up having it rooted and running.

 This procedure works by allowing us to mod the not booted bank and config, then switch over to it without doing a factory reset or standard upgrade procedure. Note that if you factory reset while not on a `Type 2` firmware, you will need to run the entire procedure from the beginning and a auto-upgrade could lock you out permanently in that reset state if the Gateway has internet access!

Run the following command to look at your Gateway's bank state:

```find /proc/banktable -type f -print -exec cat {} ';'```

It should look something like this:

```bash
/proc/banktable/notbootedoid
<not important>
/proc/banktable/bootedoid
<not important>
/proc/banktable/passiveversion
<not important>
/proc/banktable/activeversion
<not important>
/proc/banktable/inactive
bank_2
/proc/banktable/active
bank_1
/proc/banktable/notbooted
bank_2
/proc/banktable/booted
bank_1
```

!!! caution "Bank Planning: "On which bank should I stay to be safe?""
    It's strongly recommended to adhere to the above situation before following this guide further. The bigger picture description can be found [here](https://github.com/Ansuel/tch-nginx-gui/issues/514). The short thing is that you should really be on a `Type 2` image booted from `bank_1` now, and then you should only mod your preferred firmware version (not necessarily of `Type 2`) while booted from `bank_2`.
    **Key Point**: it's unsafe to deeply mod firmware settings of any firmware booted from `bank_1`.

These gateways use two flash partitions (`bank_1` and `bank_2`) which can be upgraded/used almost independently.

They are signature checked before boot so you can't flip a single bit of the base firmware image in either bank if you want to see your device booting. The whole config and customized stuff is stored in the matching folder within the [overlay filesystem](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/overlayfs.txt), i.e. `/overlay/bank_2`

!!! hint
    You can see your modified config files in `/overlay` if you want to backup stuff or see what changes you made, however, all original versions of modified files are stored permanently in `/rom`, in case you would like to revert something back.

When a proper Reset to Factory Defaults is done, the overlay partition is not formatted, just the relevant `/overlay/bank_*` partition is deleted. You can learn more on such aspects by reading the [Recovery](/Recovery) page.

Let's rule out an awful, surprise sad ending. Run this command *now* to ensure this guide will work as expected:

```bash
cat /proc/banktable/booted > /proc/banktable/active
```

Unless your target preferred firmware is there already, it's now time to flash it into its final destination: the `notbooted` bank.
This time you can't use AutoFlashGUI, even if your current firmware is `Type 2`. Otherwise the regular firmware upgrade procedures will perform an unwanted switchover, leading to a reboot immediately before any indirect root could be performed.

To decide what procedure you should use for flashing, you must know what bank is the `notbooted` one. You can find this by running `cat /proc/banktable/inactive`.

- If you are still following the **not recommended** bank planning and your `notbooted` bank is `bank_1`, well, you will need to go with BOOT-P flashing. After reboot you will still be on your rooted/rootable `Type 2` firmware. However, if your preferred firmware is not available as RBI file, you can't continue this way. If not, go with [BOOT-P flashing](/Recovery/#boot-p-recovery-mode-tftp-flashing) then come back here and continue reading.

- If you are following the **recommended** bank planning and your `notbooted` bank is `bank_2`, you will now need to [decrypt and extract](/Resources/#decrypting-firmware) the raw bank image from the RBI firmware file and [flash it manually](/Resources/#backuprestore-bit-for-bit-dumps) into the right bank - it's easier and faster then BOOT-P. Is your preferred firmware available as raw bank dump already? You just saved some good amount of fun ... and time. Is the OSCK for your device model unknown? You have root access right now on the current `Type 2` firmware, so get it, **share it**, and use it. Come back here and continue reading when you are done.

Welcome back! Are you enjoying so far?

Now, run the following to prepare inactive bank for temporary root and switch back to it:

```bash
rm -rf /overlay/`cat /proc/banktable/inactive`
mkdir /overlay/`cat /proc/banktable/inactive`
chmod 755 /overlay/`cat /proc/banktable/inactive`
mkdir /overlay/`cat /proc/banktable/inactive`/etc
chmod 775 /overlay/`cat /proc/banktable/inactive`/etc
echo -e "echo root:root | chpasswd
sed -i '\''s#root:/bin/false#root:/bin/ash#'\'' /etc/passwd
sed -i '\''s/#//'\'' /etc/inittab
dropbear -p 6666 &
" >> /overlay/`cat /proc/banktable/inactive`/etc/rc.local
chmod +x /overlay/`cat /proc/banktable/inactive`/etc/rc.local
sync
cat /overlay/`cat /proc/banktable/inactive`/etc/rc.local
```

You should get this output from the last command:

```bash
echo root:root | chpasswd
sed -i '\''s#root:/bin/false#root:/bin/ash#'\'' /etc/passwd
sed -i '\''s/#//'\'' /etc/inittab
dropbear -p 6666 &
```

If you didn't, reboot the Gateway and retry the procedure.

If successful, nuke the `Type 2` firmware from inside booted bank with:

```bash
mtd erase `cat /proc/banktable/inactive`
```

Then reboot and wait 3 to 4 minutes for the Gateway to boot into this "new" rooted bank. It will fail three attempts to boot from the empty active bank, then it will load your firmware from the inactive one.

!!! hint "Something went Wrong?"
    Flash back the same `Type 2` image you were up to now, following the [BOOT-P recovery](/Recovery/#boot-p-recovery-mode-tftp-flashing) guide. If you followed the initial advice about bank planning, you will be back on the exact situation you were before the last command. Otherwise, you will likely need to solve a typical *soft-brick* issue: prepare some extra luck, perform a [RTFD](/Recovery/#reset-to-factory-defaults-rtfd) and then restart over from the beginning.

Now you have temporary root access on your preferred firmware, you can now jump below to set your own root access [password](#change-the-root-password).

### Change the Root Password

!!! warning "Serious hint!"
    Do not ignore this step! :)

Run:

```bash
passwd
```

Reboot now if you're not doing any further configuration.

At this point you should now read below to set up permanent SSH access

### Setting up Permanent SSH Server

Run these commands to setup a permanent SSH access on port `22` by defining a new dropbear instance:

```bash
uci add dropbear dropbear
uci rename dropbear.@dropbear[-1]=afg
uci set dropbear.afg.enable='1'
uci set dropbear.afg.Interface='lan'
uci set dropbear.afg.Port='22'
uci set dropbear.afg.IdleTimeout='600'
uci set dropbear.afg.PasswordAuth='on'
uci set dropbear.afg.RootPasswordAuth='on'
uci set dropbear.afg.RootLogin='1'
uci commit dropbear
/etc/init.d/dropbear enable
/etc/init.d/dropbear restart
```

Now you must harden your access, to prevent it from being lost via a Firmware Upgrade in future. See below.

### Hardening Gained Access

Run the following in the SSH terminal to prevent your Gateway loosing root access unexpectedly.

!!! hint "Pick only what you need"
    You can paste each block directly into the terminal independently, use only ones your firmware needs. If you don't know, just paste them all. It is very unlikely that it will break your gateway.

```bash
# Disable CWMP
uci delete cwmpd.cwmpd_config
uci delete firewall.cwmpd
uci del_list watchdog.@watchdog[0].pidfile='/var/run/cwmpd.pid'
uci del_list watchdog.@watchdog[0].pidfile='/var/run/cwmpevents.pid'
uci commit
/etc/init.d/cwmpd disable
/etc/init.d/cwmpd stop
/etc/init.d/cwmpdboot disable
/etc/init.d/cwmpdboot stop
/etc/init.d/zkernelpanic disable
/etc/init.d/zkernelpanic stop
# Disable CWMP - extra, in case you think it may resurrect
uci set cwmpd.cwmpd_config.state=0
uci set cwmpd.cwmpd_config.acs_url='https://127.0.1.1:7547/'
uci set cwmpd.cwmpd_config.use_dhcp=0
uci set cwmpd.cwmpd_config.interface=loopback
uci set cwmpd.cwmpd_config.enforce_https=1
uci commit cwmpd
# Disable Telstra monitoring
uci delete tls-vsparc.Config
uci delete tls-vsparc.Passive
uci delete autoreset.vsparc_enabled
uci delete autoreset.thor_enabled
uci delete wifi_doctor_agent.acs
uci delete wifi_doctor_agent.config
uci delete wifi_doctor_agent.as_config
uci commit
# Disable Telstra Air/Fon WiFi
/etc/init.d/hotspotd stop
/etc/init.d/hotspotd disable
uci delete dhcp.hotspot
uci delete dhcp.fonopen
uci commit
# Remove any ISP ssh access pubkey
echo > /etc/dropbear/authorized_keys
# Completely disable SSH access over wan
uci set dropbear.wan.enable='0'
uci commit
# Free space for gateways with small flash
opkg --force-removal-of-dependent-packages remove conf-cwmpd cwmpd autoreset-tch mappings-fon geolocation-tch
find /rom/usr/lib/ipk -type f |xargs -n1 basename | cut -f 1 -d '_' |xargs opkg --force-removal-of-dependent-packages remove
# Clear startup script DO NOT MISS!!!
echo > /etc/rc.local
```

**Now you can Move on to [Unlocking Functionality](/Unlock%20Functionality)**

### My Firmware is so Old that AutoFlashGUI can't Authenticate

*This is because they changed the web authentication method to SRPv6 with firmware v15, and this is the only method that the AutoFlashGUI tool knows how to authenticate with.*

You are going to have to flash a newer (let's say v16.3) RBI file via `sysupgrade` after using the original manual procedure to get a shell.

Go to *Advanced > Diagnostics*, and click on the *Ping & Traceroute* tab. (If your Gateway doesn’t display the Diagnostics tile, factory reset the Gateway. This only happens when the config is corrupted.) In the IP address section, enter your Gateway's IP and run:

```bash
:::::::;echo root:root | chpasswd; dropbear -p 6666;
```

Give it 30 seconds to generate SSH host keys and then try to SSH into your Gateway on port 6666 with root/root.

Copy the RBI to a USB stick (FAT32 formatted is most likely to work on old firmware) and insert it into the Gateway's USB port.

If you type `cd /mnt/` and keep hitting tab it should eventually get to the end of the USB stick path, then hit enter. (You can also run `mount` and try to work out the path the USB stick is mounted on.)

To be on the on the safe side we will copy the RBI to RAM, then flash it. Do the following with the correct RBI file name (keeping in mind that this is case sensitive):

```bash
cp filename.rbi /tmp
cd /tmp
sysupgrade filename.rbi
```

All things going well you should see it progress along and reboot, then you can commence the current procedure.
