# Post-Root Procedures

!!! warning "Stop!"
    Do not follow any post-root procedure unless explicitly told to.

## Bank Planning (without firmware upgrade)

We are now going to prepare an optimal bank planning for the same firmware version you have now booted.

Run the following command to look at your Gateway's bank state:

```find /proc/banktable -type f -print -exec cat {} ';'```

Take note of `active` and `booted` banks:

```bash
xxxxx
/proc/banktable/booted
<take note of this>
/proc/banktable/active
<take note of this>
xxxxx
```

At the end of this guide your Gateway will boot the current firmware image as per *optimal* bank plan:

```bash
/proc/banktable/active
bank_1
/proc/banktable/booted
bank_2
```

!!! caution "On which bank should I stay to be safe?"
    It's strongly recommended to stick to the *optimal* bank plan (listed above) before modding your device further. The bigger picture description can be found [here](https://github.com/Ansuel/tch-nginx-gui/issues/514). The short thing is that you should really consider modding your preferred firmware version (not necessarily of `Type 2`) while booted from `bank_2` keeping `bank_1` as the active one.
    **Key Point**: it's unsafe to deeply mod firmware settings of any firmware booted from `bank_1`.

These gateways use two flash partitions (`bank_1` and `bank_2`), which can be upgraded/used almost independently.

They are signature checked before boot so you can't flip a single bit in the base firmware image in either bank if you want to see your device booting. The whole config and customized stuff is stored in the matching folder within the [overlay filesystem](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/overlayfs.txt), i.e. `/overlay/bank_2`

!!! hint
    You can see your modified config files in `/overlay` if you want to backup stuff or see what changes you made. All original versions of modified files are stored permanently in `/rom`, in case you would like to revert something back.

When a proper Reset to Factory Defaults is done, the overlay partition is not formatted, just the relevant `/overlay/bank_*` partition is deleted. You can learn more on such aspects by reading the [Recovery](../../Recovery/) page.

We need to make sure the current firmware loads from the recommended bank on every reboot.

!!! danger "Notable exception: Missing RBI"
    In the unfortunate case that there are no RBI firmware files available for your model, you are not in a safe position because you can't exploit `BOOTP` recovery options. In such a situation whatever bank you boot is the same. Your best option is to keep a copy of your rootable firmware on both banks. Skip the next step for optimality.

If your `booted` bank is `bank_2` already, run the following commands:

```bash
# Activate bank_1
echo bank_1 > /proc/banktable/active
# Erase firmware in bank_1
mtd erase bank_1
```

If your `booted` bank is `bank_1` instead, run the following commands:

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

You should now be in the previously mentioned *optimal* bank plan. On each reboot, your device will try booting `active` bank first. Since we set `bank_1` as active and we also erased `bank_1` firmware, it will boot from `bank_2`.

