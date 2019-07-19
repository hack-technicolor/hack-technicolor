# Resources

## IMPORTANT, do not SKIP

**Warning:** This process is not supported by the manufacturer or supplier of your modem.

There is no way of knowing your situation and the process could break your modem or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## What tools can I use to administer OpenWrt from a Windows computer

There are a number of tools such as cmder, SmarTTY, PuTTY, and WinSCP as described in the [OpenWRT SSH Administration for Newcomers](https://openwrt.org/docs/guide-quick-start/sshadministration) page.

## Handy Commands

* `find /proc/banktable -type f -print -exec cat {} ';'`
  * Checking firmware flashed and what is active.

* `ps`
  * Shows processes that are running.

* `netstat -tuplen`
  * Shows programs that are listening as network services.

* `netstat -lenp`
  * Shows everything that's listening on sockets (TCP, UPD, Unix etc).

* `df -h`
  * Free (NAND) space.

* `uci show`
  * Dump entire config (~7700+ lines to console).

* `uci show | grep password`
  * Example to filter lines with password.

* `logread -f`
  * Access logs for most services (which use syslog). Pass an argument of -e nginx to match log entries just related to Nginx, which is perfect for debugging errors in the Web GUI.

  * Remove `-f` flag for all time logs (erased every reboot).

* `for F in /etc/init.d/* ; do $F enabled && echo $F on || echo $F **disabled**; done`
  * Display status of all init.d scripts.

* `/rom/usr/lib/cwmpd/transfers/switchover.sh`
  * **UNSAFE** Switch active bank and reboot.

* `echo bank_1 > /proc/banktable/active`
  * Set bank_1 as active, replace with `bank_2` for the opposite

* `cat /etc/openwrt_release`
  * OpenWrt Release metadata.
  * eg TG799:

```bash
DISTRIB_ID='OpenWrt'
DISTRIB_RELEASE='Chaos Calmer'
DISTRIB_REVISION='r46610'
DISTRIB_CODENAME='chaos_calmer'
DISTRIB_TARGET='brcm63xx-tch/VANTF'
DISTRIB_DESCRIPTION='OpenWrt Chaos Calmer 15.05.1'
DISTRIB_TAINTS='no-all busybox'
```

## Files

* `/www/*`
  * Lua/HTML Web Interface source files.

* `/etc/config/*`
  * UCI config source files, pehaps more readable than `uci show`.

* `/sbin/*.sh, /usr/bin/*.sh, /usr/sbin/*.sh`
  * Various executables, many custom-written for this hardware.

* `/etc/init.d/*`
  * Services present; May or may not be enabled or running.

## LED's

[Directly accessing /sys/class/leds is a BAD practice...](https://github.com/davidjb/technicolor-tg799vac-hacks/issues/6#issue-388905312)

* `ls -1 /sys/class/leds/`
  * List available LED's.

* `cat /sys/class/leds/<led>:<colour>/trigger`
  * Shows the triggers available and the current trigger.
  * Replace LED with the name of the LED and colour with the colour, eg. `cat /sys/class/leds/dect:green/trigger`

* `echo "default-on" > /sys/class/leds/power:green/trigger`
  * Reset trigger to default.

* `opkg list | grep led`
  * List all LED packages used.

Examples:

Turn on LED:
`echo 1 > /sys/class/leds/power:green/brightness`

Turn off LED:
`echo 0 > /sys/class/leds/power:red/brightness`

## Backing up Configuration

Your a Super Modder. You flash your modem on a daily basis.

To save the Config:

* `sysupgrade -i -b filename.tar.gz`

To restore the Config:

* `sysupgrade -f filename.tar.gz`

## Decrypting Firmware

Firmware is easily decrypted using [Decrypt_RBI_Firmware_Utility](https://github.com/Ansuel/Decrypt_RBI_Firmware_Utility/releases) on any platform (Java Required). If you cannot find your OSCK and your device is rooted then extract it. See [secr](https://github.com/pedro-n-rocha/secr) for details of a safe process which does not overwrite any files on the device. Please [share your OSCK](https://github.com/Ansuel/Decrypt_RBI_Firmware_Utility/issues/new) and use it to decrypt firmware.

## The Boot Process

To be updated * refer to the [OpenWrt Boot Process guide](https://openwrt.org/docs/techref/process.boot) as an example for now but don't rely on it.

## The Homeware Flash Layout

TG799vac:

`root@mygateway:~# cat /proc/mtd`

|Device|   Size   | Erasesize | Name         |
|:-----|:---------|:----------|:-------------|
| mtd0 | 10000000 | 00020000  | "brcmnand.0" |
| mtd1 | 02c60000 | 00020000  | "rootfs"     |
| mtd2 | 05920000 | 00020000  | "rootfs_data"|
| mtd3 | 05000000 | 00020000  | "bank_1"     |
| mtd4 | 05000000 | 00020000  | "bank_2"     |
| mtd5 | 00020000 | 00020000  | "eripv2"     |
| mtd6 | 00040000 | 00020000  | "rawstorage" |

Apart from partition sizes, and `mtd2` which may appear named as `userfs` instead, it's always the same.

## Backup/restore bit-for-bit dumps

This guide will show you how to dump a bit-for-bit clone of any partition and reflash it.

### You will need

* FAT32 USB Stick
* 5min

### Making dumps

`bank_1` is usually mapped to the `mtd3` partition and `bank_2` is usually mapped to `mtd4`, you do not really need to backup firmware banks if you already have an RBI file for that same firmware available.

If you are not sure you already have the same firmware saved somewhere, you can extract the RBI file, mark the first 4 bytes of the resulting binary to 0x00 and compare its checksum against output of `md5sum /dev/mtd*` (this may take a while to compute, be patient).

You definitely need instead to backup all other partitions, especially the `eripv2` one, and all the others. You can get the full partition list with `cat /proc/mtd`

It is good practice to keep moving dumped partitions to USB as soon as you complete one in order to minimise the chance of filling the ram, and causing an out-of-memory crash and reboot.

1. Plug in a USB stick and run:

```bash
ls -la /mnt/usb
```

Example output:

```bash
root@mygateway:~# ls -la /mnt/usb/
drwxr-xr-x    2 root     root             0 Jan 16 12:31 .
drwxrwxrwx    1 root     root             0 Jan 16 10:55 ..
lrwxrwxrwx    1 root     root            20 Jan 16 12:31 USB-A1 -> /tmp/run/mountd/sda1
```

1. To backup, run: `dd if=/dev/mtd<X> of=/tmp/mtd<X>.dump`.

    * Replace `<X>` with any block device number.

2. Move the dumped partition into USB drive, run: `mv /tmp/mtdX.dump /mnt/usb/<usb-path>/`.

    * Replace `<usb-path>` with your USB drive, see Step 1.

3. If `<X>` partition does not include any flash portion currently mounted with enabled write access, make sure to compare checksums to ensure the dump is a 1:1 exact copy.

4. Repeat from Step 1 for every partition you would like to dump.

#### Restoring dumps

To restore a partition dump, run: `mtd write /mnt/usb/<usb-path>/mtd<X>.dump <partition_name>`

* Replace `<usb-path>` with your USB drive path

* Replace `<X>` with the block number

* Replace `<partition_name>` with the partition name you want to flash to (names are shown in `/proc/mtd` too)

Raw firmware dumps (which are not RBI files) are flashed this way to matching devices.

## IPv6 Issues

IPv6 is very problematic in most "TCH" Wrt builds (Homeware). The old OpenWRT version used by Technicolor to build Homeware (Chaos Calmer) has broken IPv6 Support. It also depends on the ISP's configuration. [See more.](https://github.com/Ansuel/tch-nginx-gui/issues/114)

## BusyBox (ash)

The gateway runs [BusyBox](https://busybox.net/about.html) as it's terminal emulator, designed for Embedded Linux systems.

```bash
root@mygateway:~# busybox --help
BusyBox v1.23.2 (2017-08-22 01:34:50 UTC) multi-call binary.
BusyBox is copyrighted by many authors between 1998-2012.
Licensed under GPLv2. See source distribution for detailed
copyright notices.

Usage: busybox function arguments...
   or: busybox --list
   or: function arguments...

        BusyBox is a multi-call binary that combines many common Unix
        utilities into a single executable.  Most people will create a
        link to busybox for each function they wish to use and BusyBox
        will act like whatever it was invoked as.

Currently defined functions:
        , , addgroup, arping, ash, awk, base64, basename, bunzip2, bzcat,
        cat, chgrp, chmod, chown, chpasswd, chroot, chrt, clear, cmp, cp,
        crond, crontab, cut, date, dd, df, dirname, dmesg, du, echo, egrep,
        env, expr, false, fgrep, find, free, fsync, grep, gunzip, gzip, halt,
        head, hexdump, hostid, hwclock, id, ifconfig, insmod, kill, killall,
        less, ln, lock, logger, login, ls, lsmod, lsusb, md5sum, mkdir, mkfifo,
        mknod, mktemp, mount, mv, nc, netmsg, netstat, nice, nslookup, ntpd,
        passwd, pgrep, pidof, ping, ping6, pivot_root, poweroff, printf, ps,
        pwd, readlink, reboot, reset, rm, rmdir, rmmod, route, sed, seq, sh,
        sha256sum, sleep, sort, start-stop-daemon, strings, switch_root, sync,
        sysctl, tail, tar, taskset, tee, telnet, test, time, timeout, top,
        touch, tr, traceroute, traceroute6, true, udhcpd, umount, uname, uniq,
        uptime, vconfig, vi, wc, wget, which, xargs, yes, zcat
```

## BusyBox (ash) Scripting</b>

In practical terms it can be thought of as a stripped down version of bash, so write bash script and fix the errors for features not supported.

[A basic ash Guide](https://linux.die.net/man/1/ash)

## Lua

All of the web interface and some of the daemons are written in Lua.

```bash
lua -v
Lua 5.1.5  Copyright (C) 1994-2012 Lua.org, PUC-Rio (double int32)
```

[Lua 5.1 Reference](https://www.lua.org/manual/5.1/)
