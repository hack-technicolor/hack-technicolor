# Replacing Type 3 Firmwares

Replacing a `Type 3` firmware with a `Type 2` one that can be directly rooted, is not so easy as for a `Type 1`. Two essential points you need to get:

- There has to exist at least one `Type 2` firmware for your board available **as RBI** to replace with
- Assuming the previous point is true, replacing your `Type 3` firmware is **always** possible

## Phase 1: uploading firmware replacement

Head to [Firmware Repository](../Repository/) and get a copy of a `Type 2` image of your choice. Use [BOOTP flashing](../Recovery/#bootp-flashing) to load that `Type 2` firmware into your device `bank_1`. Two things can happen:

- Case A: the firmware you uploaded boots up. Your `bank_1` was active already. You're almost done. You may experience some issues with webui errors or invalid credentials: resetting by [RTFD](../Recovery/#reset-to-factory-defaults-rtfd) will resolve all of them. You can now start reading [Rooting Type 2](../Hack%20Type%201&2/#type-2-direct-rooting) guide.
- Case B: after reboot you still see your `Type 3` firmware in place. Your `bank_1` is not active. This is the unlucky case. Continue reading to discover how to sort out this uncomfortable situation.

## Phase 2: booting from bank_1

When you upload a firmware image with BOOTP via TFTP, it is always flashed into `bank_1`. If the active bank is `bank_2` instead, you won't automatically see your device booting the new image you just flashed. Read how to [Change booted bank](../Recovery/#change-booted-bank). Once you get in there, just start reading [Rooting Type 2](../Hack%20Type%201&2/#type-2-direct-rooting) guide.
