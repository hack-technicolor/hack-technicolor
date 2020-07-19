# Home

## IMPORTANT, do not SKIP

**Warning:** This process is not supported by the manufacturer or supplier of your Gateway.

There is no way of knowing your situation and the process could break your Gateway or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Quick start: first steps

We conventionally define different firmware *Types* to make different paths easier to follow. Determine your current firmware version and find out which *Type* it is by using the [Firmware Repository](Repository/).

!!! hint "Can't find your firmware?"
    Determining your current version number is not always an easy task, make sure you read the correct one. Very old firmware's from the Homeware 10.x era and older versions are outside the scope of this wiki. Despite the existence of old "*unlocking*" guides, if newer "*rootable*" firmware exists for such gateways, they can be upgraded following the same steps as `Type ???`. Also, consider any other newer not yet listed firmware’s as `Type ???`.

You are now required to read the complete [Introduction to Homeware Hacking](Hacking/Introduction/).

If your gateway firmware is:

- Type 1 is not directly rootable so load Type 2 then root other bank containing Type 1
    - See [Replacing Type 1 Firmwares](Hacking/Type1/) for help

- Type 2 is directly rootable
    - See [Rooting Type 2 Firmwares](Hacking/Type2/) for detailed guide

- Type 3 has more complicated process to load Type 2
    - See [Replacing Type 3 Firmwares](Hacking/Type3/) for help.

- Type ??? is unknown
    - Try the same as for Type 2, follow Type 3 steps otherwise

See the [README](https://github.com/hack-technicolor/hack-technicolor/blob/master/README.md) for more info about what are *Types*.

If in doubt, you may need to ask for help on your local community forum threads: AU @ [*whirlpool.net.au*](https://forums.whirlpool.net.au/thread/9vxxl849), IT @ [*ilpuntotecnico.com*](https://www.ilpuntotecnico.com/forum/index.php/board,9.0.html)

[![Gitter](https://badges.gitter.im/Hack-Technicolor/community.svg)](https://gitter.im/Hack-Technicolor/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## More guides and resources

This wiki collects a lot of useful reference material. Here is a quick index for pages about your rooted Homeware gateway.

- [Hardening Root Access](Hardening/): how to prevent loosing root access
- [Safe Firmware Upgrade](Upgrade/): how to install new firmwares of any Type preserving root access
- [Resources](Resources/): details on common advanced topics, very interesting for expert people
- [Recovery](Recovery/): comprehensive explained collection of known methods for device recovery
- [Firmware Repository](Repository/): collection of known firmwares for supported devices
- [Unlock Functionality](Unlock/): tweaks to unlock full device potential
