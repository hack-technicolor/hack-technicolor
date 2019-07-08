## Hacking Technicolor Gateways

**Disclaimer:** This process is not supported by the manufacturer or supplier of your gateway.
There is no way of knowing your situation and the process could break your gateway or reduce its security, allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Preliminary Steps

Before you start you need to head over to [the Firmware Repository](Firmware%20Repository/) to find out what *Type* of firmware your gateway is on today and then refer the appropriate section below.

!!! hint "Can't find your firmware?"
    You can consider any missing or unlisted firmware's as `Type ???`. Very old firmwares from the Homeware 10.x era are outside the scope of this wiki. Despite the existence of old "*unlocking*" guides, you can always upgrade to a newer "*rootable*" firmware, if any, by following the `BOOT-P` flashing guide from the [Recovery](Recovery/#boot-p-recovery-mode-tftp-flashing) section.

We conventionally define three different *Types*, each requiring different actions to be taken

### Type 1

- No direct root strategy known (*yet*).
- Easy to replace with a directly rootable firmware, if any.
- Can be rooted indirectly from `Type 2` firmware, if any.

### Type 2

- Direct and easy root strategy is known.
- Can be used for indirect root strategies for other firmware *Types*.

### Type 3

- No direct root strategy known (*yet*).
- Hard to replace with a directly rootable firmware, if any.
- Can be rooted indirectly from `Type 2` firmware, if any.

### Type ???

- No known direct root strategy tested yet, some of them may work just fine.
- May be hard, but still possible, to replace with a directly rootable firmware, if any.
- Could be rooted indirectly from `Type 2` firmware, if any.
- No experience has been shared from users on such firmware.
- If you think you know something more about that please tell us.

## Where to start

Once you understand your current situation

- If you are on a `Type 1` or `Type 2` firmware, please see [Hack Type 1 and 2.](Hack%20Type%201&2/)
- If you are on a `Type 3` or `Type ???` firmware, **and** a `Type 2` firmware is available, please see the [recovery](Recovery/#boot-p-recovery-mode-tftp-flashing) guide to flash it via `BOOT-P` and manually *bankswitch* to it, then start over from the beginning.
- Otherwise, in any other case, you may need to ask for some help from your local community forum threads:
  - AU @ [*whirlpool.net.au*](https://forums.whirlpool.net.au/thread/9vxxl849), IT @ [*ilpuntotecnico.com*](https://www.ilpuntotecnico.com/forum/index.php/board,9.0.html).

## Quick Links

- [Resources](Resources/)
- [Recovery Guides](Recovery/)
- [Firmware Repository](Firmware%20Repository/)
