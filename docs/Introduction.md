# Introduction to Homeware Hacking

!!! important "Do not SKIP!"
    !!! warning "WARNING"
        This process is not supported by the manufacturer or supplier of your Gateway.
    !!! danger "DANGER"
        The process could break your Gateway or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Why Hack your Gateway

Devices mentioned above and similar ones are very capable pieces of equipment, each with different features, which may include: 802.11ac, MU-MIMO, ADSL2/VDSL2/eVDSL modem, DECT base station, [FXS](https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station) ports, [FXO](https://en.wikipedia.org/wiki/Foreign_exchange_service_%28telecommunications%29#Foreign_exchange_station) port,  4G backup, [SFP](https://en.wikipedia.org/wiki/Small_form-factor_pluggable_transceiver) slot, etc. They are known to have a high quality internal PCB and low power consumption, for example the TG799vac Xtream uses about 12 watts with WiFi on (typical router config) and 9 watts with WiFi off (typical bridge mode config).

There is usually no *generic* firmware available that will *just* give you access to the Gateway as any other device you would purchase. Most of Technicolor Gateways run customized firmware implementing ISP-specific integrations and get locked down in functionality to match service requirements. This kind of sucks because if you decide to use this device with a different ISP, you are likely to be blocked from doing that, or simply lose some functionality. That is the motivation to hack the device and at least re-enable as many features as possible.

For some other devices, a no-brand firmware exists. They appear as "Technicolor" branded and implement "MST" integration, a default third-party remote management platform for ISP's that do not pay for firmware customization. On such firmware's no regular configuration options are locked out, but getting root access will still open a wider window of possibilities.

The default IP address of the Gateway varies by Gateway model, it could be `10.0.0.138`, `192.168.0.1`, `192.168.1.1`, `10.1.1.1` and so on. Your best option is to get an IP address by DHCP the first time you connect and see what your default Gateway is.

!!! tip "Referring to your gateway"
    Avoid referring to your device by its commercial product name, refer to your device with its unique board mnemonic identifier `XXXX-X` to avoid any potential ambiguity.

## Things you will need

!!! hint
    Check the following points **before** you go offline

1. A `Type 2` RBI from [firmware repository](./Repository/) compatible with your Gateway. If you're on a `Type 2` firmware already and the RBI of your same firmware version is available, pick that one.

2. **Optionally**, another [firmware](./Repository/) file (RBI or bank dump) of any *Type* for the firmware version you would like to stay on at the end of the process for daily usage on your Gateway, like a newer one or some old one you feel more stable and comfortable with.

3. An SSH and SCP client - the famous [PuTTY](https://www.chiark.greenend.org.uk/%7Esgtatham/putty/) is fine for SSH in Windows. [WinSCP](https://winscp.net/eng/download.php) is recommended for SCP. If you have any WSL distribution installed (eg. Cygwin or WSL), or you run a Unix-based OS, you should have both SSH and SCP CLI clients available.

4. A copy of this documentation for reference while you're offline. Just keep a tab open in your browser from a mobile device ***or*** see [Hosting these Docs Locally](https://github.com/hack-technicolor/hack-technicolor/blob/master/Host%20this%20Locally.md).

5. Physical access to the Gateway so you can power cycle it and unplug the WAN/DSL cable while you're going through this process.

6. A *happy* Gateway! If it's in bridge mode or half the tiles are missing (in the GUI), or it's simply not working as expected, just [recover it](../../Recovery/) to get it to a stock state first.

!!! caution "Make sure your Gateway is offline!"
    The ISP could lock you out of the Gateway by pushing a firmware update or configuration script through a landline, WiFi or SIM card connection, until the Gateway is rooted and remote management disabled.

Ensure the Gateway does not have a wired or wireless internet connection. Gateways with 4G Backup, must also have the SIM removed from under the 25mm x 25mm white plastic sticker on the bottom. For instance, on the DJA0231, the SIM card is under a rubber plug above the green port.

Now go back to [Quick Start](../../) and head on to the right guide for your current firmware *Type*.
