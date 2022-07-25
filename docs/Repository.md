# Firmware Repository

## About model names

For simplicity, model names are reported here without branding codes.

For example `DJA0230TLS`, where `TLS` stands for `Telstra`, is listed here as simply `DJA0230` since they often refers to the same board and device.

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
| TN   | Telenor      | Sweden            |

Type 1/2/3 indicates if it can be rooted directly. For Type 2 only, Root Strategy # indicates how to do it. Please, **don't miss these important details** whenever you add a new firmware version to this page if you know about that.

## What to do if your firmware is not listed here

If you want to get an image of a Technicolor firmware which is not listed here you have two main options:

- Try searching very deeply in the web for the original RBI file. Most ISP's keep all firmware's released via remote upgrade on their server, so you may resort into just guessing the right URL.

- Try getting root access on a device currently running the firmware you are looking for and grab a dump of its firmware partitions (banks).

Read further below to get some more useful tips.

If you find another firmware for a Technicolor gateway which is not yet listed in this page, please, [open a new Issue on GitHub](https://github.com/hack-technicolor/hack-technicolor/issues/new?assignees=&labels=Add+FW+Request&template=add-firmware.md&title=Add+_VERSION_+for+_BOARD_) so it can be added!

### Hunting RBI Firmware URL's

The stock bootloader allows TFTP flashing only with the correct RBI firmware file for the hardware version, usually identified with a board mnemonic string like `XXXX-X`. HAving an RBI file for your Gateway board is therefore really important.

The Firmware filename combination is usually ISP specific, so the first thing to do is to find another known firmware from the same ISP to get a better idea of how it should look like. As you can see from below links, it is often constructed by combining some tokens like product vendor, product name, hardware version, firmware version and special ISP-specific suffixes or prefixes.

The ISP may have customized firmware version numbers to match their own versioning scheme. If so, check the contents of `/rom/etc/config/versioncusto`. Look for any firmware version prefiz, suffic, or complete string overrides.

Using the web interface, go to `Advanced >>Gateway`. In here you will find all basic information like Product Vendor, Hardware Version (aka board mnemonic) and Firmware Version (including any suffix or prefix):

```bash
Global Information
Product Vendor      Technicolor
Product Name        Technicolor TG797n v3
Software Version    15.3
Firmware Version    15.53.6469-510-RA
Hardware Version    DANT-O
```

#### Configuration version

For some ISP's, you may see the configuration version as part of the firmware URL. If the Gateway is rooted, the CONF_VERSION string can be found in `/rom/etc/config/env`

Obtain by running `cat /rom/etc/config/env | grep "CONF_VERSION"`

```bash
option CONF_VERSION 'CRF483'
```

#### Past upgrades history

You can also run

```bash
strings /etc/cwmpd.db
```

Which may yield some firmware URL's your Gateway received as automatic update.

### Make a raw device dump

Firmware partitions, called banks, contain **signed** and **read-only** squashfs images that get extracted from RBI files during regular firmware flash or upgrade. These images cannot boot on different boards and **do not include any sensitive info** about your own device so they are totally safe to be shared.

In usual dual-bank devices the two firmware partitions are named `bank_1` and `bank_2`, at least one of them has to contain valid firmware in order to boot correctly.

Please note the two banks are usually mapped to `mtd3` and `mtd4` respectively, but you should always check yourself by reading contents of `/proc/mtd` from your own device (eg. `cat /proc/mtd`).

To make a full dump of them you can follow [Making dumps](../Resources/#making-dumps) instructions.

## TG582n v2 / DANT-7

### Fastweb

| Type   | Version           | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------|:-----------|:--------------|:-------|
| 2      | 15.28.6169_FW_120 | 2015-07-11 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/15.28.6169_FW_120_TG582nv2.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/dant-7/15.28.6169_FW_120_TG582nv2.rbi.torrent?raw=true) |

## TG582n v2 / DANT-8

### Wind

| Type   | Version           | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------|:-----------|:--------------|:-------|
| 2      | 15.05.5876        | 2015-10-15 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/dant-8/wind-dant-8_15.05.5876-0521002-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |

## TG797n v3 / DANT-O

!!! note "OSCK Not Required"
    Firmware images in RBI files for this board are not encrypted with model-specific keys

A basic ADSL only BCM6362 based gateway. Very useful as SIP ATA.

### Telstra - T-Gateway

| Type   | Version           | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------|:-----------|:--------------|:-------|
| 2      | 15.53.6469-510-RA | 2016-01-07 | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF483-15.53.6469-510-RA/dant-o_CRF483-15.53.6469-510-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/dant-o/dant-o_CRF483-15.53.6469-510-RA.rbi.torrent?raw=true) |
| 2      | 16.1.7565-580-RC  | 2017-06-08 | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF685-16.1.7565-580-RC/dant-o_CRF685-16.1.7565-580-RC.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/dant-o/dant-o_CRF685-16.1.7565-580-RC.rbi.torrent?raw=true) |
| ???    | 16.1.8372-580-RA  | 2018-09-20 | -             | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF869-16.1.8372-580-RA/dant-o_CRF869-16.1.8372-580-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/dant-o/dant-o_CRF869-16.1.8372-580-RA.rbi.torrent?raw=true) |

## TG799vn v2 / VDNT-O

### Telia

| Type   | Version           | Timestamp  | Root Strategy | Mirror |
|:------:|:----------------- |:-----------|:--------------|:-------|
| 2      | 15.51.6436        | 2016-03-21 | #A            | [HTTP](http://131.116.22.230/15516436o1361004closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-o/15516436o1361004closed.rbi.torrent?raw=true) |
| 2      | 15.51.6436        | 2016-05-24 | #A            | [HTTP](http://131.116.22.230/15516436o1361005closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-o/15516436o1361005closed.rbi.torrent?raw=true) |
| 2      | 16.2.7732         | 2017-05-02 | #A            | [HTTP](http://131.116.22.230/1627732o2221004closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-o/1627732o2221004closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339         | 2018-04-16 | #A            | [HTTP](http://131.116.22.230/172339o1901024closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-o/172339o1901024closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405         | 2018-10-17 | -             | [HTTP](http://131.116.22.230/1720405o1901012closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-o/1720405o1901012closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405         | 2020-12-15 | -             | [HTTPS](https://rgw.teliacompany.com:7547/1720405o1901068closed.rbi) - [HTTP](http://131.116.22.230/1720405o1901068closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-o/1720405o1901068closed.rbi.torrent?raw=true) |

