# Home

!!! danger "Read Before Proceeding!"
    This process is not supported by the manufacturer or supplier of your gateway. There is no way of knowing your situation and the process could break your gateway or reduce its security, allowing other people into your network. Anyone following this guide accepts full responsibility for any and all of the outcomes.

## Where to Start

We conventionally define different firmware *Types*. This is to address differetn rooting paths and made things simpler for you to follow.
Find out what *Type* of firmware is on your gateway from the [Firmware Repository](Firmware%20Repository/).

!!! hint "Can't find your firmware?"
    Very old firmware's from the Homeware 10.x era are outside the scope of this wiki. Despite the existence of old "*unlocking*" guides, if newer "*rootable*" firmware exists the gateway can be upgraded following the same steps as of `Type ???`. Also, consider any other newer, not yet listed firmware of `Type ???`.

If your gateway firmware is:

- Type 1 is not directly rootable so load Type 2 then root other bank containing Type 1
  - See [Hack Type 1 and 2](Hack%20Type%201&2/) for detailed guide
- Type 2 directly rootable
  - See [Hack Type 1 and 2](Hack%20Type%201&2/) for detailed guide
- Type 3 has more complicated process to load Type 2
  - See the [TFTP flashing guide](Recovery/#boot-p-recovery-mode-tftp-flashing) and [bootfail](Recovery/#bootfail-procedure)
- Type ??? is unknown
  - Try the same as for Type 2, follow Type 3 steps otherwise

See the [README](https://github.com/kevdagoat/hack-technicolor/blob/master/README.md) for more info about what are *Types*.

If in doubt, you may need to ask for help on your local community forum threads: AU @ [*whirlpool.net.au*](https://forums.whirlpool.net.au/thread/9vxxl849), IT @ [*ilpuntotecnico.com*](https://www.ilpuntotecnico.com/forum/index.php/board,9.0.html)
