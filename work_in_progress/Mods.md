# Modifying your Gateway

The aim of this section is to tell you how to safely modify your gateway to produce your desired outcome.

## IMPORTANT, do not SKIP

**Warning:** This process is not supported by the manufacturer or supplier of your Gateway.

There is no way of knowing your situation and the process could break your Gateway or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Finding Buttons

You can find the functions of the buttons on your Gateway to do whatever you want with them.

To do this, you will need:

1. A working, rooted Gateway. See the [Home](../) page for a step by step process.
2. A SSH client, see [Administering OpenWRT from Windows](../Resources/#administering-openwrt-from-windows)

### Locate the Buttons you want to change

Fire up your SSH client of choice and connect to your Gateway using its IP address.

To list the current button configuration, run:

```bash
 uci show button | grep "BTN" | sed -e 's/button.//g'
```

It should have given you an output like this:

```bash
root@mygateway:~# uci show button | grep "BTN" | sed -e 's/button.//g'
reset.'BTN_0'
easy_reset.'BTN_3'
dect_paging.'BTN_2'
dect_registration.'BTN_2'
wifi_onoff.'BTN_1'
wps.'BTN_4'
```

Usually `easy_reset` is the *Status* indicator light on the TG799vac, which is actually a button originally to toggle the rest of the LED's on or off. This is also known as the ECO LED/Button in Technicolor Data Sheets (or ECO functionality).

Now you must locate these buttons.

#### Locating the buttons

Using your eyes, follow these rules to locate the buttons on your Gateway:

- Reset is usually the pinhole *Reset* button on the Gateway
- WiFi On/Off is usually marked *WiFi* or it has a radio-style icon.
- WPS is usually marked with *Pair* or the WPS logo
    - On newer models of gateway, this button is used for DECT paging, DECT pairing and WPS duties
- On the older models, easy reset is the *Status* indicator (as stated above)
