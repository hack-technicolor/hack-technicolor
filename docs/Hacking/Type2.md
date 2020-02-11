# Rooting Type 2 Firmwares

## Rooting via different strategies

Every `Type 2` firmware can be rooted directly by some known rooting strategy. Look into [Firmware Repository](../../Repository/) for known valid Root Strategy # for your firmware. If no Root Strategy is specified, try them all or pick one that could reasonably work because of similarities (same ISP, same webUI, same model,...). It is recommended to always perform a factory reset before any new attempt otherwise you could get unpredictable results.

!!! info "WANTED!"
    Existing rooting strategies may also work with firmware's for models you don't see listed here or in the [Firmware Repository](../../Repository/). If you get some success with other models not listed here, let us know! Every rooting guide intentionally written or adapted to be explicitly compatible with this wiki could be linked here.

 | Strategy # | Known as            | Where to look for instructions |
 |:----------:|:--------------------|:------------------------------:|
 | #0         | AutoFlashGUI        | [external link](https://github.com/mswhirl/autoflashgui) ([download](https://github.com/mswhirl/autoflashgui/archive/master.zip)) |
 | #1         | FASTGate samba hack | [external link (ita)](https://www.ilpuntotecnico.com/forum/index.php?topic=80598) |
 | #2         | tch-exploit         | [external link](https://github.com/BoLaMN/tch-exploit) ([download](https://github.com/BoLaMN/tch-exploit/releases)) |
 | #3         | clash escaping      | not documented yet, ask communities |

Once you finished running through any of the above guides, and you got your SSH client connected into a root shell come back here and continue reading [Final Type 2 steps](#final-type-2-steps) below.

## Final Type 2 steps

!!! warning "Is the current SSH server permanent?"
    If the tool you used does not know how to correctly set permanent root access on your firmware, or you mixed different rooting strategies without resetting between them, you may get a temporary SSH dropbear instance on port `6666`. You will configure dropbear in order to run a permanent LAN-side SSH server later on following this guide.

Fire up your SSH client and connect with user `root` to the Gateway IP on default port `22`, or `6666`.

As your first step into your brand-new rooted Gateway, it is a good idea to always ensure the serial console port is enabled - this is a very useful feature in case of disasters, so just do it. Execute the following command:

```bash
sed -i 's/#//' /etc/inittab
```

At this point you have a rooted `Type 2` image on your Gateway, but your trip is not over. Take note of the exact `Type 2` firmware version you are now running, could be useful in future for recovery purposes.

If you would like to stay on this `Type 2` firmware for daily usage and stay safe from possible soft-bricks or terrible issues, you now need to ensure your *bank plan* is optimal. Jump to [Bank Planning](../PostRoot/#bank-planning).
