## IMPORTANT - Leave gateway turned off until you understand these instructions.

!!! warning "Disclaimer"
    This process is not supported by the manufacturer or supplier of your modem. There is no way of knowing your situation and the process could break your modem or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Things you will need

!!! hint
    You need the following **before** you go offline

1. The latest version of the AutoFlashGUI software, available from GitHub either as a  [ZIP file](https://github.com/mswhirl/autoflashgui/archive/master.zip) or the source code at [the project page](https://github.com/mswhirl/autoflashgui). 
*Make sure the tool runs and GUI loads before you go offline!*

2. The RBI [firmware](/Firmware%20Repository/) file of a `Type 2` version comapatible with your gateway.

3. **Optionally**, the RBI [firmware](/Firmware%20Repository/) file for the firmware version you would like to stay at the end on your gateway, like a newer one or some old one you feel more stable and comfortable with.

4. An SSH and SCP client - the famous [PuTTY](https://www.chiark.greenend.org.uk/%7Esgtatham/putty/) is fine for SSH in Windows. [WinSCP](https://winscp.net/eng/download.php) is recommanded for SCP, but PuTTY has an SCP client as well. If you have any WSL distribution installed, or you run a native Unix OS you have both SSH and SCP cli clients available already.

5. A copy of this documentation for reference while you're offline. Just keep a tab open in your browser from a mobile device or print/export this someway. (if you know how MkDocs work you could also clone this repo and render it locally by yourself)

6. Physical access to the gateway so you can power cycle it and unplug the WAN/DSL cable while you're going through this process.

7. A *happy* gateway! If it's in bridge mode or half the tiles are missing (in the GUI), or it simply is not working as expected, just [recover it](/Recovery) to a proper functional state first.

## Introduction

### Known Working Models

 | Model Number    | Mnemonic | ISP's own Commercial Names
 |:---------------:|:--------:|:--------------------------
 | TG797n v3       | DANT-O   | Telstra T-Gateway
 | TG789vac v2     | VANT-6   | -
 | TG799vac        | VANT-F   | Telstra Gateway Max
 | TG789vac (v1)   | VANT-D   | -
 | TG800vac        | VANT-Y   | Telstra Gateway Max 2
 | TG789vac v3     | VBMT-1   | -
 | TG799vac Xtream | VBNT-H   | -
 | DJN2130         | VBNT-J   | Telstra Frontier Gateway
 | TG789vac v2 HP  | VBNT-L   | -
 | DJA0231         | VCNT-A   | Telstra Smart Modem Gen2

!!! tip "Not sure which one is yours?"
    Avoid referring to your device by its commercial product name, refer to your device with its unique board mnemonic identifier `XXXX-X` to avoid any potential ambiguity.

### The Basics

Devices mentioned above and similar ones are very capable pieces of equipment, each with different features, which may include: 802.11ac, MU-MIMO, ADSL2/VDSL2/eVDSL modem, DECT base station, [FXS](https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station) ports, [FXO](https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station) port,  4G backup, [SFP](https://en.wikipedia.org/wiki/Small_form-factor_pluggable_transceiver) slot, etc.
They are known to have a high quality internal PCB and low power consumption, for example the TG799vac Xtream uses about 12 watts with WiFi on (typical router config) and 9 watts with WiFi off (typical bridge mode config).

The guide was originally written for gateways provided by Telstra and as such, have Telstra branded firmware.

Usually, there is no ‘generic’ firmware available that will *just* give you access to the gateway as any other device you would purchase. This kind of sucks because if you decide to use this device with different ISP, you are likely to be blocked fomr doing that, or simply loose some functionality like VoIP, DECT base station, FXS/FXO ports, mobile backup or something else.

That's what should motivate you to hack your device and at least re-enable as many features as possible. For some small set of devices, an alternative no-brand firmware (MST) exists, where no configurations options are locked out, but getting root access to it will still open a wider window of possibilities.

The default IP address of the gateway varies by gateway model, it could be `10.0.0.138`, `192.168.0.1`, `192.168.1.1`, `10.1.1.1` and so on. Your best option is to get an IP address by DHCP the first time you connect and see what your default gateway gets assigned to.

## Gaining Root Access

!!! caution "Go offline NOW!"
    The ISP could lock you out of the gateway by pushing a firmware update or configuration script through a landline, WiFi or SIM card connection, until the gateway is rooted and remote management disabled.

Ensure the gateway does not have a wired or wireless internet connection. Gateways with 4G Backup, such as the DJA/DJN Series, must also have the SIM removed from under the bottom 25mm x 25mm white plastic sticker. On the DJA0231, the SIM is under a small rubber plug above the green port.

!!! info
    These instructions were built for the TG799vac, so if you are doing this for a different gateway be sure to substitute the correct firmware files and change the other options as needed.

### Type 1 - Easy flash of Type 2, then Rooting

In this example we work with `VANT-F` gateway, `16.3.7567` is the `Type 2` firmware we need to flash, `17.2.0261` is the `Type 1` firmware we are currently on.

Run up the AutoFlashGUI tool and flash the `Type 2` firmware to your gateway, `vant-f_CRF687-16.3.7567-660-RG.rbi`, and allow it to finish flashing and rooting.

!!! warning "Make sure SSH is permanent"
    If AutoFlashGUI does not know how to set permanent root access on your model it will spawn a temporary SSH dropbear instance on port `6666`. You should now configure dropbear in order to run a permanent lan-side SSH server. Read below [permanent ssh](#setting-up-permanent-ssh-server) section, then come back here.

Fire up your SSH client and connect with user `root` to the gateway IP on default port `22`, or `6666`.

At this point you have a rooted `Type 2` image on your gateway to play with. Would you like to upgrade back to a newer firmware without loosing root access? Fine, jump over to [inactive bank pre-rooting](#root-inactive-bank). Continue reading here otherwise.

Now proceed to setting your own root access [password](#change-the-root-password).

### Type 2 - Direct Rooting

In this example we work with `VANT-F` gateway, `16.3.7567` is the `Type 2` firmware.

Using AutoFlashGUI, find or fill-up your gateway settings, allow it to run through getting root.

![16.3 AFG](images/flashgui_16.3.png)

If you are unable to fill your profile correctly or AutoFlashGUI it's not working, search communities for detailed model-specific root commands and report back your issues. Being a `Type 2` image, a working root guide exists for sure.

!!! warning "Make sure SSH is permanent"
    If AutoFlashGUI does not know how to set permanent root access on your model it will spawn a temporary SSH dropbear instance on port `6666`. You should now configure dropbear in order to run a permanent lan-side SSH server. Read below [permanent ssh](#setting-up-permanent-ssh-server) section, then come back here.

Fire up your SSH client and connect with user `root` to the gateway IP on default port `22`, or `6666`.

At this point you have a rooted `Type 2` image on your gateway to play with. Would you like to upgrade back to a newer firmware without loosing root access? Fine, jump over to [inactive bank pre-rooting](#root-inactive-bank). Continue reading here otherwise.

Now proceed to setting your own root access [password](#change-the-root-password).

### Type 3 - Hard flash of Type 2, then Rooting

!!! info "Where you come from??"
    Do not cheat, restart reading from the [index of this wiki](/). See you later!

## Post-root procedures

### Root inactive bank

At this point you are ready to activate root on whatever *Type* of firmware you would like to end up having rooted, and finally switch over to it.

 This procedure works by allowing us to mod the not booted bank and config, then switch over to it without doing a factory reset or standard upgrade procedure. Note that if you factory reset while not on `Type 2` you will need to run the entire procedure from the beginning and an eventual auto-upgrade could lock you out permanently in that reset state if it has internet access!

Run the following command to look at your gateway's bank state:

```find /proc/banktable -type f -print -exec cat {} ';'```

It should look something like this:

```
/proc/banktable/notbootedoid
____don't care_____
/proc/banktable/bootedoid
____don't care_____
/proc/banktable/passiveversion
____don't care_____
/proc/banktable/activeversion
____don't care_____
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
    It's strongly recommennded to adhere to the above situation before continue following this guide. The bigger picture description can be found [here](https://github.com/Ansuel/tch-nginx-gui/issues/514). The short thing is that you should really be on a `Type 2` image booted from `bank_1` now, and then you should only mod your preferred firmware version (not necessarily of `Type 2`) booted from `bank_2`. Keypoint: it's unsafe to deeply mod firmware settings of any firmware booted from `bank_1`.

These gateways use two flash partitions (`bank_1` and `bank_2`) which can be upgraded/used almost independently.

They are signature checked before boot so you can't flip a single bit of the base firmware image in both banks if you would see your device booting from there. The whole config and customized stuff is stored into the matching folder within the [overlay filesystem](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/overlayfs.txt), i.e. `/overlay/bank_2`

!!! hint
    You can see your modified config files in `/overlay` if you want to back stuff up or see what changes you made. Conversely, all original versions of modified files are stored permanently in `/rom`, in case you would like to revert something back.

When a proper Reset To factory Default is done, the overlay partition is not formatted, just the relevant `/overlay/bank_*` partition is deleted. You can learn more on such aspects reading [Recovery](/Recovery) page on this wiki.

Let's rule out an awful surprising sad ending: run this command *now* to make sure booted and active banks coincide - they should already, but...
```bash
cat /proc/banktable/booted > /proc/banktable/active
```

Unless your target preferred firmware is there already, it's now time to flash it into its ultimate destination: the `notbooted` bank.
This time you can't use AutoFlashGui, even if your current firmware is of `Type 2`, otherwise the regular firmware upgrade procedures will perform an unwanted switchover and will reboot the gateway immediately before any indirect root could be performed. So let's distinguish the two different cases:

- You love the dark side. If you are still following the **not recommended** bank planning, and your `notbooted` bank is `bank_1`, well, you just need to go with BOOT-P flashing. After reboot you will still be there on your rooted/rootable `Type 2` firmware, ready to continue reading. However, if your preferred firmware has no available RBI file but is only available as raw bank dump you can't continue this way. So, go with [BOOT-P flashing](/Recovery/#boot-p-recovery-mode-tftp-flashing) then come back here and continue reading.
- You are on the right side. If you are following the **recommended** bank planning, and your `notbooted` bank is `bank_2` you will now need to [decrypt and extract](/Resources/#decrypting-firmware) the raw bank image from the RBI firmware file and [flash it manually](/Resources/#backuprestore-bit-for-bit-dumps) into the right bank - it's easier and faster then BOOT-P, actually. Is your preferred firmware available as raw bank dump already? You just saved some good amount of fun ... and time. Is the OSCK for your device model unknown? You have root access right now on the current `Type 2` firmware, so get it, **share it**, and use it. Come back here and continue reading when you are done.

*15 minutes later*

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
If you didn't, reboot the modem and retry the procedure.

If sucessful, nuke the `Type 2` firmware from inside booteed bank with:
```bash
mtd erase `cat /proc/banktable/inactive`
```

then reboot and wait 3 to 4 minutes for the gateway to boot into this "new" rooted bank. It will fail three attempts to boot from the empty active bank, then it will load your firmware from the inactive one.

!!! hint "Something went wrong?"
    Fash back the same `Type 2` image you were up to now, following [BOOT-P recovery](/Recovery/#boot-p-recovery-mode-tftp-flashing). If you followed the initial advice about bank planning, you will be back on tha seme exact situation you were before the last above command. Otherwise, you will likely need to solve a typical *soft-brick* issue: prepare some extra luck, perform a [RTFD](/Recovery/#reset-to-factory-defaults-rtfd) and then restart over from the beginning

Now you have some temporary root access into your preferred firmware. Just conclude all this long trip by reading below section for [permanent ssh](#setting-up-permanent-ssh-server) setup.

### Change the Root Password

!!! hint "Serious hint!"
    Do not ignore this step! :)

Run:

```bash
passwd
```

Reboot now if you're not doing any further configuration.

At this point you should now be able to SSH in with root and your password (which should no longer be 'root'!)

### Setting up permanent SSH server

!!! info "WIP"

### Hardening gained access

Run the following in the SSH terminal to prevent your gateway loosing root access unexpectedly.

!!! hint "Pick only what you need"
    You can paste each block directly into the terminal indipendently, use only that ones your firmware needs, keep matching your actual settings paths otherwise they will have no effect.

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
# Disable telstra monitoring
uci delete tls-vsparc.Config
uci delete tls-vsparc.Passive
uci delete autoreset.vsparc_enabled
uci delete autoreset.thor_enabled
# Remove any ISP ssh access pubkey
echo > /etc/dropbear/authorized_keys
# Completely disable SSH access over wan
uci set dropbear.wan.enable='0'
```

### My firmware is so old that AutoFlashGUI can't authenticate!

*This is because they changed the web authentication method to SRPv6 with firmware v15, and this is the only method that the AutoFlashGUI tool knows how to authenticate with.*

You are going to have to flash a newer (let's say v16.3) RBI file via `sysupgrade` after using the original manual procedure to get a shell.

Go to *Advanced > Diagnostics*, and click on the *Ping & Traceroute* tab. (If your gateway doesn’t display the Diagnostics tile, factory reset the gateway. This only happens when the config is corrupted.) In the IP address section, enter your gateway's IP and run:

```bash
:::::::;echo root:root | chpasswd; dropbear -p 6666;
```

Give it 30 seconds to generate SSH host keys and then try to SSH into your gateway on port 6666 with root/root.

Copy the RBI to a USB stick (FAT32 formatted is most likely to work on old firmware) and insert it into the gateway's USB port.

If you type `cd /mnt/` and keep hitting tab it should eventually get to the end of the USB stick path, then hit enter. (You can also run `mount` and try to work out the path the USB stick is mounted on.)

To be on the on the safe side we will copy the RBI to RAM, then flash it. Do the following with the correct RBI file name (keeping in mind that this is case sensitive):

```bash
cp filename.rbi /tmp
cd /tmp
sysupgrade filename.rbi
```

All things going well you should see it progress along and reboot, then you can commence the current procedure.
