
### Word on Formatting and New Firmware

If you find another firmware for a Technicolor modem, please post it here! Keep an eye on your formatting, follow everyone else's!

### Guessing Firmware URL's

Stock bootloader allows TFTP flashing only with the correct RBI firmware file for the hardware board mnemonic version (something like XXXX-X). 

Firmware filename pattern is ISP specific, so the first thing to do is to find another known one from the same ISP to get a better idea of how it should look like. As you can see from below links, it is often constructed by combining: 

Product Vendor + **Hardware** + CRF + **Firmware**

Using the web interface, advanced view Gateway tile will give you Product Vendor, Hardware Version (aka board mnemonic) and Firmware Version:

```
Global Information
Product Vendor 	 	Technicolor
Product Name 	 	Technicolor TG797n v3
Software Version 	15.3
Firmware Version 	15.53.6469-510-RA
Hardware Version 	DANT-O
```

If the modem is rooted the CRF number can be found in `/rom/etc/config/env`
```
cat /rom/etc/config/env
...
option CONF_VERSION 'CRF483'
...
```

The ISP may have customized firmware version numbers to match their own versioning scheme. If so, check the contents of `/rom/etc/config/versioncusto`.

Once you have guessed it please post it here!

Newer firmware images are often encrypted with a board-specific AES-128 (thus symmetric) key, called OSCK. When flashing via either TFTP or web interface it first decrypt the RBI payload and then flash its contents into one of the internal "banks".

Every firmware image is also authenticated by asymmetric keys used for signing and verifying signature. This second action is performed on boot by the stock bootloader which will fail to boot if the signature verification fails.



### Firmware versions and URLs if available

For simplicity, model names are reported here without irrelevant branding codes. 

For example "DJA0230TLS" where "TLS" stands for "Telstra" is presented here as simply "DJA0230" because it shares the same board mnemonic. 

Other branding codes you could see are "TS" for "Telia Sonera", "MYR" for MyRepublic, and so on. You can safely ignore branding codes.

Type 1/2/3 indicates if it can be rooted directly. 

**Please add this detail when adding firmware versions.**



### TG800vac / VANT-Y

**Telstra - Gateway Max 2**

- 16.3.7567-660-RD (Type 2): 

   - http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF690-16.3.7567-660-RD/vant-y_CRF690-16.3.7567-660-RD.rbi
   


- 17.2.0188-820-RA (Type 1):

   - http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF691-17.2.0188-820-RA/vant-y_CRF691-17.2.0188-820-RA.rbi
   
   

- 17.2.0213-820-RB (Type 1):

   - http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF779-17.2.0213-820-RB/vant-y_CRF779-17.2.0213-820-RB.rbi
   
   

- 17.2.0261-820-RA (Type 2):

   - http://fwstore.bdms.telstra.net/Technicolor_vant-y_CRF851-17.2.0261-820-RA/vant-y_CRF851-17.2.0261-820-RA.rbi



### TG799vac / VANT-F

**Telstra - Gateway Max**

- 15.18.6052-420-RA (Type ???):

    - http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF363-15.18.6052-420-RA/vant-f_CRF363-15.18.6052-420-RA.rbi
    


- 15.53.6886-510-RF (Type 2):

    - http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF540-15.53.6886-510-RF/vant-f_CRF540-15.53.6886-510-RF.rbi
    


- 16.3.7567-660-RG (Type 2): 

    - http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF687-16.3.7567-660-RG/vant-f_CRF687-16.3.7567-660-RG.rbi
    


- 17.2.188-820-RA (Type 1):

    - http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF683-17.2.188-820-RA/vant-f_CRF683-17.2.188-820-RA.rbi
    


- 17.2.0213-820-RC (Type 1):

    - http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF780-17.2.0213-820-RC/vant-f_CRF780-17.2.0213-820-RC.rbi
    


- 17.2.0261-820-RA (Type 2):

    - http://fwstore.bdms.telstra.net/Technicolor_vant-f_CRF852-17.2.0261-820-RA/vant-f_CRF852-17.2.0261-820-RA.rbi




### TG797n v3 / DANT-O

OSCK: Not required.  Firmware images in RBI files are not encrypted with model-specific keys

**Telstra - T-Gateway**

- 16.1.7565-580-RC (Type 2):

    - http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF685-16.1.7565-580-RC/dant-o_CRF685-16.1.7565-580-RC.rbi
    
 

- 15.53.6469-510-RA (Type 2):

    - http://fwstore.bdms.telstra.net/Technicolor_dant-o_CRF483-15.53.6469-510-RA/dant-o_CRF483-15.53.6469-510-RA.rbi
 



### TG789vac referred as v1 / VANT-D

OSCK: Not Known

**WARNING**: This is not for the VANT-6, it is for a VANT-D model. Won't boot on common Australian TG789vac v2/v3

**MST (no-brand) from UNO.UK**

- 16.2.7064 (Type 2):

    - https://uno.help/attachments/690




### TG1 / VANT-5

