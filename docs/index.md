# Home

!!! danger "Read Before Proceeding!"
    This process is not supported by the manufacturer or supplier of your gateway. There is no way of knowing your situation and the process could break your gateway or reduce its security, allowing other people into your network. Anyone following this guide accepts full responsibility for any and all of the outcomes.

## Where to Start

- Find out what *Type* of firmware is on your gateway from the [Firmware Repository](Firmware%20Repository/)

!!! hint "Can't find your firmware?"
    Any missing or unlisted firmware is `Type ???`. Very old firmware's from the Homeware 10.x era are outside the scope of this wiki. Despite the existence of old "*unlocking*" guides, if newer "*rootable*" firmware exists the gateway can be upgraded by following the `TFTP` flashing guide from the [Recovery](Recovery/#boot-p-recovery-mode-tftp-flashing) section.

If your gateway firmware is:

- `Type 1` or `Type 2`: See [Hack Type 1 and 2](Hack%20Type%201&2/).

- `Type 3` or `Type ???`: See the TFTP [flashing guide](Recovery/#boot-p-recovery-mode-tftp-flashing).
  - For any other case, you may need to ask for help on your local community forum threads: AU @ [*whirlpool.net.au*](https://forums.whirlpool.net.au/thread/9vxxl849), IT @ [*ilpuntotecnico.com*](https://www.ilpuntotecnico.com/forum/index.php/board,9.0.html)

## What are Types

We conventionally define three different *Types*. This is to make the rooting process simpler.

- Type 1 is not directly rootable so load Type 2  then root other bank

- Type 2 directly rootable

- Type 3 has more complicated process to load Type 2

- Type ??? is unknown

See the [README](https://github.com/kevdagoat/hack-technicolor/blob/master/README.md) for more info.
