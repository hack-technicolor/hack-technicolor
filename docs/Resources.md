


### What tools can I use to administer OpenWrt from a Windows computer?</b>

There are a number of tools such as cmder, SmarTTY, PuTTY, and WinSCP as described in the OpenWRT SSH Administration for Newcomers(https://openwrt.org/docs/guide-quick-start/sshadministration) page.

### Handy Commands

* `find /proc/banktable -type f -print -exec cat {} ';'` 
    - Checking firmware flashed and what is active.

* `ps` 
    - Shows processes that are running.

* `netstat -tuplen` 
    - Shows programs that are listening as network services.

* `netstat -lenp` 
    - Shows everything that's listening on sockets (TCP, UPD, Unix etc).

* `df -h` 
    - Free (NAND) space.

* `uci show` 
    - Dump entire config (~7700+ lines to console).

* `uci show | grep password` 
    - Example to filter lines with password.

* `logread -f` 
    - Access logs for most services (which use syslog). Pass an argument of -e nginx to match log entries just related to Nginx, which is perfect for debugging errors in the Web GUI.

    - Remove `-f` flag for all time logs (erased every reboot).

* `for F in /etc/init.d/* ; do $F enabled && echo $F on || echo $F **disabled**; done` 
    - Display status of all init.d scripts.

* `/rom/usr/lib/cwmpd/transfers/switchover.sh` 
    - Switch bank and reboot.

* `cat /etc/openwrt_release` 
    - OpenWrt Release metadata. 
    - eg TG799:
```
DISTRIB_ID='OpenWrt'
DISTRIB_RELEASE='Chaos Calmer'
DISTRIB_REVISION='r46610'
DISTRIB_CODENAME='chaos_calmer'
DISTRIB_TARGET='brcm63xx-tch/VANTF'
DISTRIB_DESCRIPTION='OpenWrt Chaos Calmer 15.05.1'
DISTRIB_TAINTS='no-all busybox'
```

### Files

* `/www/*` 
    - Lua/HTML Web Interface source files.

* `/etc/config/*` 
    - UCI config source files, pehaps more readable than `uci show`.

* `/sbin/*.sh, /usr/bin/*.sh, /usr/sbin/*.sh` 
    - Various executables, many custom-written for this hardware.

* `/etc/init.d/*` 
    - Services present; May or may not be enabled or running.


### LED's

[Directly accessing /sys/class/leds is a BAD practice...](https://github.com/davidjb/technicolor-tg799vac-hacks/issues/6#issue-388905312)

* `ls -1 /sys/class/leds/` 
    - List available LED's.

* `cat /sys/class/leds/<led>:<colour>/trigger` 
    - Shows the triggers available and the current trigger.
    - Replace LED with the name of the LED and colour with the colour, eg. `cat /sys/class/leds/dect:green/trigger`

* `echo "default-on" > /sys/class/leds/power:green/trigger`
    - Reset trigger to default.

* `opkg list | grep led` 
    - List all LED packages used.


#### Example:

Turn on LED:
`echo 1 > /sys/class/leds/power:green/brightness`

Turn off LED:
`echo 0 > /sys/class/leds/power:red/brightness`


## Super Modder
### Backing up Configuration

Your a Super Modder. You flash your modem on a daily basis.

To save the Config:
- `sysupgrade -i -b filename.tar.gz` - 
    
To restore the Config:    
- `sysupgrade -f filename.tar.gz`

### Decrypting Firmware

See secr(https://github.com/mswhirl/secr) for details (original code from here(https://github.com/pedro-n-rocha/secr)). Follow instructions with OSCK from below. If you cannot find your OSCK, you can check out the repository(https://pastelink.net/laft), or extract OSCK from modem, then decrypt firmware. This procedure is safe (no files are overwritten on the modem).

| Model Number    | Mnemonic |                        OSCK                                      | 
|:----------------|:---------|:-----------------------------------------------------------------|
| TG797nv3        |  dant-o  | RBI not encryped, only signed                                    |
| TG789vac (v1)   |  vant-d  | Unknown                                                          |
| TG789vac v2     |  vant-6  | 546259AFD4E85AA6FFCE358CE0A93452E25A848138A67C142E42FEC79F4F3784 |
| TG789vac v2 HP  |  vbnt-l  | a484245ccfbe2541b0c5c5e923be67a7deb9a823dd5cbab92cc619dea1391a42 |
| TG799vac        |  vant-f  | 7fa2fdf4d4dc31bf66f91dda9a3e8777b7d7d2ec6e8db1926c0831ca2a279fdb |
| TG799vac XTREAM |  vbnt-h  | Unknown                                                          |
| TG800vac        |  vant-y  | 8e07111f188641948e84506db65270bd26595ad41327235a53998db068dc3833 |
| DJA0231         |  vcnt-a  | Unknown                                                          |
| DJN2130         |  vbnt-j  | 222c4dc4a9df952b02d5a489a112cf5e29aaedf86adb634410d6721f15f451e4 |


### The Boot Process

To be updated - refer to the <a href="https://openwrt.org/docs/techref/process.boot">OpenWrt Boot Process guide</a> as an example for now but don't rely on it.

### The "TCH" Wrt (Homeware) Flash Layout
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

### Backup/Restore bit-for-bit

This guide will show you how to create a bit-for-bit clone of a bank and reflash it.

**You will need**

- FAT32 USB Stick
- 5min

Bank_1 is mounted on mtd3 partition and bank_2 is mounted on mtd4. It is good practise to backup to USB to minimise chance of filling the ram, causing a coredump and bricking your device.

1. Plug in a USB stick and run:
```
ls -la /mnt/usb
```
Example output:
```
root@mygateway:~# ls -la /mnt/usb/
drwxr-xr-x    2 root     root             0 Jan 16 12:31 .
drwxrwxrwx    1 root     root             0 Jan 16 10:55 ..
lrwxrwxrwx    1 root     root            20 Jan 16 12:31 USB-A1 -> /tmp/run/mountd/sda1
```

2. To backup, run `dd if=/dev/mtd<X> of=/mnt/usb/<usb-path>/mtd<X>.bin` 
      - Replace X with 3, 4 or any other block number
      - Replace usb-path with your USB drive, see Step 1.

3. To restore, run `mtd write /mnt/usb/<usb-path>/mtd<X>.bin bank_<n>`
      - Replace usb-path with your USB drive, see Step 1.
      - Replace X with the block number.
      - Replace N with the bank number you want to flash to.
      - Firmware can be restored to either bank. 

Tiscali firmware (which has no RBI files) is flashed this way to some TG789vac devices.


### IPv6 Issues

IPv6 is very problematic in most "TCH" Wrt builds (Homeware). The old OpenWRT version used by Technicolor that is used to build Homeware (Chaos Calmer) has broken IPv6 Support. It also depends on the ISP's configuration. See more.(https://github.com/Ansuel/tch-nginx-gui/issues/114)


### BusyBox (ash)

The gateway runs BusyBox(https://busybox.net/about.html) as it's terminal emulator, designed for Embedded Linux systems.

```
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

### BusyBox (ash) Scripting</b>

In practical terms it can be thought of as a stripped down version of bash, so write bash script and fix the errors for features not supported.

A basic ash Guide( https://linux.die.net/man/1/ash)


### Lua

All of the web interface and some of the daemons are written in Lua.

```
lua -v
Lua 5.1.5  Copyright (C) 1994-2012 Lua.org, PUC-Rio (double int32)
```

Lua 5.1 Reference(https://www.lua.org/manual/5.1/)