> *\* requires access to ISP's management network*

## TG788vn v2 / VDNT-W

### Telmex

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 17.2.0279        | 2017-10-31 | #D            | [HTTP](http://gateway.telmex.com/test/vdnt-w_TG788vnV2_17.2.0279_Upgrade.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-w/vdnt-w_TG788vnV2_17.2.0279_Upgrade.rbi.torrent?raw=true) |
| 2      | 17.2.0360        | 2018-07-16 | #A            | [HTTP](http://gateway.telmex.com/TECHNICOLOR_TG788vnv2_17.2.0360/F_TG788vnv2_17.2.0360.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vdnt-w/F_TG788vnv2_17.2.0360.rbi.torrent?raw=true) |

## TG389ac / GANT-1

### Com Hem

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 15.53.6568         | 2016-09-09 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/gant-1/comhem-gant-1_15.53.6568-1721005-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |

### Teo & Telia Lithuania

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 15.32.6210         | 2015-10-21 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/gant-1/telia-gant-1_15.32.6210-1081007-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools*   |
| 2      | 16.1.7053          | 2016-10-28 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/gant-1/telia-gant-1_16.1.7053-1941003-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools*   |
| 2      | 17.1.7992          | 2018-05-15 | #C #E         | [HTTP](http://10.0.98.250/TG389ac_gant-1_17.1.7992-0001012-20180515151413_PROD.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/gant-1/TG389ac_gant-1_17.1.7992-0001012-20180515151413_PROD.rbi.torrent?raw=true) |

> *\* requires access to ISP's management network*

## TG588v v2 / VANT-2

### MST

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 15.53.6970         | 2016-06-24 | #A #C #D      | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-2/MST%20TG588v%20v2%2015.53.6970-1341001.rbi.torrent?raw=true) |
| 2      | 16.2.7064          | 2016-08-25 | #A #C #D      | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-2/MST%20TG588v%20v2%2016.2.7064.2201001.rbi.torrent?raw=true) |
| 2      | 16.2.7064          | 2017-02-07 | #A #C #D      | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vant-2/mst-vant-2_16.2.7064-2201007-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools*   |

## TG-1 / VANT-5

### iiNet & Internode

| Type   | Version             | Root Strategy | Mirror |
|:------:|:--------------------|:--------------|:-------|
| ???    | 15.32.1509-ver1.4   | -             | *None, **no RBI available**!, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.* |
|  2     | 15.53.6627-ver1.6   | #A #C         | [HTTP](http://mirror.internode.on.net/pub/internode-support/hardware/tg1/firmware/old/vant-5_15.53.6627-ver1.6-CRF509-1729006.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-5/vant-5_15.53.6627-ver1.6-CRF509-1729006.rbi.torrent?raw=true) |
|  2     | 15.53.7004-ver1.7.1 | #A #C         | [HTTP](http://mirror.internode.on.net/pub/internode-support/hardware/tg1/firmware/old/vant-5_15.53.7004-ver1.7.1-CRF557-1721003.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-5/vant-5_15.53.7004-ver1.7.1-CRF557-1721003.rbi.torrent?raw=true) |
|  2     | 15.53.8141-ver1.9.0 | #A #C         | [HTTP](http://mirror.internode.on.net/pub/internode-support/hardware/tg1/firmware/vant-5_15.53.8141-ver1.9.0-CRF775-1721002.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-5/vant-5_15.53.8141-ver1.9.0-CRF775-1721002.rbi.torrent?raw=true) |
|  2     | 15.53.8141-ver1.9.2 | #A #C         | [FTP](ftp://ftp.iinet.net.au/pub/iinet/firmware/TG-1/VANT-5/vant-5_15.53.8141-ver1.9.2-CRF908-1721006.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-5/vant-5_15.53.8141-ver1.9.2-CRF908-1721006.rbi.torrent?raw=true) |

## TG789vac v2 / VANT-6

### MST

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 17.2.0278        | 2018-01-08 | #C #D            | [HTTPS](https://uno.help/attachments/732)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/MST.TG789vac.v2-17.2.278-0901008.rbi.torrent?raw=true) |

> *\* requires access to ISP's network*

### Tiscali

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 16.3.7636        | 2017-04-19 | #A            | [HTTP](http://ftp.tr69.tiscali.it/TR69/vant-6_16.3.7636-2921002-20170419153951-718b590506a915e24be58946f4755c0c617d9c8d.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/vant-6_16.3.7636-2921002-20170419153951-718b590506a915e24be58946f4755c0c617d9c8d.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*

