# Safe Upgrade for pkgtb Firmware

This simple guide will show you how to clean-up your rooted Gateway modifications and safely change firmware avoiding or handling any possible issues, as well as preserving existing root access. If your Gateway is not rooted already or you don't know what *rooting* is about, go to [Home page](../).

This is the way you should regularly clean-up your modifications and install firmware upgrades when available.

This method will use *sysupgrade* to flash the pkgtb firmware file into the passive bank and then root the passive bank before switching. Read [here](../Resources/#different-methods-of-flashing-firmwares) for extra details about different flashing methods.

!!! hint "Safest and Easiest Method"
    The safest and easiest method for flashing pkgtb firmware to your device is to use the [safe-firmware-upgrade](https://github.com/seud0nym/tch-gui-unhide/tree/master/utilities#safe-firmware-upgrade) script. It not only automates this procedure, it provides many options for preserving and/or setting important configuration.

## Get prepared

What you will need:

1. A rooted Gateway in working order

2. Make sure that you are booting from a firmware bank that contains a `Type 2` firmware that can be easily rooted

2. Make sure you can eventually get a copy of your current firmware
    - Check if it's available from [Firmware Repository](../Repository/)

3. A way to access this documentation in case of issues
    - If this is your main Gateway, a mobile internet connection is recommended

4. Your current bank planning. Run the following commands (or use [show-bank-plan](https://github.com/seud0nym/tch-gui-unhide/tree/master/utilities#safe-firmware-upgrade)):  
`bootmgr partition notbooted;bootmgr partition passive | grep -v ^rd_metadata`
`uci show env.var | grep friendly_sw_version`

5. The firmware image to flash, either the pkgtb file or ubifs bank dumps of the bootfs and rootfs ubi devices
    - Pick one for your model, of whatever *Type*, from the [Firmware Repository](../Repository/)

## Things to know

##### Will root access be preserved?
  - Well, that is the point of this guide, however we can't guarantee root access preservation won't break in future firmwares.

##### On which bank will the new firmware be flashed?
  - The not-booted passive bank, and the currently installed firmware will *not* be overwritten. Make sure the firmware in the passive bank is listed in our [Repository](../Repository/) before overwriting!

##### Will the upgrade affect my bank planning?
  - The firmware will be flashed into the passive, not-booted bank.

##### Will any setting and customization be lost?
  - It depends on whether you wish to switch to the new firmware after flashing. If not, then no.

## Switch Banks If Necessary

If the active firmware is *not* a `Type 2`, and the not-booted bank *does* contain a rooted `Type 2` firmware, then you should switch to that bank before starting.

```bash
bootmgr switch_over $(bootmgr partition notbooted)
reboot
```

## Backup the Overlay

Make a full backup of your passive firmware overlay:

```bash
tar -C /overlay -cz -f /tmp/backup-$(date -I).tar.gz bank_$(bootmgr partition notbooted)
```

Move the backup to your PC by SCP or USB drive. Make sure you can open the backup archive and keep it in a safe place.

Please note, importing back this full backup on the new firmware is dangerous. This will come handy in future whenever you go back to the old firmware, or if you want to check how the old firmware was configured.

## Preparing Firmware

Check the file format your new firmware is. It could be either a PKGTB file or two ubifs bank dumps (the bootfs and rootfs partitions).

### PKGTB file

Take the PKGTB file to flash and move it to `/tmp/new.pkgtb` by SCP. Here is an example from WinSCP, but you can use any SCP client.

![WinSCP firmware upload](../images/winscp_pkgtb_upload.png)

### ubifs bank dumps

Download **and extract** the ubifs bootfs and rootfs images, and move these files into `/tmp/bootfs.bin` and `/tmp/rootfs.bin` on the device by SCP or USB drive.

## Flashing firmware

### PKGTB file

Run these commands to write `/tmp/new.pkgtb` firmware into the `notbooted` bank:

```bash
sysupgrade -n -v --no-reboot /tmp/new.pkgtb
rm -f /overlay/data.remove_due_to_upgrade /overlay/sysupgrade.bank.switchover
[ -d /overlay/bank_$(bootmgr partition notbooted).remove_due_to_upgrade] && mv /overlay/bank_$(bootmgr partition notbooted).remove_due_to_upgrade /overlay/bank_$(bootmgr partition notbooted)
```

### ubifs bank dumps

Run these commands to write `/tmp/bootfs.bin` and `/tmp/rootfs.bin` images into the `notbooted` bank:

```bash
for dev in $(ls /dev/ubi*_* | grep -v 'ubi_ctrl\|ubiblock'); do
  name=$(ubinfo $dev | grep "Name:" | tr -s ' ' | cut -d' ' -f2)
  if [ "$name" = "bootfs$(bootmgr partition notbooted)" ]; then
    bootfs=$dev
  elif [ "$name" = "rootfs$(bootmgr partition notbooted)" ]; then
    rootfs=$dev
  fi
done
# Erase the devices
ubiupdatevol $bootfs -t
ubiupdatevol $rootfs -t
# Write the images
ubiupdatevol $bootfs /tmp/bootfs.bin
ubiupdatevol $rootfs /tmp/rootfs.bin
```

## Clean-up

It is **recommended** to clean-up every change to files and configs whenever you are either downgrading or moving to a firmware of a different brand.

If you are just flashing a minor firmware update of the same brand, you could take the short (and **unsafe**) path by skipping over to [Preserving root access](#preserving-root-access). Please note, if anything goes wrong or you experience any issues, this will almost certainly be the culprit.

Run the command below to completely reset the overlay for the not-booted bank:

```bash
rm -rf /overlay/bank_$(bootmgr partition notbooted)
```

The above command cleans up the same files a regular RTFD would. We need to prepare a couple more things before rebooting, that's why we didn't use RTFD.

!!! warning "Don't stop here!"
    Your gateway's not-booted bank is now completely **clean** and reset to factory defaults, but right now SSH root access is *not* enabled!. You should **really** keep the getaway on and proceed to the next step to avoid loosing root access.

## Preserving root access

The below block of commands prepares a run-once root access setup script to be executed on the *next* boot. This is equivalent to redoing the entire hacking [from scratch](../) as if your gateway were never rooted before.

Run the following set of commands:

> *please note there is a long multi-line command here, paste it all at once*

```bash
mkdir -p /overlay/bank_$(bootmgr partition notbooted)/etc
chmod 755 /overlay/bank_$(bootmgr partition notbooted) /overlay/bank_$(bootmgr partition notbooted)/etc
echo -e "echo root:root | chpasswd
sed -i 's#/root:.*\$#/root:/bin/ash#' /etc/passwd
sed -i -e 's/#//' -e 's#askconsole:.*\$#askconsole:/bin/ash#' /etc/inittab
uci -q set \$(uci show firewall | grep -m 1 \$(fw3 -q print | \
egrep 'iptables -t filter -A zone_lan_input -p tcp -m tcp --dport 22 -m comment --comment \"!fw3: .+\" -j DROP' | \
sed -n -e 's/^iptables.\+fw3: \(.\+\)\".\+/\1/p') | \
sed -n -e \"s/\(.\+\).name='.\+'$/\1/p\").target='ACCEPT'
uci add dropbear dropbear
uci rename dropbear.@dropbear[-1]=afg
uci set dropbear.afg.enable='1'
uci set dropbear.afg.Interface='lan'
uci set dropbear.afg.Port='22'
uci set dropbear.afg.IdleTimeout='600'
uci set dropbear.afg.PasswordAuth='on'
uci set dropbear.afg.RootPasswordAuth='on'
uci set dropbear.afg.RootLogin='1'
uci set dropbear.lan.enable='0'
uci commit dropbear
/etc/init.d/dropbear enable
/etc/init.d/dropbear restart
rm /overlay/bank_$(bootmgr partition notbooted)/etc/rc.local
source /rom/etc/rc.local
" > /overlay/bank_$(bootmgr partition notbooted)/etc/rc.local
chmod +x /overlay/bank_$(bootmgr partition notbooted)/etc/rc.local
sync
bootmgr switch_over $(bootmgr partition notbooted)
reboot
```

!!! hint "Clean and rooted"
    The passive bank of your gateway is now clean but will re-enable permanent root SSH access on the next boot. Please note, your SSH credentials will be changed back to `root:root`.

Wait for your device to reboot completely.

## Completing setup

The Gateway should boot normally into the new firmware. Please review the following:

- Your device has switched banks and you are running the firmware version you just flashed.
- You should still have permanent SSH server on port `22`.
- Your root credentials have been reset to `root:root`. Make sure you [change password](../Hacking/PostRoot/#change-the-root-password) now.

!!! fail "Something went wrong?"
    Your device should automatically revert to the original firmware in case of boot failure caused by bad firmware flashing. If you end up without root on the new firmware, then as long as you followed the preparations correctly and your original bank contains a `Type 2` rootable firmware, then you can follow the [change booted bank](../Recovery/#change-booted-bank) instructions to get back to a rootable firmware.
