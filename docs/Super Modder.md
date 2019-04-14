## Super Modder
### Backing up Configuration

Your a Super Modder. You flash your modem on a daily basis.

To save the Config:
* `sysupgrade -i -b filename.tar.gz` - 
    
To restore the Config:    
* `sysupgrade -f filename.tar.gz`] - restore configuration after firmware reflash

### Decrypting Firmware

See [secr](https://github.com/mswhirl/secr) for details (original code from [here](https://github.com/pedro-n-rocha/secr)). Follow instructions with OSCK from <a href="https://pastelink.net/laft">repository</a>, or extract OSCK from modem, then decrypt firmware. This procedure is safe (no files are overwritten on the modem).

| Model Number | Mnemonic |                        OSCK                                      | 
|:-------------|:---------|:----------------------------------------------------------------:|
| TG797nv3     |  dant-o  | RBI not encryped, only signed                                    |
| TG789vac (v1)|  vant-d  | Unknown                                                          |
| TG789vac v2  |  vant-6  | 546259AFD4E85AA6FFCE358CE0A93452E25A848138A67C142E42FEC79F4F3784 |
| TG799vac     |  vant-f  | 7fa2fdf4d4dc31bf66f91dda9a3e8777b7d7d2ec6e8db1926c0831ca2a279fdb |

### The Boot Process

To be updated - refer to the <a href="https://openwrt.org/docs/techref/process.boot">OpenWrt Boot Process guide</a> as an example for now but don't rely on it.

== <b>The OpenWrt Flash Layout</b>

To be updated - refer to the <a href="https://openwrt.org/docs/techref/flash.layout">The OpenWrt Flash Layout guide</a> as an example for now but don't rely on it. eg:

$ root@mygateway:~# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 10000000 00020000 "brcmnand.0"
mtd1: 02c60000 00020000 "rootfs"
mtd2: 05920000 00020000 "rootfs_data"
mtd3: 05000000 00020000 "bank_1"
mtd4: 05000000 00020000 "bank_2"
mtd5: 00020000 00020000 "eripv2"
mtd6: 00040000 00020000 "rawstorage"


== <b>Preinit and Root Mount and Firstboot Scripts</b>

To be updated - refer to the <a href="https://openwrt.org/docs/techref/preinit_mount?s[]=overlay">OpenWrt Preinit and Root Mount and Firstboot Scripts guide</a> as an example for now but don't rely on it.


== <b>Backup / Restore without rbi file</b>

Bank_1 is on mtd3 partition and bank_2 is on mtd4. Best to backup to usb to minimise chance of filling storage and bricking device.

Plug in a USB stick and run [`ls -la /mnt/usb`]

$ root@mygateway:~# ls -la /mnt/usb/
drwxr-xr-x    2 root     root             0 Jan 16 12:31 .
drwxrwxrwx    1 root     root             0 Jan 16 10:55 ..
lrwxrwxrwx    1 root     root            20 Jan 16 12:31 USB-A1 -> /tmp/run/mountd/sda1

* Backup: [`dd if=/dev/mtd[*X*] of=/mnt/usb/USB-A1/mtd[*X*].bin`] (replace [*X*] with 3 or 4)
* Restore: [`mtd write /mnt/usb/USB-A1/mtd[*X*].bin bank_[*Y*]`] (replace [*Y*] with 1 or 2)
           Firmware can be restored to either bank. 

Tiscali firmware (which has no RBI files) is flashed this way to other TG789 devices.


== <b>IPv6 Connection Issue</b>

['Ipv6 is really problematic... On openwrt on this old base it think it's quite broken... Also the configuration depends on the ISP... Hard to fix...'] https://github.com/Ansuel/tch-nginx-gui/issues/114


== <b>BusyBox</b>

The gateway runs <a href="https://busybox.net/about.html">busybox</a>, an embedded linux system with minimalist documentation.

$ root@mygateway:~# busybox --help
BusyBox v1.23.2 (2017-08-22 01:34:50 UTC) multi-call binary.
BusyBox is copyrighted by many authors between 1998-2012.
Licensed under GPLv2. See source distribution for detailed
copyright notices.
$ 
Usage: busybox [function [arguments]...]
   or: busybox --list
   or: function [arguments]...
$ 
        BusyBox is a multi-call binary that combines many common Unix
        utilities into a single executable.  Most people will create a
        link to busybox for each function they wish to use and BusyBox
        will act like whatever it was invoked as.
$ 
Currently defined functions:
        [, [[, addgroup, arping, ash, awk, base64, basename, bunzip2, bzcat,
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


== <b>ash script</b>

Shell script is ash and best reference found is https://linux.die.net/man/1/ash. In practical terms it can be thought of as stripped down bash script so write bash script and fix the errors for features not supported.

<a href="https://www.howtogeek.com/108890/how-to-get-help-with-a-command-from-the-linux-terminal-8-tricks-for-beginners-pros-alike/">-h or –help</a>

== <b>Lua</b>

Much of the interface is written in Lua.

$ $ lua -v
Lua 5.1.5  Copyright (C) 1994-2012 Lua.org, PUC-Rio (double int32)

<a href="https://www.lua.org/manual/5.1/">Lua 5.1 Reference Manual</a>.