### iiNet & Internode

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 16.3.7196-ver2.0.5 | 2016-10-21 | #A            | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/vant-6_16.3.7196-ver2.0.5-CRF592-2729004.rbi.torrent?raw=true) |
| 2      | 16.3.7637-ver2.2.0 | 2017-05-23 | #A            | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/VANT-6_16.3.7637-ver2.2.0-CRF638-2721002%20.rbi.torrent?raw=true) |
| 2      | 16.3.7637-ver2.2.1 | 2017-06-30 | #A            | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/vant-6_16.3.7637-ver2.2.1-CRF695-2721005.rbi.torrent?raw=true) |
| 1      | 16.3.8046-ver3.0   | 2017-12-18 | -             | [FTP](ftp://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi) - [HTTP](http://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi.torrent?raw=true)
|        | *note: this is officially named `ver3.0` but it is version `2.3.0` indeed* | |
| 2      | 16.3.8046-ver2.5.3 | 2019-03-22 | #C            | [FTP](ftp://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/.2752ae5a/vant-6_16.3.8046-ver2.5.3-CRF927-2721031.rbi) - [HTTP](http://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/.2752ae5a/vant-6_16.3.8046-ver2.5.3-CRF927-2721031.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-6/vant-6_16.3.8046-ver2.5.3-CRF927-2721031.rbi.torrent?raw=true) |

## TG589vac v2 / VANT-8

### MST

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 17.2.0278          | 2018-01-08 | #C #D         | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vant-8/mst-vant-8_17.2.0278-0901009-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools*   |

## TG789vac / VANT-D

!!! danger "OSCK Not Known"
    Nobody has shared the model specific key for decrypting firmware's for this board. Hence, we generally don't know their contents. If you would like to, please create an issue so we can guide you.

### MST

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 16.2.7064          | -          | #A #C         | [HTTPS](https://uno.help/attachments/690)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-d/MST%20TG789vac%2016.2.7064.2201002.rbi.torrent?raw=true) |

> *\* requires access to ISP's network*

## TG799vac / VANT-F

### Telstra - Gateway Max

| Type   | Version           | Root Strategy | Mirror |
|:------:|:------------------|:--------------|:-------|
| ???    | 15.18.6052-420-RA | -             | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF363-15.18.6052-420-RA/vant-f_CRF363-15.18.6052-420-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF363-15.18.6052-420-RA.rbi.torrent?raw=true) |
| 2      | 15.53.6886-510-RF | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF540-15.53.6886-510-RF/vant-f_CRF540-15.53.6886-510-RF.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF540-15.53.6886-510-RF.rbi.torrent?raw=true) |
| 2      | 16.3.7567-660-RG  | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF687-16.3.7567-660-RG/vant-f_CRF687-16.3.7567-660-RG.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF687-16.3.7567-660-RG.rbi.torrent?raw=true) |
| 2      | 17.2.0188-820-RA  | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF683-17.2.188-820-RA/vant-f_CRF683-17.2.188-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF683-17.2.188-820-RA.rbi.torrent?raw=true) |
| 2      | 17.2.0213-820-RC  | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF780-17.2.0213-820-RC/vant-f_CRF780-17.2.0213-820-RC.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF780-17.2.0213-820-RC.rbi.torrent?raw=true) |
| 2      | 17.2.0261-820-RA  | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF852-17.2.0261-820-RA/vant-f_CRF852-17.2.0261-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF852-17.2.0261-820-RA.rbi.torrent?raw=true) |
| ???    | 17.2.0284-820-RA  | -             | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF915-17.2.0284-820-RA/vant-f_CRF915-17.2.0284-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-f/vant-f_CRF915-17.2.0284-820-RA.rbi.torrent?raw=true) |

## TG799vac / VANT-R

### Telia - Trådlös router

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 15.51.6436       | 2016-02-05 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vant-r/telia-vant-r_15.51.6436-1361003-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 15.51.6436       | 2016-05-27 | #A            | [HTTP](http://131.116.22.230/15516436r1361008closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-r/15516436r1361008closed.rbi.torrent?raw=true) |
| 2      | 16.2.7732        | 2017-05-02 | #A            | [HTTP](http://131.116.22.230/1627732r2221004closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-r/1627732r2221004closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339        | 2018-02-28 | #A            | [HTTP](http://131.116.22.230/172339r1021008closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-r/172339r1021008closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339        | 2018-04-16 | #A            | [HTTP](http://131.116.22.230/172339r1021022closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-r/172339r1021022closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405        | 2019-03-29 | -             | [HTTPS](https://rgw.teliacompany.com:7547/172405r1021034closed.rbi) - [HTTP](http://131.116.22.230/172405r1021034closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-r/172405r1021034closed.rbi.torrent?raw=true) |

> *\* requires access to ISP's management network*

## TG789vac v2 HP / VBNT-L

### MyRepublic - WiFi Hub+

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 16.3.7190        | 2016-10-06 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vbnt-l/myrepublic-vbnt-l_16.3.7190-2761005-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 16.3.7190        | 2017-09-07 | #A            | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-l/vbnt-l_16.3.7190-2761003-20170907085601-501361d1f0abcd3206e49f0897c4a6cca07a114d.rbi.torrent?raw=true) |

## TG799vac Xtream / VANT-W