**iiNet & Internode**

- 15.32.1509-ver1.4 (Type ???):

    - ftp://ftp.iinet.net.au/pub/iinet/firmware/TG-1/VANT-5/vant-5-15.32.1509-ver1.4-CRF434-1049003.rbi 
    
   
   
- 15.53.6627-ver1.6 (Type ???):

    - ftp://ftp.iinet.net.au/pub/iinet/firmware/TG-1/VANT-5/vant-5_15.53.6627-ver1.6-CRF509-1729006.rbi
    
    
   
- 15.53.7004-ver1.7.1 (Type ???):

    - ftp://ftp.iinet.net.au/pub/iinet/firmware/TG-1/VANT-5/vant-5_15.53.7004-ver1.7.1-CRF557-1721003.rbi
    
    
   
- 15.53.8141-ver1.9.0 (Type ???):

    - ftp://ftp.iinet.net.au/pub/iinet/firmware/TG-1/VANT-5/vant-5_15.53.8141-ver1.9.0-CRF775-1721002.rbi
    
    
   
   
### TG789vac v2 / VANT-6

**iiNet**

- 16.3.7196-ver2.0.5 (Type 2):

    - https://app.box.com/s/hp780lnir7xbulk10317ia4n3u3jbnee
    
 

- 16.3.7637-ver2.2.0 (Type 2):

    - https://app.box.com/s/o1oxgju3z8ra1d3sb5nmghyvj2v6cqtq
    
 

- 16.3.7637-ver2.2.1 (Type 2):

    - https://app.box.com/s/phdp7z9sn7s4sk8sooj7rkiv3bql0h01
    
 
 
- 16.3.8046-ver3.0 (Type 1):

     - ftp://ftp.iinet.net.au/pub/iinet/firmware/TG789vacV2/VANT-6/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi
     
     - http://mirror.internode.on.net/pub/internode-support/hardware/tg789/firmware/vant-6_16.3.8046-ver3.0-CRF767-2721002.rbi
     
     

**MST (no-brand) from UNO.UK**

- 17.2.0278 (Type 2):

     - https://uno.help/attachments/732
     



### TG789vac v3 / VBNT-1

**iiNet**

- 18.3.0157-3-2-1-CRF905 (Type ???):

    - No RBI available, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.



### TG789vac v2 HP / VBNT-L

**MyRepublic**

- 16.3.7190 (Type 2):

    - No RBI available, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.



### DJN2130 / VBNT-J

**Telstra - Frontier Gateway**

- 16.3.7413-660-RF (Type 2):

    - **WARNING**: This is not an RBI firmware, it is a raw bank dump, you can't use with tftp or regular firmware upgrade tools https://github.com/kevdagoat/hack-technicolor/raw/master/firmware/vbnt-j_CRF640-16.3.7413-660-RF-bank_dump.xz



- 17.2.0219-820-RA (Type ???):

    - http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF752/vbnt-j_CRF752-17.2.0219-820-RA.rbi



- 17.2.0219-820-RB (Type ???):

    - http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF778-17.2.0219-820-RB/vbnt-j_CRF778-17.2.0219-820-RB.rbi



- 17.2.0261-820-RA (Type 2):

    - http://fwstore.bdms.telstra.net/Technicolor_vbnt-j_CRF847-17.2.0261-820-RA/vbnt-j_CRF847-17.2.0261-820-RA.rbi
    



### DJA0230 / VBNT-V

**Testra - Smart Modem (Gen1)**

- 17.2.0188-820-RA (Type ???):

    - No RBI available, this version has been found on some devices. If you have it on your device please share a dump! Ask for help if you don't know how to get the dump.



- 17.2.0288-820-RA (Type ???):

    - http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF761-17.2.0288-820-RA/vbnt-v_CRF761-17.2.0288-820-RA.rbi
    
 

- 17.2.0320-820-RA (Type ???):

    - http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF795-17.2.0320-820-RA/vbnt-v_CRF795-17.2.0320-820-RA.rbi
 
 

- 17.2.0406-820-RC (Type ???):

    - http://fwstore.bdms.telstra.net/Technicolor_vbnt-v_CRF909-17.2.0406-820-RC/vbnt-v_CRF909-17.2.0406-820-RC.rbi
     



### DJA0231 / VCNT-A

OSCK: Not Known

**Telstra - Smart Modem (Gen2)**

- 18.1.c.0215-950-RA (Type 2):

    - http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF867-18.1.c.0215-950-RA/vcnt-a_CRF867-18.1.c.0215-950-RA.rbi
    
 

- 18.1.c.0241-950-RA (Type 1):

    - http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF899-18.1.c.0241-950-RA/vcnt-a_CRF899-18.1.c.0241-950-RA.rbi
    
 

- 18.1.c.0283-950-RA (Type 1):

    - http://fwstore.bdms.telstra.net/Technicolor_vcnt-a_CRF916-18.1.c.0283-950-RA/vcnt-a_CRF916-18.1.c.0283-950-RA.rbi 
    
 