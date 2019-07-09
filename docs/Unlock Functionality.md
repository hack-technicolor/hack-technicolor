# Unlock Functionality

## Custom GUI

A highly universal custom GUI with tons (!) of features is available [here](https://github.com/Ansuel/tch-nginx-gui).

**This is highly recommended for users who want the most usability out of their new gateway!**

## Change DNS

This is by far one of the most requested mods.

### Changing the default assigned server from your modems IP address to your DNS server

1. Using `vi` or a program like WinSCP edit /etc/config/DHCP
2. Under

```bash
config dhcp '<interface name>'
```

Add:

```bash
list dhcp_option '6,<dns 1>,<dns 2>'
```

### Redirecting all queries through the gateway to a specific DNS server

1. Using `vi` or a program like WinSCP edit /etc/config/DHCP
2. Under

```bash
config dnsmasq 'main'
```

Add:

```bash
list server '<IP of DNS>'
```

## VoIP Setup

If you want to use VoIP, the following is the quickest way to set it up and remove some broken config that causes calls to be sent out via the FXO port which will be unplugged for everyone in Australia, once you are on NBN.

```bash
# Block 1
# Edit these lines as required, or use the GUI afterwards to fix the values
uci set mmpbxrvsipnet.sip_net.primary_proxy='sipserver'
uci set mmpbxrvsipnet.sip_net.primary_registrar='sipserver'
uci set mmpbxrvsipnet.sip_profile_0.uri='SIPuserName'
uci set mmpbxrvsipnet.sip_profile_0.user_name='SIPuserName'
uci set mmpbxrvsipnet.sip_profile_0.password='SIPpassword'
uci set mmpbxrvsipnet.sip_net.primary_proxy_port='5060'
uci set mmpbxrvsipnet.sip_net.primary_registrar_port='5060'
# End Edit these lines as required
uci set mmpbxrvsipnet.sip_profile_0.enabled='1'
uci set mmpbxbrcmfxsdev.fxs_dev_0.relay_state='1'
uci set mmpbxbrcmfxsdev.fxs_dev_1.relay_state='1'
uci del_list mmpbx.@outgoing_map[0].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[0].priority='2'
uci del_list mmpbx.@outgoing_map[1].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[1].priority='2'
uci del_list mmpbx.@outgoing_map[2].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[2].priority='2'
uci del_list mmpbx.@outgoing_map[3].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[3].priority='2'
uci del_list mmpbx.@outgoing_map[4].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[4].priority='2'
uci del_list mmpbx.@outgoing_map[5].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[5].priority='2'
uci del_list mmpbx.@outgoing_map[6].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[6].priority='2'
uci del_list mmpbx.@outgoing_map[7].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[7].priority='2'
sed -e 's/getrole()=="guest"/getrole()=="admin"/' -i /www/snippets/tabs-voice.lp
uci commit
/etc/init.d/nginx restart
/etc/init.d/mmpbxd restart
```

The following commands are only required for older Telstra firmware i.e. `17.2.0188-820-RA` and earlier.  

They aren't required on newer firmware.  Failures can be ignored. Some of the extra tabs exist in the newer firmware but they hang, so they have been left out!

 We also reset the LAN SIP inbound passwords here for security.

 Please don't post the default passwords in public forums as they could be a security risk for those still using them!

```bash
# Block 2 - most people can skip this
uci add_list web.tvoicecontacts.roles=admin
uci add_list web.tvoicecalllog.roles=admin
uci add_list web.tvoicecapability.roles=admin
uci add_list web.tvoicesipconfig.roles=admin
uci add_list web.ruleset_main.rules=mmpbxinoutgoingmapmodal
uci set web.mmpbxinoutgoingmapmodal=rule
uci set web.mmpbxinoutgoingmapmodal.target='/modals/mmpbx-inoutgoingmap-modal.lp'
uci add_list web.mmpbxinoutgoingmapmodal.roles='admin'
uci add_list web.ruleset_main.rules=mmpbxstatisticsmodal
uci set web.mmpbxstatisticsmodal=rule
uci set web.mmpbxstatisticsmodal.target='/modals/mmpbx-statistics-modal.lp'
uci add_list web.mmpbxstatisticsmodal.roles='admin'
uci del_list mmpbx.@outgoing_map[8].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[8].priority='2'
uci del_list mmpbx.@outgoing_map[9].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[9].priority='2'
uci del_list mmpbx.@outgoing_map[10].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[10].priority='2'
uci del_list mmpbx.@outgoing_map[11].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[11].priority='2'
uci del_list mmpbx.@outgoing_map[12].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[12].priority='2'
uci del_list mmpbx.@outgoing_map[13].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[13].priority='2'
uci del_list mmpbx.@outgoing_map[14].profile='fxo_profile'
uci del_list mmpbx.@outgoing_map[14].priority='2'
uci set mmpbxrvsipdev.sip_dev_0.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_1.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_2.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_3.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_4.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_5.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_6.password=`dd if=/dev/urandom bs=1 | tr -dc A-Za-z0-9 | head -c${1:-10}`
uci set mmpbxrvsipdev.sip_dev_0.push_type='none'
uci set mmpbxrvsipdev.sip_dev_1.push_type='none'
uci set mmpbxrvsipdev.sip_dev_2.push_type='none'
uci set mmpbxrvsipdev.sip_dev_3.push_type='none'
uci set mmpbxrvsipdev.sip_dev_4.push_type='none'
uci set mmpbxrvsipdev.sip_dev_5.push_type='none'
uci set mmpbxrvsipdev.sip_dev_6.push_type='none'
uci delete mmpbxrvsipdev.sip_server.apn_cert_key
uci delete mmpbxrvsipdev.sip_server.apn_interface
sed -e 's/{"mmpbx-sipdevice-modal.lp", T"Sip Device"},/{"mmpbx-sipdevice-modal.lp", T"Sip Device"},\n{"mmpbx-inoutgoingmap-modal.lp", T"In-Out Mapping"},\n{"mmpbx-statistics-modal.lp", T"Statistics"},/' -i /www/snippets/tabs-voice.lp
uci commit
/etc/init.d/nginx restart
/etc/init.d/mmpbxd restart
```

## VoLTE backup voice service & SMS reception

From firmware `17.2.0406-820-RC` on the DJA0230TLS it is possible to use a 4G/VoLTE enabled SIM card in the modem to provide a phone service on the phone ports and to DECT handsets.  

If you have SIP profiles configured, these will be used before the call is routed via the mobile network.  This has been tested with a Telstra 4G SIM; it's unknown if it will work with Vodafone/Optus SIMs due to the internal VoLTE configuration in the 4G module in the modem.

VoLTE status is visible under *Advanced > Telephony > VoLTE tab*; SMS messages are under the *Advanced > Mobile > SMS tab*.

```bash
uci set mmpbxmobilenet.mobile_profile_0.enabled='1'
uci set mobiled_device_specific.@device[0].ims_pdn_autobringup='1'
uci set mobiled_sessions.@session[0].activated='1'
uci set mobiled_sessions.@session[0].autoconnect='1'
uci set mobiled_sessions.@session[0].optional='1'
uci add_list web.ruleset_main.rules=ltesms
uci set web.ltesms=rule
uci set web.ltesms.target='/modals/lte-sms.lp'
uci add_list web.ltesms.roles='admin'
uci commit
/etc/init.d/mmpbxd restart
/etc/init.d/nginx restart
```

## Speeding up VDSL sync times

!!! note "Firmware 16.3"
    Firmware version 16.3.x works the best in terms of xDSL sync and compatibility. Use if available

If you're on VDSL you may be able to speed up your sync times by removing redundant DSL profiles so the integrated modem does not even try to use them.

**Don't do this if you're still on ADSL!**

```bash
uci del_list xdsl.dsl0.profile='8a'
uci del_list xdsl.dsl0.profile='8b'
uci del_list xdsl.dsl0.profile='8c'
uci del_list xdsl.dsl0.profile='8d'
uci del_list xdsl.dsl0.profile='12a'
uci del_list xdsl.dsl0.profile='12b'
uci del_list xdsl.dsl0.multimode='gdmt'
uci del_list xdsl.dsl0.multimode='adsl2annexm'
uci del_list xdsl.dsl0.multimode='adsl2plus'
uci commit
reboot
```

If you wish to add the selections to the web interface to play with later, you can run the following:

```bash
uci add_list web.ruleset_main.rules=xdsllowmodal
uci set web.xdsllowmodal=rule
uci set web.xdsllowmodal.target='/modals/xdsl-low-modal.lp'
uci add_list web.xdsllowmodal.roles='admin'
uci commit
/etc/init.d/nginx restart
```

## Running the TG799vac as the router with a second router behind it (Double NAT)

Double NAT used to break many things, but testing with this configuration shows that most current applications are very tolerant of it. Most applications assume they are on a private network and that their visible IP is not the one they are visible on on the internet via, so if it's nested one more level down via NAT with a DMZ redirecting traffic to the second router's WAN interface it makes very little difference (if this guide is followed)!

There are many reasons you would want to do this:

- You have a complex network setup with a more advanced router running services such as a VPN server and you still want to use the VoIP in the TG799vac so that it can manage the packet priority tagging properly.

- You don't quite trust the TG799vac.

- You want a simpler solution than the 'Using bridge mode with a dedicated PPPoE ethernet port' section below outlines which can be a nightmare to set up and debug if something goes wrong.

- You want easy access to the TG799vac GUI so you can get sync speeds etc at the gateway's IP. This is still possible in bridged mode but it's less straight forward.

- You want to hack the TG799vac with alternate network access if you corrupt the hacked gateway.

Here is how you go setting this up properly:

1. Set up the TG799vac as above fully including VoIP etc and make sure it works to your satisfaction.

2. The TG799vac's default LAN IP on Telstra firmware is `10.0.0.138` and subnet mask `255.255.255.0`. If your inner router also has a default LAN subnet of `10.0.0.0` then it's advised to change one of them (probably the TG799vac so your network will not be disrupted) to a subnet of your choosing such as `10.0.100.0` subnet mask `255.255.255.0`. The rest of this section assumes you moved the TG799vac's LAN IP to `10.0.100.1` subnet mask `255.255.255.0`

3. Add a 'static lease' on the TG799vac under Advanced -> Local Network -> Static Leases with your internal router's WAN MAC address and a suitable ip such as `10.0.100.2`.

4. Connect your inner router's WAN port to one of the TG799vac's LAN ports.

5. Confirm on the inner router that it got `10.0.100.2` as the WAN IP. If it did not, reboot both of them at the same time to get rid of any lingering DHCP leases. If that fails re-check the MAC address of the lease handed out from the TG799vac.

6. On the TG799vac under Advanced -> WAN Services -> DMZ enable it and set the IP to `10.0.100.2` Set up DynDNS if you want to. Save.

7. Turn off WiFi on the TG799vac.

At this point the TG799vac should be transparent to incoming requests which will hit the WAN interface of your internal router and be handled normally.