### Telenor

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 15.53.7451       | 2017-03-20 | #A #C         | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vant-w/telenor-vant-w_15.53.7451-1761003-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 17.1.7937        | 2018-10-17 | #C            | [HTTP](http://acs.bredband.com/Technicolor/Technicolor_TG799vacXTREAM/TN_SWE_TG799vacXtream_17.1.7937-1281014-20180313133921-Official.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/TN_SWE_TG799vacXtream_17.1.7937-1281014-20180313133921-Official.rbi.torrent?raw=true) |
| 3      | 18.1.0297        | 2019-10-03 | -             | [HTTP](http://acs.bredband.com/Technicolor/Technicolor_TG799vacXTREAM/TG799vacXtream_18.1.0297-1321001-20191002151007_official_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/TG799vacXtream_18.1.0297-1321001-20191002151007_official_closed.rbi.torrent?raw=true) |
| 3      | 18.1.0297        | 2019-12-13 | -             | [HTTP](http://acs.bredband.com/Technicolor/Technicolor_TG799vacXTREAM/vant-w_18.1.0297-1321006-20191213145958-e139794833dfb6bcc766549899da1ff0e0631539_official.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/vant-w_18.1.0297-1321006-20191213145958-e139794833dfb6bcc766549899da1ff0e0631539_official.rbi.torrent?raw=true) |
| 3      | 18.1.0299        | 2020-05-13 | -             | [HTTP](http://acs.bredband.com/Technicolor/Technicolor_TG799vacXTREAM/vant-w_18.1.0299-1321005-20200513125128-e139794833dfb6bcc766549899da1ff0e0631539_official.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/vant-w_18.1.0299-1321005-20200513125128-e139794833dfb6bcc766549899da1ff0e0631539_official.rbi.torrent?raw=true) |

> *\* requires download password*

### Etisalat

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 17.1.7854        | 2018-02-15 | #C            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vant-w/etisalat-vant-w_17.1.7854-0001025-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |

## TG799vac Xtream / VANT-W

### Telia - Wifi-router Plus

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| ???    | 15.51.6436       | 2015-12-23 | -             | [HTTP](http://131.116.22.230/15516436w1361002closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/15516436w1361002closed.rbi.torrent?raw=true) |
| 2      | 15.51.6436       | 2016-02-26 | #A          | [HTTP](http://131.116.22.230/15516436w1361005closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/15516436w1361005closed.rbi.torrent?raw=true) |
| ???    | 15.51.6436       | 2016-05-24 | -             | [HTTP](http://131.116.22.230/15516436w1361006closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/15516436w1361006closed.rbi.torrent?raw=true) |
| 2      | 16.2.7732        | 2017-05-02 | #A            | [HTTP](http://131.116.22.230/1627732w2221002closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/1627732w2221002closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339        | 2018-02-28 | #A            | [HTTP](http://131.116.22.230/172339w1441004closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/172339w1441004closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339        | 2018-04-16 | #A            | [HTTP](http://131.116.22.230/172339w1441020closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/172339w1441020closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405        | 2019-03-29 | -             | [HTTPS](https://rgw.teliacompany.com:7547/172405w1441030closed.rbi) - [HTTP](http://131.116.22.230/172405w1441030closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-w/172405w1441030closed.rbi.torrent?raw=true) |

> *\* requires access to ISP's management network*

## TG789vac v3 / VBNT-1

### iiNet & Internode

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 18.3.0157-ver3.2.1 | 2018-11-22 | #A            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vbnt-1/iinet-vbnt-1_18.3.0157-ver3.2.1-CRF905-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 18.3.0442-ver3.4.1 | 2019-11-14 | #A            | [FTP](ftp://ftp.iinet.net.au/pub/internode-support/hardware/tg789/firmware/vbnt-1_18.3.0442-ver3.4.1-CRF981-3141011.rbi) - [HTTP](http://ftp.iinet.net.au/pub/internode-support/hardware/tg789/firmware/vbnt-1_18.3.0442-ver3.4.1-CRF981-3141011.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-1/vbnt-1_18.3.0442-ver3.4.1-CRF981-3141011.rbi.torrent?raw=true) |

## TG789vac Xtream 35b / VBNT-F

### Fastweb - FASTGate

| Type   | Version              | Timestamp  | Root Strategy | Mirror |
|:------:|:---------------------|:-----------|:--------------|:-------|
| 2      | 16.1.6637_FW_108_MOS | 2016-03-29 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.1.6637-2081001_FW_108_MOS_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.1.6637-2081001_FW_108_MOS_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.1.6866_FW_111_IAD | 2016-05-19 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.1.6866-2081001_FW_111_IAD_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.1.6866-2081001_FW_111_IAD_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.2.7384_FW_209_IAD | 2017-01-04 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.2.7384-2349001-FW_209-IAD_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.2.7384-2349001-FW_209-IAD_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.2.7384_FW_209_MOS | 2017-01-04 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.2.7384-2349001-FW_209-MOS_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.2.7384-2349001-FW_209-MOS_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.2.7825_FW_212_IAD | 2017-06-27 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.2.7825-2349001-FW_212-IAD_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.2.7825-2349001-FW_212-IAD_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.2.7825_FW_212_MOS | 2017-06-27 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.2.7825-2349001-FW_212-MOS_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.2.7825-2349001-FW_212-MOS_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.2.8706_FW_214_IAD | 2019-04-30 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.2.8706_FW_214_IAD_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.2.8706_FW_214_IAD_TG789vacXtream.rbi.torrent?raw=true) |
| 2      | 16.2.8706_FW_214_MOS | 2019-04-30 | #A            | [HTTP](http://59.0.121.191:8080/ACS-server/file/16.2.8706_FW_214_MOS_TG789vacXtream.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-f/16.2.8706_FW_214_MOS_TG789vacXtream.rbi.torrent?raw=true) |

> *\* requires access to ISP's network*

### TIM San Marino

| Type   | Version              | Timestamp  | Root Strategy | Mirror |
|:------:|:---------------------|:-----------|:--------------|:-------|
| 2      | 16.3.7446            | 2017-03-15 | #A #D         | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vbnt-f/timsm-vbnt-f_16.3.7446-2921002-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |

## TG799vac Xtream / VBNT-H

### Telia - Wifi-router Plus v3

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 16.2.7732        | 2017-05-02 | #A            | [HTTP](http://131.116.22.230/1627732h2221002closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-h/1627732h2221002closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339        | 2018-02-28 | #A            | [HTTP](http://131.116.22.230/172339h1441002closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-h/172339h1441002closed.rbi.torrent?raw=true) |
| 2      | 17.2.0339        | 2018-04-16 | #A            | [HTTP](http://131.116.22.230/172339h1441018closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-h/172339h1441018closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405        | 2019-03-29 | -             | [HTTP](http://131.116.22.230/172405h1441028closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-h/172405h1441028closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405        | 2019-03-29 | -             | [HTTPS](https://rgw.teliacompany.com:7547/172405h1441028closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-h/172405h1441028closed.rbi.torrent?raw=true) |
| 3      | 17.2.0405        | 2019-11-14 | -             | [HTTPS](https://rgw.teliacompany.com:7547/172405h1441042closed.rbi) - [HTTP](http://131.116.22.230/172405h1441042closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-h/172405h1441042closed.rbi.torrent?raw=true) |

> *\* requires access to ISP's management network*

## TG800vac / VANT-Y

### Telstra - Gateway Max 2

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 16.3.7567-660-RD | -          | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF690-16.3.7567-660-RD/vant-y_CRF690-16.3.7567-660-RD.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-y/vant-y_CRF690-16.3.7567-660-RD.rbi.torrent?raw=true) |
| 2      | 17.2.0188-820-RA | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF691-17.2.0188-820-RA/vant-y_CRF691-17.2.0188-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-y/vant-y_CRF691-17.2.0188-820-RA.rbi.torrent?raw=true) |
| 2      | 17.2.0213-820-RB | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF779-17.2.0213-820-RB/vant-y_CRF779-17.2.0213-820-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-y/vant-y_CRF779-17.2.0213-820-RB.rbi.torrent?raw=true) |
| 2      | 17.2.0261-820-RA | -          | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF851-17.2.0261-820-RA/vant-y_CRF851-17.2.0261-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-y/vant-y_CRF851-17.2.0261-820-RA.rbi.torrent?raw=true) |
| ???    | 17.2.0284-820-RA | -          | -             | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF914-17.2.0284-820-RA/vant-y_CRF914-17.2.0284-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-y/vant-y_CRF914-17.2.0284-820-RA.rbi.torrent?raw=true) |

## DGA0130 / VANT-9

### Vodafone - Ultra Hub

