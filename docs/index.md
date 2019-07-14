# Hacking Technicolor Gateways

!!! danger "Read Before Proceeding!"
    This process is not supported by the manufacturer or supplier of your gateway. 
    There is no way of knowing your situation and the process could break your gateway or reduce its security, allowing other people into your network. 
    Anyone following this guide accepts full responsibility for any and all of the outcomes.

## Where to start

- Find out what *Type* of firmware is on your gateway from the [Firmware Repository](Firmware%20Repository/)

!!! hint "Can't find your firmware?"
    Any missing or unlisted firmware is `Type ???`. Very old firmware's from the Homeware 10.x era are outside the scope of this wiki. Despite the existence of old "*unlocking*" guides, if newer "*rootable*" firmware exists the gateway can be upgraded by following the `TFTP` flashing guide from the [Recovery](Recovery/#boot-p-recovery-mode-tftp-flashing) section.

If your gateway firmware is:

- `Type 1` or `Type 2` - see [Hack Type 1 and 2](Hack%20Type%201&2/)
- `Type 3` or `Type ???` - see the TFTP [flashing guide](Recovery/#boot-p-recovery-mode-tftp-flashing)
- For any other case, you may need to ask for help on your local community forum threads: AU @ [*whirlpool.net.au*](https://forums.whirlpool.net.au/thread/9vxxl849), IT @ [*ilpuntotecnico.com*](https://www.ilpuntotecnico.com/forum/index.php/board,9.0.html)

## What are these Types?
We conventionally define three different *Types*. This is to make the rooting process simpler.

### Definitions
| Type Number |     Definition     |
|-------------|--------------------|
|      1      |  No direct root strategy known (*yet*). Easy to replace with a directly rootable firmware, if any. Can be rooted indirectly from `Type 2` firmware, if any. |
|      2      |  Direct and easy root strategy is known. Can be used for indirect root strategies for other firmware *Types*. |
|      3      |  No direct root strategy known (*yet*). Hard to replace with a directly rootable firmware, if any. Can be rooted indirectly from `Type 2` firmware, if any. |
|     ???     |   No known direct root strategy tested yet, some of them may work just fine. May be hard, but still possible, to replace with a directly rootable firmware, if any. Could be rooted indirectly from `Type 2` firmware, if any. No experience has been shared from users on such firmware. If you think you know something more about that please tell us. |

