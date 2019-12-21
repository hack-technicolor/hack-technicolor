# Safe Firmware Upgrade

This simple guide will show you how to change your rooted Gateway firmware avoiding or handling any possible issues. If your Gateway is not rooted or you don't know what *rooting* is about, go to Home page.

This is the way you should regularly install firmware upgrades when available. Firmware flashing via *sysupgrade* or *BOOTP* is not safe as it will remove root access.

This method will use direct partition writing to flash the firmware exactly where it needs to be and to guarantee root. Read [here](../Resources/#different-methods-of-flashing-firmwares) for extra details about different flashing methods.

## Get prepared

What you will need:

1. A rooted Gateway in working order

2. The firmware image to flash, either RBI file or raw bank dump
    - Pick one for your model, of whatever *Type*, from the [Firmware Repository](../Firmware%20Repository/)

3. Make sure you can eventually get a copy of your current firmware
    - Check if it's available from [Firmware Repository](../Firmware%20Repository/)

4. A way to access this documentation in case of issues
    - If this is your main Gateway, a mobile internet connection is recommended

5. Your current bank planning. Check and take note of firmware flashed, *active* and *booted* banks after running:
`find /proc/banktable -type f -print -exec cat {} ';'`

## Things to know

Will root access will be preserved?
  - Well, that is the point.

On which bank will the new firmware be flashed?
  - The booted one, the current firmware will be overwritten.

Will the upgrade affect my bank planning?
  - No it won't, there won't be any bank switches.

Will any setting and customization be lost?
  - It depends on the firmware you want to flash, read further.

## Preparing Firmware

Check the file format your new firmware is. It could be either an RBI file or a raw bank dump.

### RBI file

Take the RBI file to flash and move it to `/tmp/new.rbi` by SCP or USB drive. Run this command to unpack the RBI image, will take a while:

```bash
cat "/tmp/new.rbi" | (bli_parser && echo "Please wait..." && (bli_unseal | dd bs=4 skip=1 seek=1 of="/tmp/new.bin"))
```

### Raw bank dump

Download **and extract** the raw bank image, and move this file into `/tmp/new.bin` folder by SCP or USB drive.

## Preserving root access

It is **not recommended** to keep custom changes to files and configs if you are either downgrading or moving to a firmware of a different brand.

If you are just upgrading to a newer firmware of the same brand you can try the easy (*not the **safest***) way by skipping this section and jumping [over](#flashing-firmware). In this section you have required steps to keep root access only.

Make a full backup of your bank configuration:

```bash
tar -C /overlay -cz -f /tmp/backup-$(date -I).tar.gz bank_1 bank_2
```

Move the backup to your PC by SCP or USB drive. Make sure you can open the backup archive and keep it in a safe place.

```bash
rm -rf /overlay/`cat /proc/banktable/booted`
mkdir -p /overlay/`cat /proc/banktable/booted`/etc
chmod 755 /overlay/`cat /proc/banktable/booted` /overlay/`cat /proc/banktable/booted`/etc
echo -e "echo root:root | chpasswd
sed -i 's#/root:.*\$#/root:/bin/ash#' /etc/passwd
sed -i 's/#//' /etc/inittab
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
rm /overlay/`cat /proc/banktable/booted`/etc/rc.local
" > /overlay/`cat /proc/banktable/booted`/etc/rc.local
chmod +x /overlay/`cat /proc/banktable/booted`/etc/rc.local
```

Note that your ssh credentials will be changed back to `root:root`.

## Flashing firmware

Run this command to write `/tmp/new.bin` image into `booted` bank:

```bash
mtd write "/tmp/new.bin" $(cat /proc/banktable/booted)
```

Reboot the Gateway now.

## Completing setup

The Gateway should boot normally into the new firmware. You should still have root access at least. Make sure everything will be fine: read [Hardening Root Access](../Hardening%20Root%20Access/).