| Type   | Version                  | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------------|:-----------|:--------------|:-------|
| 1      | 17.1.7875-CRF731         | 2017-09-04 | -             | [HTTP](http://downloads.vodafone.co.nz/ultrahub_crf731.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-9/ultrahub_crf731.rbi.torrent?raw=true) |
| 2      | 17.1.7988-CRF846-V2.4.6  | 2018-05-09 | *[WIP](https://github.com/hack-technicolor/hack-technicolor/issues/68#issuecomment-578359876)*         | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-9/RC2.4.6_prod_AUTH_vant-9_17.1.7988-2461009-20180510014336.rbi.torrent?raw=true) |
| 3      | 17.1.7988-CRF897-RC2-4-9 | 2018-10-21 | -             | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vant-9/DGA-2-4-9-Prod.rbi.torrent?raw=true) |

## DJN2130 / VBNT-J

### Telstra - Frontier Gateway

| Type   | Version          | Timestamp  | Root Strategy | Mirror |
|:------:|:-----------------|:-----------|:--------------|:-------|
| 2      | 16.3.7413-660-RF | -          | #A #C         | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vbnt-j/telstra-vbnt-j_CRF640-16.3.7413-660-RF-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 17.2.0219-820-RA | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF752/vbnt-j_CRF752-17.2.0219-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-j/vbnt-j_CRF752-17.2.0219-820-RA.rbi.torrent?raw=true) |
| 2      | 17.2.0219-820-RB | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF778-17.2.0219-820-RB/vbnt-j_CRF778-17.2.0219-820-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-j/vbnt-j_CRF778-17.2.0219-820-RB.rbi.torrent?raw=true) |
| 2      | 17.2.0261-820-RA | -          | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF847-17.2.0261-820-RA/vbnt-j_CRF847-17.2.0261-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-j/vbnt-j_CRF847-17.2.0261-820-RA.rbi.torrent?raw=true) |
| 2      | 17.2.0284-820-RA | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF913-17.2.0284-820-RA/vbnt-j_CRF913-17.2.0284-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-j/vbnt-j_CRF913-17.2.0284-820-RA.rbi.torrent?raw=true) |

## DGA4130 / VBNT-K

### MST

| Type   | Version   | Timestamp  | Root Strategy | Mirror |
|:------:|:----------|:-----------|:--------------|:-------|
| 2      | 17.3.0165 | 2018-02-28 | #D            | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/MST%20DGA4130%2017.3.0165.1681007.rbi.torrent?raw=true) |

### Tiscali

| Type   | Version   | Timestamp  | Root Strategy | Mirror |
|:------:|:----------|:-----------|:--------------|:-------|
| ???    | 17.1.7970 | 2018-03-01 | -             | [HTTP](http://ftp.tr69.tiscali.it/TR69/Tiscali_DGA4130_17.1.7970-0001001-20180301141418.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/Tiscali_DGA4130_17.1.7970-0001001-20180301141418.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*

### TIM - Smart Modem Plus

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| ???    | 16.3.7196          | 2016-10-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.0_003_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.0_003_closed.rbi.torrent?raw=true) |
| ???    | 16.3.7271          | 2016-11-01 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.0_004_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.0_004_closed.rbi.torrent?raw=true) |
| ???    | 16.3.7343          | 2016-11-27 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.0_006_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.0_006_closed.rbi.torrent?raw=true) |
| ???    | 16.3.7391          | 2016-12-11 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.2_001_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.2_001_closed.rbi.torrent?raw=true) |
| ???    | 16.3.7498          | 2017-01-19 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.2_002_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.2_002_closed.rbi.torrent?raw=true) |
| 2      | 16.3.7498          | 2017-01-30 | #A            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.2_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 16.3.7573          | 2017-02-20 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.3_001_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.3_001_closed.rbi.torrent?raw=true) |
| ???    | 16.3.7636          | 2017-03-17 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.3_003_closed.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.3_003_closed.rbi.torrent?raw=true) |
| 2      | 16.3.7636          | 2017-04-11 | #A            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.3_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.3_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7745          | 2017-05-12 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTHP_1.0.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7765          | 2017-05-23 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTHP_1.0.1_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7765          | 2017-06-07 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7765          | 2017-06-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_005_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_005_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7841          | 2017-07-17 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_006_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_006_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7882          | 2017-09-25 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_007_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_007_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7882          | 2017-10-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_008_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_008_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7882          | 2017-10-31 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_009_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_009_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0177          | 2017-11-15 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.0_001_CLOSED.rbi.torrent?raw=true) |
| 2      | 17.1.7882          | 2017-11-23 | #A            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.0.4_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.0.4_CLOSED.rbi.torrent?raw=true) |
| 1      | 17.3.0177          | 2018-02-02 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0238          | 2018-03-09 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0268          | 2018-04-05 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.1_002_CLOSED.rbi.torrent?raw=true) |
| 3      | 17.3.0268          | 2018-04-18 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.1_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0307          | 2018-05-23 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.2_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.2_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0331        | 2018-07-05 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.2_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.2_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0337        | 2018-07-18 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.2_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.2_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0337        | 2018-08-31 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.2.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.2.0_001_CLOSED.rbi.torrent?raw=true) |
| 3 🙄   | 17.3.c.0337        | 2018-09-14 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_1.1.2_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_1.1.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0337        | 2018-10-12 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.0_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0349        | 2018-10-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0349        | 2018-11-28 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.0_003_CLOSED.rbi.torrent?raw=true) |
| 1      | 17.3.c.0349        | 2019-01-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0365        | 2019-01-15 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0365        | 2019-03-12 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.1_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.1_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0313          | 2019-04-02 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.1.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.1.0_001_CLOSED.rbi.torrent?raw=true) |
| 1      | 17.3.c.0365        | 2019-04-18 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.0.1_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.0.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0335          | 2019-05-06 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.1.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.1.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0335          | 2019-05-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.1.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.1.0_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0357          | 2019-05-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.1.0_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.1.0_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0376          | 2019-06-27 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.1.0_005_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.1.0_005_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0385          | 2019-07-11 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.0_001_CLOSED.rbi.torrent?raw=true) |
| 1 😉   | 18.3.0376          | 2019-07-19 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.1.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.1.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0445          | 2019-09-30 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.0_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.k.0451        | 2019-10-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.0_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.0_004_CLOSED.rbi.torrent?raw=true) |
| 1      | 18.3.k.0451        | 2019-10-25 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0495          | 2019-12-03 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0547          | 2020-02-20 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.1_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-04-27 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.1_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.1_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-07-01 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.1_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.1_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-07-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTEF_2.2.1_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.2.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0643          | 2021-06-01 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTEF_2.3.0_002_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.3.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-07-01 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTEF_2.3.0_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.3.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-07-19 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTEF_2.3.1_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.3.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-08-13 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTEF_2.3.2_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.3.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0725          | 2021-09-27 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTEF_2.3.3_001_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.3.3_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0725          | 2021-11-03 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTEF_2.3.3_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-k/AGTEF_2.3.3_CLOSED.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*