At this point, you now need to check if your [SSH server setup](#setting-up-permanent-ssh-server) is permanent.

## Bank Planning (with firmware upgrade)

!!! warning "Are you looking for firmware upgrade guide?"
    This is not a firmware upgrade guide. This is a bank planning guide with integrated firmware upgrade. If you came here in search of firmware upgrade guide you are in the wrong place. You can find that guide in this wiki homepage.

We are now going to prepare an optimal bank plan for another firmware you don't have on your Gateway yet.

At this stage it's possible to choose whatever *Type* of firmware you would like, to end up having it rooted and running.

We need to mod the `notbooted` bank's config, then switch over to it without doing a factory reset or standard upgrade procedure. Note that if you factory reset while not on a `Type 2` firmware, you will need to follow the entire guide from the beginning and a auto-upgrade could lock you out permanently in that reset state if the Gateway has internet access!

Let's rule out any current bank plan inconsistency. Run this command **now** to ensure this guide will work as expected:

```bash
cat /proc/banktable/booted > /proc/banktable/active
```

Run the following command to look at your current Gateway's bank plan:

```find /proc/banktable/*booted -type f -print -exec cat {} ';'```

It should now look either like this (*"State A"*):

```bash
/proc/banktable/booted
bank_2
/proc/banktable/notbooted
bank_1
```

or this (*"State B"*):

```bash
/proc/banktable/booted
bank_1
/proc/banktable/notbooted
bank_2
```

!!! hint "If you are on *State A*, move to *State B* now!"
    To follow the *optimal* bank plan configuration, we need to swap your Gateway to *State B*.

Run these commands to move from *state A* to *state B*:

```bash
# Make a temp copy of the firmware in bank_2
dd if=/dev/mtd4 of=/tmp/bank2.fw
# Flash that copy into bank_1
mtd write /tmp/bank2.fw bank_1
# Clean temp firmware copy
rm /tmp/bank2.fw
# Clean any existing overlay for bank_1 firmware
rm -rf /overlay/bank_1
# Make a temp copy of overlay for bank_2 firmware
cp -rf /overlay/bank_2 /tmp/bank_2_backup
# Free up overlay space by removing existing overlay for bank_2 firmware
rm -rf /overlay/bank_2
# Use the previously made temp copy as overlay for bank_1 firmware
cp -rf /tmp/bank_2_backup /overlay/bank_1
# Activate bank_1
echo bank_1 > /proc/banktable/active
# Erase firmware in bank_2
mtd erase bank_2
# Reboot to first valid firmware
reboot
```

The *optimal* bank plan will look like this once you reach the end of this guide:

```bash
/proc/banktable/active
bank_1
/proc/banktable/booted
bank_2
```

!!! caution "On which bank should I stay to be safe?"
    It's strongly recommended to adhere to the above *optimal* bank plan before modding your device further. The bigger picture description can be found [here](https://github.com/Ansuel/tch-nginx-gui/issues/514). The short thing is that you should really consider modding your preferred firmware version (not necessarily of `Type 2`) while booted from `bank_2` keeping `bank_1` as the active one.
    **Key Point**: it's unsafe to deeply mod firmware settings of any firmware booted from `bank_1`.

These gateways use two flash partitions (`bank_1` and `bank_2`) which can be upgraded/used almost independently.

They are signature checked before boot so you can't flip a single bit of the base firmware image in either bank if you want to see your device booting. The whole config and customized stuff is stored in the matching folder within the [overlay filesystem](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/filesystems/overlayfs.txt), i.e. `/overlay/bank_2`

!!! hint
    You can see your modified config files in `/overlay` if you want to backup stuff or see what changes you made, however, all original versions of modified files are stored permanently in `/rom`, in case you would like to revert something back.

When a proper Reset to Factory Defaults is done, the overlay partition is not formatted, just the relevant `/overlay/bank_*` partition is deleted. You can learn more on such aspects by reading the [Recovery](../../Recovery/) page.

Unless your target preferred firmware is there already, it's now time to flash it into its final destination: the `notbooted` bank.
This time you can't use just AutoFlashGUI, even if your current firmware is `Type 2`. Otherwise the regular firmware upgrade procedures will perform an unwanted switchover, leading to a reboot immediately before any indirect root could be performed.

The shortest path for firmware flashing depends whether you start from on *"state A"* or *"state B"*.

- If you are on **state A** and your `notbooted` bank is `bank_1` since you didn't take the hints, well, go with BOOTP flashing. After reboot you will still be on your rooted/rootable `Type 2` firmware from `bank_2`. However, if your preferred firmware is not available as RBI file, you can't continue this way. If not, go with [BOOTP flashing](../../Recovery/#bootp-recovery-mode-tftp-flashing) then come back here and continue reading.

- If you are on **state B** and your `notbooted` bank is `bank_2`, you now need to [decrypt and extract](../../Resources/#decrypting-firmware) the raw bank image from the RBI firmware file, change its first 4 bytes to 0x00 and [restore it manually](../../Resources/#backuprestore-bit-for-bit-dumps) into `notbooted` bank as you were restoring a previous backup - it's easier and faster than BOOTP. There's another way of doing the very same thing in a single command, however it's really recommended you do it manually at least once in your life to take confidence with all the tools and take this opportunity to also make backups. Is your preferred firmware available as raw bank dump already? You just saved some good amount of fun ... and time: just restore it back into `notbooted` bank. Is the OSCK for your device model unknown? You have root access right now on the current `Type 2` firmware, so get it, **share it**, and use it. Come back here and continue reading when you are done.

Welcome back! Are you enjoying so far?

Now, run the following to prepare `notbooted` bank for temporary root and switch back to it:

```bash
rm -rf /overlay/`cat /proc/banktable/notbooted`
mkdir -p /overlay/`cat /proc/banktable/notbooted`/etc
chmod 755 /overlay/`cat /proc/banktable/notbooted` /overlay/`cat /proc/banktable/notbooted`/etc
echo -e "echo root:root | chpasswd
sed -i 's#/root:.*\$#/root:/bin/ash#' /etc/passwd
sed -i 's/#//' /etc/inittab
dropbear -p 6666 &
rm /overlay/`cat /proc/banktable/booted`/etc/rc.local
" > /overlay/`cat /proc/banktable/notbooted`/etc/rc.local
chmod +x /overlay/`cat /proc/banktable/notbooted`/etc/rc.local
cat /overlay/`cat /proc/banktable/notbooted`/etc/rc.local
```

You should get this output from the last command:

```bash
echo root:root | chpasswd
sed -i 's#/root:.*\$#/root:/bin/ash#' /etc/passwd
sed -i 's/#//' /etc/inittab
dropbear -p 6666 &
rm /overlay/`cat /proc/banktable/booted`/etc/rc.local
```

If you didn't, reboot the Gateway and retry the procedure.

If successful, nuke the `Type 2` firmware from inside `booted` bank with:

```bash
mtd erase `cat /proc/banktable/booted`
```

Then reboot and wait 3 to 4 minutes for the Gateway to boot into this "new" rooted bank. It will fail three attempts to boot from the empty active bank, then it will load your firmware from the inactive one.

You should now be in the previously mentioned "optimal" bank plan unless you opted to go on from *state A*.

!!! hint "Something went Wrong?"
    Flash back the same `Type 2` image you were up to now, following [BOOTP flashing](../../Recovery/#bootp-flashing). If you followed the initial advice about bank planning, you will be back on the exact situation you were before the last command. Otherwise, you will likely need to solve a typical *soft-brick* issue: prepare some extra luck, perform a [RTFD](../../Recovery/#reset-to-factory-defaults-rtfd) and then restart over from the beginning.

Now you have temporary root access on your preferred firmware, you can now jump below to set up [permanent SSH server](#setting-up-permanent-ssh-server).

## Setting up Permanent SSH Server

Are you connected to SSH on port `6666`?

If the answer is "Yes", run these commands to setup a permanent SSH access on port `22` by defining a new dropbear instance:

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

You don't need to run the above commands if you are already able to connect on port `22`, the default one.

Now proceed to changing your [root password](#change-the-root-password), this is **mandatory**.

## Change the Root Password

!!! warning "Serious hint!"
    Do not ignore this step! Your firmware was probably designed to work only on certain specific ISP network. Some kind of remote SSH access could be left open by design in such a way only that same ISP could access. Connecting to some different ISP network could lead to this open access to be exposed on the internet.

Run:

```bash
passwd
```

Now you **must** harden your access, to prevent it from being lost because of unwanted automatic firmware upgrades in future. See [Hardening Root Access](../../Hardening/) page.
