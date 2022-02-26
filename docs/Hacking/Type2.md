# Rooting Type 2 Firmwares

## Rooting via different strategies

Every `Type 2` firmware can be rooted directly by some known rooting strategy. Look into [Firmware Repository](../../Repository/) for known valid Root Strategy # for your firmware. If no Root Strategy is specified, try them all or pick one that could reasonably work because of similarities (same ISP, same webUI, same model,...). It is recommended to always perform a factory reset before any new attempt otherwise you could get unpredictable results.

!!! info "WANTED!"
    Existing rooting strategies may also work with firmware's for models you don't see listed here or in the [Firmware Repository](../../Repository/). If you get some success with other models not listed here, let us know! Every rooting guide intentionally written or adapted to be explicitly compatible with this wiki could be linked here.

 | Strategy # | Known as            | Where to look for instructions |
 |:----------:|:--------------------|:------------------------------:|
 | #A         | AutoFlashGUI        | [external link](https://github.com/mswhirl/autoflashgui) ([download](https://github.com/mswhirl/autoflashgui/archive/master.zip)) |
 | #B         | FASTGate samba hack | [external link (ita)](https://www.ilpuntotecnico.com/forum/index.php?topic=80598) |
 | #C         | tch-exploit         | [external link](https://github.com/BoLaMN/tch-exploit) ([download](https://github.com/BoLaMN/tch-exploit/releases)) |
 | #D         | clash escaping      | [external link (ita)](https://www.ilpuntotecnico.com/forum/index.php/topic,77981.msg246548.html#msg246548) |
 | #E         | Stock samba hack    | [external link](https://github.com/full-disclosure/FDEU-CVE-2020-1FC5) |

Once you finished running through any of the above guides, and you got your SSH client connected into a root shell come back here and continue reading [Final Type 2 steps](#final-type-2-steps) below.

!!! question "Is the current SSH server permanent?"
    If the rooting strategy you just used does not allow to directly set root SSH access on your firmware in a permanent fashion, or you mixed different rooting strategies without resetting between them, you may get a temporary SSH dropbear instance on port `6666`. You will configure dropbear in order to run a permanent LAN-side SSH server later on following this guide. Do not reboot the Gateway until then.

## Final Type 2 steps

Fire up your SSH client and connect with user `root` to the Gateway IP on default port `22`, or `6666`.

!!! note "Legacy ciphers and mismatching key alerts"
    If your SSH client refuses to use the only cipher supported by the Gateway, you need to allow it from your SSH client options.
    If your SSH client refuses to connect because of a different key was previously saved for your Gateway host/IP, follow your client instructions to clean or replace the old keys.

As first step into your brand-new rooted Gateway, it is a good idea to always ensure the serial console port is enabled - this is a very useful feature in case of disasters, so just do it. Execute the following command:

```bash
sed -i -e 's/#//' -e 's#askconsole:.*$#askconsole:/bin/ash#' /etc/inittab
```

At this point you have a rooted `Type 2` image on your Gateway, but your trip is not over. Take note of the exact `Type 2` firmware version you are now running, it could be useful to remember in future for recovery purposes.

To stay safe from terrible issues during your mods and achieve easier recovery from possible soft-bricks, you now need to ensure your *bank plan* is optimal. Jump to [Bank Planning](../PostRoot/#bank-planning).