## DGA4131 / VBNT-O

### Fastweb - FASTGate

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| 2      | 17.2.0214_FW_219   | 2017-10-17 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0214_FW_219_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0214_FW_219_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0245_FW_223   | 2017-11-28 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0245_FW_223_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0245_FW_223_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0245_FW_225   | 2017-12-19 | #B #C         | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vbnt-o/fastweb-vbnt-o_17.2.0245_FW_225-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 17.2.0245_FW_226   | 2017-12-22 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0245_FW_226_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0245_FW_226_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0279_FW_233   | 2018-04-13 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0279_FW_233_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0279_FW_233_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0279_FW_235   | 2018-06-22 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0279_FW_235_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0279_FW_235_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0392_FW_245   | 2018-10-24 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0392_FW_245_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0392_FW_245_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0407_FW_247   | 2018-12-06 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0407_FW_247_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0407_FW_247_DGA4131.rbi.torrent?raw=true) |
| 2      | 17.2.0412_FW_248   | 2018-12-15 | #B #C         | [HTTP](http://59.0.121.191:8080/ACS-server/file/17.2.0412_FW_248_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/17.2.0412_FW_248_DGA4131.rbi.torrent?raw=true) |
| 2      | 18.3.n.0439_FW_258 | 2020-01-21 | #C            | [HTTP](http://59.0.121.191:8080/ACS-server/file/18.3.n.0439_FW_258_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/18.3.n.0439_FW_258_DGA4131.rbi.torrent?raw=true) |
| 2      | 18.3.n.0462_FW_261 | 2020-07-17 | #C            | [HTTP](http://59.0.121.191:8080/ACS-server/file/18.3.n.0462_FW_261_DGA4131.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-o/18.3.n.0462_FW_261_DGA4131.rbi.torrent?raw=true) |

> *\* requires access to ISP's network*

## DGA4132 / VBNT-S

### TIM - TIM HUB

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| ???    | 17.1.7765          | 2017-06-08 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.2_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.2_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7798          | 2017-06-09 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.2_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.2_002_CLOSED.rbi.torrent?raw=true) |
| 2      | 17.1.7798          | 2017-06-09 | #A            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.2_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7812          | 2017-06-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.3_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.3_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7812          | 2017-06-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.3_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.3_002_CLOSED.rbi.torrent?raw=true) |
| 2      | 17.1.7812          | 2017-07-04 | #A            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.3_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.3_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7841          | 2017-07-24 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.4_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.4_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7882          | 2017-09-15 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.5_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.5_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.1.7882          | 2017-09-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.5_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.5_002_CLOSED.rbi.torrent?raw=true) |
| 2      | 17.1.7882          | 2017-10-23 | #A            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.5_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.5_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0165          | 2017-10-23 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.0.6_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.0.6_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0177          | 2017-11-15 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.0_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0177          | 2017-12-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.0_002_CLOSED.rbi.torrent?raw=true) |
| 1      | 17.3.0177          | 2018-02-02 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0238          | 2018-03-09 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0268          | 2018-04-05 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.1_002_CLOSED.rbi.torrent?raw=true) |
| 3      | 17.3.0268          | 2018-04-18 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.1_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.0307          | 2018-05-23 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.2_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.2_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0331        | 2018-07-05 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.2_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.2_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0337        | 2018-07-18 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.2_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.2_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0337        | 2018-08-31 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.2.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.2.0_001_CLOSED.rbi.torrent?raw=true) |
| 3      | 17.3.c.0337        | 2018-09-14 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_1.1.2_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_1.1.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0337        | 2018-10-12 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.0_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0349        | 2018-10-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0349        | 2018-11-28 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.0_003_CLOSED.rbi.torrent?raw=true) |
| 1      | 17.3.c.0349        | 2019-01-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0365        | 2019-01-15 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0365        | 2019-02-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.1_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 17.3.c.0365        | 2019-03-12 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.1_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.1_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0313          | 2019-04-02 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.1.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.1.0_001_CLOSED.rbi.torrent?raw=true) |
| 1      | 17.3.c.0365        | 2019-04-18 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.0.1_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.0.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0335          | 2019-05-06 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.1.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.1.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0335          | 2019-05-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.1.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.1.0_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0357          | 2019-05-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.1.0_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.1.0_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0376          | 2019-06-27 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.1.0_005_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.1.0_005_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0385          | 2019-07-11 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.0_001_CLOSED.rbi.torrent?raw=true) |
| 1      | 18.3.0376          | 2019-07-19 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.1.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.1.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0412          | 2019-09-11 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0445          | 2019-09-30 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.0_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.k.0451        | 2019-10-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.0_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.0_004_CLOSED.rbi.torrent?raw=true) |
| 1      | 18.3.k.0451        | 2019-10-25 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0495          | 2019-12-02 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0547          | 2020-02-20 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.1_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-04-27 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.1_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.1_003_CLOSED.rbi.torrent?raw=true) |
| 1      | 19.4.0297          | 2020-05-20 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.2_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.2_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-07-01 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.1_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.1_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-07-21 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.1_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-11-04 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.3_001_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.3_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-11-13 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.3_002_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.3_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 18.3.0600          | 2020-11-20 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHP_2.2.3_003_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.2.3_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0643          | 2021-06-01 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHP_2.3.0_002_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.3.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-07-01 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHP_2.3.0_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.3.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-07-19 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHP_2.3.1_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.3.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-08-13 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHP_2.3.2_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.3.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0725          | 2021-09-27 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHP_2.3.3_001_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.3.3_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0725          | 2021-11-03 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHP_2.3.3_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vbnt-s/AGTHP_2.3.3_CLOSED.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*

## DGA4134 / VCNT-J

### Net Lynk

