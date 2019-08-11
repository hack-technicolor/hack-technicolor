# Firmware Repository

## IMPORTANT, do not SKIP

**Warning:** This process is not supported by the manufacturer or supplier of your modem.

There is no way of knowing your situation and the process could break your modem or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Firmware versions and URLs if available

For simplicity, model names are reported here without branding codes.

For example `DJA0230TLS`, where `TLS` stands for `Telstra`, is listed here as simply `DJA0230` since all of them share the same board mnemonic.

Other branding codes you could see worldwide:

| Code | ISP          | Countrie(s)       |
|:----:|:------------:|:------------------|
| TLS  | Telstra      | Australia  (AUS)  |
| TS   | Telia Sonera | Sweden            |
| MYR  | MyRepublic   | AUS and Singapore |
| VDF  | Vodafone     | AUS, EU, US and other |
| FWB  | Fastweb      | Italy             |
| TIS  | Tiscali      | Italy             |
| TI   | TIM          | Italy             |

Type 1/2/3 indicates if it can be rooted directly. Please, **don't miss this important detail** whenever you add a new firmware version to this page.

### TG800vac / VANT-Y

#### Telstra - Gateway Max 2

| Type   | Version          |
|:------:|:-----------------|
| 2      | [16.3.7567-660-RD](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF690-16.3.7567-660-RD/vant-y_CRF690-16.3.7567-660-RD.rbi) |
| 2      | [16.3.7567-660-RD](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF690-16.3.7567-660-RD/vant-y_CRF690-16.3.7567-660-RD.rbi) |
| 1      | [17.2.0188-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF691-17.2.0188-820-RA/vant-y_CRF691-17.2.0188-820-RA.rbi) |
| 1      | [17.2.0213-820-RB](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF779-17.2.0213-820-RB/vant-y_CRF779-17.2.0213-820-RB.rbi) |
| 2      | [17.2.0261-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF851-17.2.0261-820-RA/vant-y_CRF851-17.2.0261-820-RA.rbi) |
| ???    | [17.2.0284-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF914-17.2.0284-820-RA/vant-y_CRF914-17.2.0284-820-RA.rbi) |

### TG799vac / VANT-F

#### Telstra - Gateway Max

| Type   | Version          |
|:------:|:-----------------|
| ???    | [15.18.6052-420-RA](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF363-15.18.6052-420-RA/vant-f_CRF363-15.18.6052-420-RA.rbi) |
| 2      | [15.53.6886-510-RF](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF540-15.53.6886-510-RF/vant-f_CRF540-15.53.6886-510-RF.rbi) |
| 2      | [16.3.7567-660-RG](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF687-16.3.7567-660-RG/vant-f_CRF687-16.3.7567-660-RG.rbi)  |
| 1      | [17.2.188-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF683-17.2.188-820-RA/vant-f_CRF683-17.2.188-820-RA.rbi)  |
| 1      | [17.2.0213-820-RC](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF780-17.2.0213-820-RC/vant-f_CRF780-17.2.0213-820-RC.rbi)  |
| 2      | [17.2.0261-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF852-17.2.0261-820-RA/vant-f_CRF852-17.2.0261-820-RA.rbi)  |

### TG797n v3 / DANT-O

!!! note "OSCK Not Required"
    Firmware images in RBI files for this board are not encrypted with model-specific keys

#### Telstra - T-Gateway

| Type   | Version          |
|:------:|:-----------------|
| 2      | [16.1.7565-580-RC](http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF685-16.1.7565-580-RC/dant-o_CRF685-16.1.7565-580-RC.rbi) |
| 2      | [15.53.6469-510-RA](http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF483-15.53.6469-510-RA/dant-o_CRF483-15.53.6469-510-RA.rbi) |

### TG789vac / VANT-D

!!! warning "Model Warning"
    This is not for the VANT-6, it is for a VANT-D model we often informally refer to as TG789vac **v1**. This won't boot on more common TG789vac v2/v3.

!!! danger "OSCK Not Known"
    Nobody has shared the model specific key for decrypting firmware's for this board. Hence, we generally don't know their contents. If you would like to, please create an issue so we can guide you.

#### MST (no-brand) from UNO.UK

