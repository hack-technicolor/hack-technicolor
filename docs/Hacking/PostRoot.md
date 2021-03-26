# Post-Root Procedures

!!! warning "Stop!"
    Do not follow any post-root procedure unless explicitly told to in a previous step of this guide.

## Bank Planning

We are now going to prepare an *optimal* bank plan for the same firmware version you have now booted.

Run the following command to look at your Gateway's bank state:

```find /proc/banktable -type f -print -exec cat {} ';'```

You should see something like this being printed:

```bash
xxxxx
/proc/banktable/booted
<take note of this>
/proc/banktable/active
<take note of this>
xxxxx
```

If the above command failed, your board is not dual bank and no bank planning is possible. Otherwise, take note of the current `active` and `booted` banks.
This guide will let you setup your Gateway to boot the same firmware you are now running as per *optimal* bank plan. An optimal bank plan looks like this:

```bash
/proc/banktable/active
bank_1
/proc/banktable/booted
bank_2
```

We will now do what your current state requires to match the above one, such that the device will boot from the recommended bank on every reboot.

!!! question "Which bank should I _use_ to stay safe?"
    It's strongly recommended to stick to the above mentioned *optimal* bank plan before applying any further mod to your device. The bigger picture description is available [here](https://github.com/Ansuel/tch-nginx-gui/issues/514). The short thing is that you should really mod your preferred firmware version (not necessarily of *Type 2*) only while it's being booted from `bank_2` and keep `bank_1` as the active one.
    **Key Point**: it's unsafe to deeply mod any firmware which is being booted from `bank_1`.

!!! danger "Notable exception: Missing RBI"
    In the unfortunate case that there are no RBI firmware files available for your board, you are not in a safe position because you can't rely on `BOOTP` firmware recovery. The *optimal* bank plan relies on `BOOTP` to flash and clean-boot a firmware from `bank_1`. Your best option is to ensure you keep a copy of a rootable *Type 2* firmware on both banks and to avoid modding one of them. Please, check the firmware repository page for any available RBI and stop following this bank planning guide if there are none.
    In case some RBI firmwares are available but none of them is of *Type 2*, the hereby described *optimal* bank plan is still fine, despite some limitations.

Run the following commands:

```bash
# Ensure two banks match in sizes
[ $(grep -c bank_ /proc/mtd) = 2 ] && \
[ "$(grep bank_1 /proc/mtd | cut -d' ' -f2)" = \
"$(grep bank_2 /proc/mtd | cut -d' ' -f2)" ] && {
# Clone and verify firmware into bank_2 if applicable
[ "$(cat /proc/banktable/booted)" = "bank_1" ] && \
mtd -e bank_2 write /dev/$(grep bank_1 /proc/mtd | cut -d: -f1) bank_2 && \
mtd verify /dev/$(grep bank_1 /proc/mtd | cut -d: -f1) bank_2 || \
{ echo Clone verification failed, retry; exit; }
# Make a temp copy of overlay for booted firmware
cp -rf /overlay/$(cat /proc/banktable/booted) /tmp/bank_overlay_backup
# Clean up jffs2 space by removing existing old overlays
rm -rf /overlay/*
# Use the previously made temp copy as overlay for bank_2
cp -rf /tmp/bank_overlay_backup /overlay/bank_2
# Activate bank_1
echo bank_1 > /proc/banktable/active
# Make sure above changes get written to flash
sync
# Erase firmware in bank_1
mtd erase bank_1; }
# end
```

Power off the Gateway now. It is better not to use the reboot command here. Power it on again and wait for it to boot completely.
You should now be in the previously mentioned *optimal* bank plan. On each reboot, your device will try booting `active` bank first. Since we set `bank_1` as active and we also erased `bank_1` firmware, it will boot from `bank_2`.

!!! hint "Upgrade now!"
    Would you like to upgrade to a newer firmware? This is the perfect moment for doing it. It is now safe to also install *non-Type 2* firmwares. Just follow the [Safe Firmware Upgrade](../../Upgrade/) guide for this. You could also upgrade later in future and continue tweaking the current firmware. Once you did install the updated firmware, come back here and continue reading.

At this point, you now need to check if your [SSH server setup](#setting-up-permanent-ssh-server) is permanent.

## Setting up Permanent SSH Server

Are you connected to SSH on port `6666`? In most cases, the answer is "No, I didn't need to specify port 6666, I've got connected on default port 22". You don't need to run the below commands if you can already connect on default port `22`, your SSH setup is permanent already.

If the answer is "Yes", run these commands to setup a permanent SSH access on port `22` by defining a new dropbear instance:

```bash
uci -q delete dropbear.afg
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

Now proceed to changing your [root password](#change-the-root-password), this is **mandatory**.

## Change the Root Password

!!! warning "Serious hint!"
    Do not ignore this step! Your firmware was probably designed to work only on certain specific ISP network. Some kind of remote SSH access could be left open by design in such a way only that same ISP could access. Connecting to some different ISP network could lead to this open access to be exposed on the internet.

Run:

```bash
passwd
```

Now you **must** harden your access, to prevent it from being lost because of limited RBI availability or automatic firmware upgrades in future. See [Hardening Root Access](../../Hardening/) page.