| Type   | Version                 | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------------|:-----------|:--------------|:-------|
| 2      | 19.4.0447               | 2021-05-25 | #C            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vcnt-j/mst-vcnt-j_19.4.0477-4381031-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |

## DJA0230 / VBNT-V

### Telstra - Smart Modem (Gen1)

| Type   | Version             | Timestamp  | Root Strategy | Mirror |
|:------:|:--------------------|:-----------|:--------------|:-------|
| 2      | 17.2.0188-820-RA    | -          | #C            | *No RBI available, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.* |
| 2      | 17.2.0288-820-RA    | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF761-17.2.0288-820-RA/vbnt-v_CRF761-17.2.0288-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF761-17.2.0288-820-RA.rbi.torrent?raw=true) |
| 2      | 17.2.0320-820-RA    | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF795-17.2.0320-820-RA/vbnt-v_CRF795-17.2.0320-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF795-17.2.0320-820-RA.rbi.torrent?raw=true) |
| 2      | 17.2.0406-820-RC    | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF909-17.2.0406-820-RC/vbnt-v_CRF909-17.2.0406-820-RC.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF909-17.2.0406-820-RC.rbi.torrent?raw=true) |
| 2      | 17.2.0468-820-RA    | 2019-07-19 | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF928-17.2.0468-820-RA/vbnt-v_CRF928-17.2.0468-820-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF928-17.2.0468-820-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0429-950-RA  | 2019-09-20 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF979-18.1.c.0429-950-RA/vbnt-v_CRF979-18.1.c.0429-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF979-18.1.c.0429-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0443-950-RA  | 2019-10-21 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF979_18.1.c.0443-950-RA/vbnt-v_CRF979_18.1.c.0443-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF979_18.1.c.0443-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0462-950-RA  | 2020-02-14 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_vbnt-v_CRF993-18.1.c.0462-950-RA/vbnt-v_CRF993-18.1.c.0462-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_CRF993-18.1.c.0462-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0514-950-RB  | 2020-06-02 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_ACR-14-18.1.c.0514-950-RB/vbnt-v_ACR-14-18.1.c.0514-950-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_ACR-14-18.1.c.0514-950-RB.rbi.torrent?raw=true) |
| 2      | 18.1.c.0549-MR17-RB | 2020-09-01 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_18.1.c.0549-MR17-RB/vbnt-v_18.1.c.0549-MR17-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_18.1.c.0549-MR17-RB.rbi.torrent?raw=true) |
| 2      | 20.3.c.0329-MR19-RA | 2021-05-28 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_20.3.c.0329-MR19-RA/vbnt-v_20.3.c.0329-MR19-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_20.3.c.0329-MR19-RA.rbi.torrent?raw=true) (*[This version has a broken adsl_phy.bin](https://github.com/hack-technicolor/hack-technicolor/issues/180)*) |
| 2      | 20.3.c.0329-MR19-RB | 2021-07-19 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_20.3.c.0329-MR19-RB/vbnt-v_20.3.c.0329-MR19-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_20.3.c.0329-MR19-RB.rbi.torrent?raw=true) |
| 2      | 20.3.c.0389-MR20-RA | 2021-11-10 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_20.3.c.0389-MR20-RA/vbnt-v_20.3.c.0389-MR20-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_20.3.c.0389-MR20-RA.rbi.torrent?raw=true) |
| 3      | 20.3.c.0432-MR21-RA | 2022-03-15 | -             | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_20.3.c.0432-MR21-RA/vbnt-v_20.3.c.0432-MR21-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-v/vbnt-v_20.3.c.0432-MR21-RA.rbi.torrent?raw=true) |


## DWA0120 / VBNT-2

### MST

| Type   | Version                 | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------------|:-----------|:--------------|:-------|
| 2      | 18.3.0278               | 2019-06-14 | #C            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vbnt-2/mst-vbnt-2_18.3.0278-2741042-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |

## DNA0130 / VBNT-Z

### Vodafone - Ultra Hub Plus

