# Replacing Type 1 Firmwares

Every `Type 1` firmware allows you to perform a firmware *upgrade*, either via stock web UI, or official *unlocked* modes, or hidden web pages. We are going to exploit this possibility in order to flash an arbitrary firmware version of `Type 2`.

## Flashing via AutoFlashGUI

In this example we are working with the `VANT-F` Gateway on `17.2.0261`, which is a `Type 1` firmware. `16.3.7567` is the `Type 2` firmware we are going to flash.

First, make sure you changed the default web admin password. Run AutoFlashGUI and configure your gateway ip address and web admin credentials. Browse for the `Type 2` RBI firmware to flash on your Gateway, in this case it is `vant-f_CRF687-16.3.7567-660-RG.rbi`. Tick the "Flash firmware?" checkbox and click "Run". Allow it to finish flashing. It will also attempt rooting.

!!! question "Is current SSH server permanent?"
    If AutoFlashGUI does not know how to set permanent root access on your model it will create a temporary SSH dropbear instance on port `6666`. You will configure  dropbear in order to run a permanent LAN-side SSH server later on following this guide.

Try firing up your SSH client of choice and connect with the Username and Password as `root/root` to the Gateway IP on default port `22`, or `6666`. If you manage to login into root shell, jump to [Final Type 2 Steps](../Type2/#final-type-2-steps) now. Otherwise, if AutoFlashGUI didn't manage to get root, your Type 2 firmware requires a different rooting strategy: start reading the [Type 2 - Direct Rooting](../Type2/) guide.

## Flashing via Web UI

Sometimes the stock web UI allows users to perform firmware upgrades on their own. In such cases AutoFlashGUI should also work as it exploits the same feature, but it is good to know you don't strictly need to depend on some tool.

It may also happen the firmware allows you to activate some kind of "*Unlocked*" mode where you can reconfigure hidden options for use with different ISP's. This is typical of Gateways deployed in countries where local laws enforce ISP's to allow users reusing their hardware. Such unlocking mode is usually offered after factory reset, before the Gateway gets automatically provisioned from the ISP. Of course it is not rooting, but it is very likely a firmware upgrade option becomes available in such modes.

In any of the above cases you can easily flash the `Type 2` firmware we need. Do it, wait for the flashing to complete, then start reading the [Type 2 - Direct Rooting](../Type2/) guide.