| Type   | Version          |
|:------:|:-----------------|
| 2      | [16.2.7064](https://uno.help/attachments/690) |

### TG789vac v2 / VANT-6

#### iiNet

| Type   | Version          |
|:------:|:-----------------|
| 2      | [16.3.7196-ver2.0.5](https://github.com/kevdagoat/hack-technicolor/blob/master/firmware/vant-6_16.3.7196-ver2.0.5-CRF592-2729004.rbi?raw=true) |
| 2      | [16.3.7637-ver2.2.0](https://github.com/kevdagoat/hack-technicolor/blob/master/firmware/VANT-6_16.3.7637-ver2.2.0-CRF638-2721002%20.rbi?raw=true) |
| 2      | [16.3.7637-ver2.2.1](https://github.com/kevdagoat/hack-technicolor/blob/master/firmware/vant-6_16.3.7637-ver2.2.1-CRF695-2721005.rbi?raw=true) |
| ???    | [16.3.8046-ver2.5.3](ftp://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/.2752ae5a/vant-6_16.3.8046-ver2.5.3-CRF927-2721031.rbi) |
| 1      | [16.3.8046-ver3.0](ftp://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi) or [here](http://mirror.internode.on.net/pub/internode-support/hardware/tg789/firmware/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi) |

#### MST (no-brand) from UNO.UK

| Type   | Version          |
|:------:|:-----------------|
| 2      | [17.2.0278](https://uno.help/attachments/732) |

### TG789vac v3 / VBNT-1

#### iiNet

| Type   | Version          |
|:------:|:-----------------|
| 2      | [18.3.0157-3-2-1](https://github.com/kevdagoat/hack-technicolor/raw/master/firmware/vbnt-1_18.3.0157-3-2-1-CRF905-bank_dump.xz) **This is not an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools** |

### TG789vac v2 HP / VBNT-L

#### MyRepublic

| Type   | Version          |
|:------:|:-----------------|
| 2      | [16.3.7190](https://github.com/kevdagoat/hack-technicolor/raw/master/firmware/vbnt-l_16.3.7190-2761005-bank_dump.xz) **This is not an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools** |

### TG-1 / VANT-5

#### iiNet & Internode

| Type   | Version          |
|:------:|:-----------------|
| ???    | [15.32.1509-ver1.4] **No RBI available, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.** |
| ???    | [15.53.6627-ver1.6](http://mirror.internode.on.net/pub/internode-support/hardware/tg1/firmware/old/vant-5_15.53.6627-ver1.6-CRF509-1729006.rbi) |
| ???    | [15.53.7004-ver1.7.1](http://mirror.internode.on.net/pub/internode-support/hardware/tg1/firmware/old/vant-5_15.53.7004-ver1.7.1-CRF557-1721003.rbi) |
| ???    | [15.53.8141-ver1.9.0](http://mirror.internode.on.net/pub/internode-support/hardware/tg1/firmware/vant-5_15.53.8141-ver1.9.0-CRF775-1721002.rbi) |
| ???    | [15.53.8141-ver1.9.2](ftp://ftp.iinet.net.au/pub/iinet/firmware/TG-1/VANT-5/vant-5_15.53.8141-ver1.9.2-CRF908-1721006.rbi) |

### DJN2130 / VBNT-J

#### Telstra - Frontier Gateway

| Type   | Version          |
|:------:|:-----------------|
| 2      | [16.3.7413-660-RF](https://github.com/kevdagoat/hack-technicolor/raw/master/firmware/vbnt-j_CRF640-16.3.7413-660-RF-bank_dump.xz) **This is not an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools** |
| ???    | [17.2.0219-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF752/vbnt-j_CRF752-17.2.0219-820-RA.rbi) |
| ???    | [17.2.0219-820-RB](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF778-17.2.0219-820-RB/vbnt-j_CRF778-17.2.0219-820-RB.rbi) |
| 2      | [17.2.0261-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF847-17.2.0261-820-RA/vbnt-j_CRF847-17.2.0261-820-RA.rbi) |

### DJA0230 / VBNT-V

#### Telstra - Smart Modem (Gen1)

| Type   | Version          |
|:------:|:-----------------|
| ???    | 17.2.0188-820-RA **No RBI available, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.** |
| ???    | [17.2.0288-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF761-17.2.0288-820-RA/vbnt-v_CRF761-17.2.0288-820-RA.rbi) |
| ???    | [17.2.0320-820-RA](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF795-17.2.0320-820-RA/vbnt-v_CRF795-17.2.0320-820-RA.rbi) |
| ???    | [17.2.0406-820-RC](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF909-17.2.0406-820-RC/vbnt-v_CRF909-17.2.0406-820-RC.rbi) |

### DJA0231 / VCNT-A

!!! danger "OSCK Not Known"
    Nobody has shared the model specific key for decrypting firmware's for this board. Hence, we generally don't know their contents.

#### Telstra - Smart Modem (Gen2)

| Type   | Version          |
|:------:|:-----------------|
| 2      | [18.1.c.0215-950-RA](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF867-18.1.c.0215-950-RA/vcnt-a_CRF867-18.1.c.0215-950-RA.rbi) |
| 1      | [18.1.c.0241-950-RA](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF899-18.1.c.0241-950-RA/vcnt-a_CRF899-18.1.c.0241-950-RA.rbi) |
| 1      | [18.1.c.0283-950-RA](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF916-18.1.c.0283-950-RA/vcnt-a_CRF916-18.1.c.0283-950-RA.rbi) |
| 2      | [18.1.c.0347-950-RC](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF947-18.1.c.0347-950-RC/vcnt-a_CRF947-18.1.c.0347-950-RC.rbi) |

## What to do if your firmware is not listed here

If you want to get an image of a Technicolor firmware which is not listed here you have two main options:

- Try searching very deeply in the web for the original RBI file. Most ISP's keep all firmware's released via remote upgrade on their server, so you may resort into just guessing the right URL

- Try getting root access on a device currently running the firmware you are looking for and grab a dump of its firmware partitions (banks)

- Ask kevdagoat and he will use his CRF Guesser :)

Read further below to get some more useful tips.

If you find another firmware for a Technicolor gateway which is not yet listed, create an Issue so it can be added!

### Guessing RBI Firmware URL's

The stock bootloader allows TFTP flashing only with the correct RBI firmware file for the hardware board mnemonic version (something like XXXX-X).

The Firmware filename combination is usually ISP specific, so the first thing to do is to find another known firmware from the same ISP to get a better idea of how it should look like. As you can see from below links, it is often constructed by combining:

Product Vendor + **Hardware** + CRF + **Firmware**

Using the web interface, go to `Advanced >>Gateway`. In here you will find the Product Vendor, Hardware Version (aka board mnemonic) and Firmware Version:

```bash
Global Information
Product Vendor      Technicolor
Product Name        Technicolor TG797n v3
Software Version    15.3
Firmware Version    15.53.6469-510-RA
Hardware Version    DANT-O
```

If the modem is rooted, the CRF number can be found in `/rom/etc/config/env`

Obtain by running `cat /rom/etc/config/env | grep "CRF"`

```bash
option CONF_VERSION 'CRF483'
```

The ISP may have customized firmware version numbers to match their own versioning scheme. If so, check the contents of `/rom/etc/config/versioncusto`.

Once you have guessed it please create an issue to get it added!

Newer firmware images are often encrypted with a board-specific AES-128 (thus symmetric) key, called OSCK. When flashing via either TFTP or web interface, the gateway first decrypts the RBI and then flashes it to the inactive bank.

Every firmware image is also verified by asymmetric keys. This second action is performed on boot by the stock bootloader which will fail to boot if the signature verification fails.

### Make a raw device dump

Firmware partitions, called banks, contain **signed** and **read-only** squashfs images that get extracted from RBI files during regular firmware flash or upgrade. These images cannot boot on different boards and **do not include any sensitive info** about your own device so they are totally safe to be shared.

In usual dual-bank devices the two firmware partitions are named `bank_1` and `bank_2`, at least one of them has to contain valid firmware in order to boot correctly.

To make a full dump of them you can easily use the built-in busybox `dd` command:

```bash
dd if=/dev/mtd3 of=/tmp/bank_1.dump
dd if=/dev/mtd4 of=/tmp/bank_2.dump
```

Please note the two banks are usually mapped to `mtd3` and `mtd4` respectively, but you should always check yourself by reading contents of `/proc/mtd` from your own device (eg. `cat /proc/mtd`).