| Type   | Version                 | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------------|:-----------|:--------------|:-------|
| 2      | 17.4.0182CRF877-RC2.0.1 | 2018-11-19 | *[WIP](https://github.com/hack-technicolor/hack-technicolor/issues/68#issuecomment-578359876)*         | [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vbnt-z/UHP-2-0-1-Prod.rbi.torrent?raw=true) |

## DJA0231 / VCNT-A

### Telstra - Smart Modem (Gen2)

| Type   | Version              | Timestamp  | Root Strategy | Mirror |
|:------:|:---------------------|:-----------|:--------------|:-------|
| 2      | 18.1.c.0215-950-RA   | -          | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF867-18.1.c.0215-950-RA/vcnt-a_CRF867-18.1.c.0215-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF867-18.1.c.0215-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0241-950-RA   | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF899-18.1.c.0241-950-RA/vcnt-a_CRF899-18.1.c.0241-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF899-18.1.c.0241-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0283-950-RA   | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF916-18.1.c.0283-950-RA/vcnt-a_CRF916-18.1.c.0283-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF916-18.1.c.0283-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0347-950-RC   | -          | #A #C         | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF947-18.1.c.0347-950-RC/vcnt-a_CRF947-18.1.c.0347-950-RC.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF947-18.1.c.0347-950-RC.rbi.torrent?raw=true) |
| 2      | 18.1.c.0384-950-RB   | -          | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF964-18.1.c.0384-950-RB/vcnt-a_CRF964-18.1.c.0384-950-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF964-18.1.c.0384-950-RB.rbi.torrent?raw=true) |
| 2      | 18.1.c.0443-950-RB   | 2019-11-20 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF983-18.1.c.0443-950-RB/vcnt-a_CRF983-18.1.c.0443-950-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF983-18.1.c.0443-950-RB.rbi.torrent?raw=true) |
| 2      | 18.1.c.0462-950-RA   | 2020-01-22 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF991-18.1.c.0462-950-RA/vcnt-a_CRF991-18.1.c.0462-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF991-18.1.c.0462-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0462-950-RB   | 2020-02-14 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF994-18.1.c.0462-950-RB/vcnt-a_CRF994-18.1.c.0462-950-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_CRF994-18.1.c.0462-950-RB.rbi.torrent?raw=true) |
| 2      | 18.1.c.0514-950-RB   | 2020-06-02 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_ACR-13-18.1.c.0514-950-RB/vcnt-a_ACR-13-18.1.c.0514-950-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_ACR-13-18.1.c.0514-950-RB.rbi.torrent?raw=true) |
| 2      | 18.1.c.0543-950-RA   | 2020-08-04 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_18.1.c.0543-950-RA/vcnt-a_18.1.c.0543-950-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_18.1.c.0543-950-RA.rbi.torrent?raw=true) |
| 2      | 18.1.c.0585-MR7.1-RA | 2020-11-17 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_18.1.c.0585-MR7.1-RA.rbi/vcnt-a_18.1.c.0585-MR7.1-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_18.1.c.0585-MR7.1-RA.rbi.torrent?raw=true) |
| 2      | 20.3.c.0329-MR19-RA  | 2021-05-28 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_20.3.c.0329-MR19-RA/vcnt-a_20.3.c.0329-MR19-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_20.3.c.0329-MR19-RA.rbi.torrent?raw=true) (*[This version has a broken adsl_phy.bin](https://github.com/hack-technicolor/hack-technicolor/issues/180)*) |
| 2      | 20.3.c.0329-MR19-RB  | 2021-07-19 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_20.3.c.0329-MR19-RB/vcnt-a_20.3.c.0329-MR19-RB.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_20.3.c.0329-MR19-RB.rbi.torrent?raw=true) |
| 2      | 20.3.c.0389-MR20-RA  | 2021-11-10 | #C            | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_20.3.c.0389-MR20-RA/vcnt-a_20.3.c.0389-MR20-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_20.3.c.0389-MR20-RA.rbi.torrent?raw=true) |
| 3      | 20.3.c.0432-MR21-RA | 2022-03-15 | -             | [HTTP](http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_20.3.c.0432-MR21-RA/vcnt-a_20.3.c.0432-MR21-RA.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-a/vcnt-a_20.3.c.0432-MR21-RA.rbi.torrent?raw=true) |

## DGA2231 / VCNT-C

### TIM

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| ???    | 18.3.0140          | 2018-09-05 | -             | [HTTPS](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTSA_1.0.0_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-c/AGTSA_1.0.0_001_CLOSED.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*

### Telmex

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| ???    | 18.3.g.0301        | 2019-10-28 | -             | [HTTP](http://gateway.telmex.com/test/DGA2231_18.3.G.0301/DGA2231_vcnt-c_18.3.g.0301-official.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-c/DGA2231_vcnt-c_18.3.g.0301-official.rbi.torrent?raw=true) |
| ???    | 18.3.g.0301        | 2021-03-08 | -             | [HTTP](http://gateway.telmex.com/Pruebas_Technicolor_DGA2231/vcnt-c_DGA2231TMX_18.3.g.0301v3_ff8f20c8.rbi) - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-c/vcnt-c_DGA2231TMX_18.3.g.0301v3_ff8f20c8.rbi.torrent?raw=true) |

### MST

| Type   | Version                 | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------------|:-----------|:--------------|:-------|
| 2      | 18.1.0203               | 2018-08-08 | #C            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vcnt-c/mst-vcnt-c_18.1.0203-1641038-bank_dump.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |



## DGA4331 / VCNT-3

### TIM - TIM HUB+

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| ???    | 19.4.0285          | 2020-05-08 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.0_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0306          | 2020-06-03 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.0_003_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.0_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0335          | 2020-06-29 | -            | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.0_004_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.0_004_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0351          | 2020-07-17 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.0_005_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.0_005_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0351          | 2020-07-29 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.0_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0393          | 2020-09-02 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.1_001_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0421          | 2020-09-25 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.1_002_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.1_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0421          | 2020-10-15 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.1_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0539          | 2021-03-10 | -             | [HTTP](http://156.54.126.84:80/Firmware/TR069/AGThomson/AGTHF_1.0.2_CLOSED.rbi)* - [Torrent](https://github.com/hack-technicolor/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.0.2_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0623          | 2021-05-07 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHF_1.1.0_001_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.1.0_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0643          | 2021-06-01 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHF_1.1.0_002_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.1.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-06-29 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHF_1.1.0_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.1.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0666          | 2021-07-22 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHF_1.1.1_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.1.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0751          | 2021-10-11 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/AGTHF_1.1.2_001_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vcnt-3/AGTHF_1.1.2_001_CLOSED.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*

## DWA0122 / VCNT-2

### Belong

| Type   | Version                 | Timestamp  | Root Strategy | Mirror |
|:------:|:------------------------|:-----------|:--------------|:-------|
| 2 😁   | 19.4.0381-RA            | 2020-09-07 | #C            | [HTTPS](https://github.com/hack-technicolor/tch-bank-dumps/raw/master/vcnt-2/belong-vcnt-2_19.4.0381-4961004-bank_dump.lfs.xz) - *note: this **IS NOT** an RBI firmware, it is a raw bank dump, you can't use with TFTP or regular firmware upgrade tools* |
| 2      | 19.4.1.0393-MR1-RB      | 2022-03-29 | #C            | [HTTPS](https://fw.ax.belong.com.au/vcnt-2_19.4.l.0393-MR1-RB.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/vcnt-2/vcnt-2_19.4.l.0393-MR1-RB.rbi.torrent?raw=true) |

> *\* requires access to ISP's network*

## OWA0131 / GCNT-N

### TIM - EasyMesh Repeater 6

| Type   | Version            | Timestamp  | Root Strategy | Mirror |
|:------:|:-------------------|:-----------|:--------------|:-------|
| ??? 🤔 | 19.4.0512          | 2021-01-08 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.0_002_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.0_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0551          | 2021-03-01 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.0_003_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.0_003_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0551          | 2021-03-08 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.0_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.0_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0615          | 2021-04-29 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.1_001_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.1_001_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0649          | 2021-06-11 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.1_002_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.1_002_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0649          | 2021-06-22 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.1_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.1_CLOSED.rbi.torrent?raw=true) |
| ???    | 19.4.0677          | 2021-07-28 | -             | [HTTP](https://fw.regman-tl.interbusiness.it:11443/Firmware/TR069/AGThomson/RPTEM_1.0.4_CLOSED.rbi)* - [Torrent](https://github.com/kevdagoat/hack-technicolor/blob/master/torrents/gcnt-n/RPTEM_1.0.4_CLOSED.rbi.torrent?raw=true) |

> *\* requires access to ISP's network and download password*
