# Unlock Functionality

## IMPORTANT, do not SKIP

**Warning:** This process is not supported by the manufacturer or supplier of your Gateway.

There is no way of knowing your situation and the process could break your Gateway or reduce its security allowing other people into your network. Anyone following this guide accepts full responsibility for the outcomes.

## Unlock Web GUI Tiles

Tested on Telstra Gateways

```bash
# Unlock Web Interface Tiles (Telstra Devices)
uci add_list web.ruleset_main.rules=iproutesmodal
uci set web.iproutesmodal=rule
uci set web.iproutesmodal.target='/modals/iproutes-modal.lp'
uci add_list web.iproutesmodal.roles='admin'
uci add_list web.ruleset_main.rules=systemmodal
uci set web.systemmodal=rule
uci set web.systemmodal.target='/modals/system-modal.lp'
uci add_list web.systemmodal.roles='admin'
uci add_list web.ruleset_main.rules=relaymodal
uci set web.relaymodal=rule
uci set web.relaymodal.target='/modals/relay-modal.lp'
uci add_list web.relaymodal.roles='admin'
uci add_list web.ruleset_main.rules=natalghelpermodal
uci set web.natalghelpermodal=rule
uci set web.natalghelpermodal.target='/modals/nat-alg-helper-modal.lp'
uci add_list web.natalghelpermodal.roles='admin'
uci add_list web.ruleset_main.rules=diagnosticstcpdumpmodal
uci set web.diagnosticstcpdumpmodal=rule
uci set web.diagnosticstcpdumpmodal.target='/modals/diagnostics-tcpdump-modal.lp'
uci add_list web.diagnosticstcpdumpmodal.roles='admin'
sed -e 's/session:hasAccess("\/modals\/diagnostics-network-modal.lp")/session:hasAccess("\/modals\/diagnostics-network-modal.lp") and \n session:hasAccess("\/modals\/diagnostics-tcpdump-modal.lp")/' -i /www/cards/009_diagnostics.lp
sed -e 's^alt="network"></div></td></tr>\\^alt="network"></div></td>\\\n <td><div data-toggle="modal" data-remote="modals/diagnostics-tcpdump-modal.lp" data-id="diagnostics-tcpdump-modal"><img href="#" rel="tooltip" data-original-title="TCPDUMP" src="/img/network_sans-32.png" alt="network"></div></td></tr>\\^' -i /www/cards/009_diagnostics.lp
sed -e 's/{"logviewer-modal.lp", T"Log viewer"},/{"logviewer-modal.lp", T"Log viewer"},\n {"diagnostics-tcpdump-modal.lp", T"tcpdump"},\n/' -i /www/snippets/tabs-diagnostics.lp
sed -e 's/if currentuserrole == "guest" /if currentuserrole == "admin" /' -i /www/docroot/modals/gateway-modal.lp
uci commit
# Enable Unsigned config export and Firmware upgrade in Web GUI
uci set system.config.export_plaintext='1'
uci set system.config.export_unsigned='1'
uci set system.config.import_plaintext='1'
uci set system.config.import_unsigned='1'
uci set web.uidefault.upgradefw_role='admin'
uci add_list web.parentalblock.roles='admin'
uci commit
```

## Custom GUI

A highly universal custom GUI with tons (!) of features is [available here](https://github.com/Ansuel/tch-nginx-gui). If you encounter any issues after installing this mod, please open a [GitHub issue here](https://github.com/Ansuel/tch-nginx-gui/issues) to ask for support.

This is recommended for users who don't fear a few bugs and want the most out-of-box usability from their modded gateway.

!!! info "Recovery options"
    Since version `9.5.60` this mod is compatible with the same *optimal* bank plan suggested in this wiki. Please, read Recovery page carefully and get familiar with recovery strategies available when this special planning is in order. The easy and reliable Recovery for optimal bank plan users will also be available for you.

!!! info "Different RTFD behavior"
    Any RTFD attempt will not uninstall this mod completely. Since version `9.5.60` you will need to repeat RTFD two times in a row to bring back the gateway to the same state a normal RTFD would.

!!! danger "This mod has permanently bricked Gateways before"
    In older versions of this GUI, it has bricked low space devices like the TG799vac.
    It now has a brick prevention method in place so this is not so much of a worry.
    Do not use versions older than `9.5.60`.

## Change DNS

This is by far one of the most requested mods.

### Changing the default assigned server from your Gateways IP address to your DNS server

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

1. Using `vi` or a program like WinSCP edit /etc/config/dhcp
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

!!! hint
    This code will not work for some Gateway / Firmware combinations (eg [DJA0230](https://forums.whirlpool.net.au/thread/9vxxl849?p=204#r64998059)). Use:
    ```uci del_list mmpbx.@outgoing_map[*].priority='3' instead of '2'```

```bash
# Block 1
# Edit these lines as required, or use the GUI afterwards to fix the values
uci set mmpbxrvsipnet.sip_profile_0=profile
uci set mmpbxrvsipnet.sip_profile_0.enabled='1'
uci set mmpbxrvsipnet.sip_profile_0.network='sip_net'
uci set mmpbxrvsipnet.sip_profile_0.user_name='UserName0'
uci set mmpbxrvsipnet.sip_profile_0.display_name='DisplayName0'
uci set mmpbxrvsipnet.sip_profile_0.password='Password0'
uci set mmpbxrvsipnet.sip_profile_0.uri='Uri0'
uci set mmpbxrvsipnet.sip_net.primary_proxy='primary.proxy.0'
uci set mmpbxrvsipnet.sip_net.user_friendly_name='SIP Network 0'
uci set mmpbxrvsipnet.sip_net.local_port='5070'
uci set mmpbxrvsipnet.sip_net.primary_registrar='primary.registrar.0'
uci set mmpbxrvsipnet.sip_net.primary_proxy_port='5060'
uci set mmpbxrvsipnet.sip_net.reg_expire='3600'
uci set mmpbxrvsipnet.sip_net.primary_registrar_port='5060'
uci set mmpbxrvsipnet.sip_profile_0.enabled='1'
uci set mmpbxbrcmfxsdev.fxs_dev_0.relay_state='1'
uci set mmpbxbrcmfxsdev.fxs_dev_1.relay_state='1'
uci set mmpbxrvsipnet.sip_profile_1.enabled='1'
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
```
## Unlocking the option to add a second SIP Network Provider

```bash
# Block 3A (Optional: Adding 2nd SIP Provider)
uci set mmpbx.sip_net_1=network
uci set mmpbx.sip_net_1.config='uci set mmpbxrvsipnet'
uci commit
uci set mmpbxrvsipnet.sip_net_1=network
uci set mmpbxrvsipnet.sip_net_1.session_expires='180'
uci set mmpbxrvsipnet.sip_net_1.no_answer_response='480'
uci set mmpbxrvsipnet.sip_net_1.dtmf_relay_translation='0'
uci set mmpbxrvsipnet.sip_net_1.call_waiting_reject_response='486'
uci set mmpbxrvsipnet.sip_net_1.cac='-1'
uci set mmpbxrvsipnet.sip_net_1.ingress_media_timeout='1000'
uci set mmpbxrvsipnet.sip_net_1.timer_D='50000'
uci set mmpbxrvsipnet.sip_net_1.privacy_handling='apply'
uci set mmpbxrvsipnet.sip_net_1.timer_J='32000'
uci set mmpbxrvsipnet.sip_net_1.reliable_provisional_response='supported'
uci set mmpbxrvsipnet.sip_net_1.transparent_soc_transmission='0'
uci set mmpbxrvsipnet.sip_net_1.switch_back_to_primary_proxy_timer='0'
uci set mmpbxrvsipnet.sip_net_1.transport_type='UDP'
uci set mmpbxrvsipnet.sip_net_1.control_qos_field='dscp'
uci set mmpbxrvsipnet.sip_net_1.timer_T4='5000'
uci set mmpbxrvsipnet.sip_net_1.realtime_qos_field='dscp'
uci set mmpbxrvsipnet.sip_net_1.escape_hash='1'
uci set mmpbxrvsipnet.sip_net_1.dtmf_relay='auto'
uci set mmpbxrvsipnet.sip_net_1.realtime_qos_value='af42'
uci set mmpbxrvsipnet.sip_net_1.fail_behaviour='stop'
uci set mmpbxrvsipnet.sip_net_1.escape_star='0'
uci set mmpbxrvsipnet.sip_net_1.timer_F='32000'
uci set mmpbxrvsipnet.sip_net_1.primary_proxy_port='5060'
uci set mmpbxrvsipnet.sip_net_1.realm_check='0'
uci set mmpbxrvsipnet.sip_net_1.reg_expire='3600'
uci set mmpbxrvsipnet.sip_net_1.reg_back_off_timeout='180'
uci set mmpbxrvsipnet.sip_net_1.secondary_proxy_port='0'
uci set mmpbxrvsipnet.sip_net_1.timer_B='32000'
uci set mmpbxrvsipnet.sip_net_1.uri_clir_format='standard'
uci set mmpbxrvsipnet.sip_net_1.reg_expire_T_before='1'
uci set mmpbxrvsipnet.sip_net_1.re_registration_mode='standard'
uci set mmpbxrvsipnet.sip_net_1.timer_T1='500'
uci set mmpbxrvsipnet.sip_net_1.call_waiting_provisional_response='182'
uci set mmpbxrvsipnet.sip_net_1.forking_mode='default'
uci set mmpbxrvsipnet.sip_net_1.interface='wan'
uci set mmpbxrvsipnet.sip_net_1.session_timer='enabled'
uci set mmpbxrvsipnet.sip_net_1.control_qos_value='ef'
uci set mmpbxrvsipnet.sip_net_1.secondary_registrar_port='5060'
uci set mmpbxrvsipnet.sip_net_1.min_period_proxy_redundancy='0'
uci set mmpbxrvsipnet.sip_net_1.min_session_expires='90'
uci set mmpbxrvsipnet.sip_net_1.primary_registrar_port='5060'
uci set mmpbxrvsipnet.sip_net_1.timer_T2='4000'
uci set mmpbxrvsipnet.sip_net_1.rport_in_via='1'
uci set mmpbxrvsipnet.sip_net_1.provisional_timer='180'
uci set mmpbxrvsipnet.sip_net_1.rejection_response='486'
uci commit
uci set mmpbxrvsipnet.sip_net_1.primary_proxy='primary.proxy.1'
uci set mmpbxrvsipnet.sip_net_1.user_friendly_name='SIP Network 1'
uci set mmpbxrvsipnet.sip_net_1.local_port='5071'
uci set mmpbxrvsipnet.sip_net_1.primary_registrar='primary.registrar.1'
uci set mmpbxrvsipnet.sip_net_1.domain_name='domain.name.1'
uci commit
/etc/init.d/nginx restart
/etc/init.d/mmpbxd restart
```
Setting SIP profiles which can be easily edited via GUI for multiple accounts per VOIP provider

```bash
# SIP Account defaults
# Edit these lines as required, or use the GUI afterwards to fix the values
uci set mmpbxrvsipnet.sip_profile_1=profile
uci set mmpbxrvsipnet.sip_profile_1.enabled='1'
uci set mmpbxrvsipnet.sip_profile_1.network='sip_net_1'
uci set mmpbxrvsipnet.sip_profile_1.user_name='UserName1'
uci set mmpbxrvsipnet.sip_profile_1.display_name='DisplayName1'
uci set mmpbxrvsipnet.sip_profile_1.password='Password1'
uci set mmpbxrvsipnet.sip_profile_1.uri='Uri1'
uci set mmpbxrvsipnet.sip_profile_2=profile
uci set mmpbxrvsipnet.sip_profile_2.enabled='1'
uci set mmpbxrvsipnet.sip_profile_2.network='sip_net'
uci set mmpbxrvsipnet.sip_profile_2.user_name='UserName2'
uci set mmpbxrvsipnet.sip_profile_2.display_name='DisplayName2'
uci set mmpbxrvsipnet.sip_profile_2.password='Password2'
uci set mmpbxrvsipnet.sip_profile_2.uri='Uri2'
uci set mmpbxrvsipnet.sip_profile_3=profile
uci set mmpbxrvsipnet.sip_profile_3.enabled='1'
uci set mmpbxrvsipnet.sip_profile_3.network='sip_net_1'
uci set mmpbxrvsipnet.sip_profile_3.user_name='UserName3'
uci set mmpbxrvsipnet.sip_profile_3.display_name='DisplayName3'
uci set mmpbxrvsipnet.sip_profile_3.password='Password3'
uci set mmpbxrvsipnet.sip_profile_3.uri='Uri3'
uci commit
```

## VoLTE backup voice service & SMS reception

From firmware `17.2.0406-820-RC` on the DJA0230TLS it is possible to use a 4G/VoLTE enabled SIM card in the Gateway to provide a phone service on the phone ports and to DECT handsets.  

If you have SIP profiles configured, these will be used before the call is routed via the mobile network.  This has been tested with a Telstra 4G SIM; it's unknown if it will work with Vodafone/Optus SIMs due to the internal VoLTE configuration in the 4G module in the Gateway.

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

## Enable VOIP for both SIP providers while on 4G Backup (Frontier DJN2130 & SMG1 DJA0230)

```bash
# Enable VOIP while on backup
uci set mmpbxrvsipnet.sip_net.interface='lan'
uci set mmpbxrvsipnet.sip_net.interface6='lan6'
uci set mmpbxrvsipnet.sip_net_1.interface='lan'
uci set mmpbxrvsipnet.sip_net_1.interface6='lan6'
uci commit
/etc/init.d/nginx restart
```

## Speeding up VDSL sync times

!!! note "Firmware 16.3"
    Firmware version 16.3.x works the best in terms of xDSL sync and compatibility. Use if available

If you're on VDSL you may be able to speed up your sync times by removing redundant DSL profiles so the integrated Gateway does not even try to use them.

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

## Turning off Power-Saving features

In theory, by turning off all power-saving features, the gateway should be more responsive in every way. To do this

1. Log in via SSH to your gateway
2. Run these commands:

```bash
pwrctl config --cpuspeed 0
pwrctl config --wait off
pwrctl config --ethapd off
pwrctl config --eee off
pwrctl config --autogreeen off
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

## Using DGA0231's VDSL and 4G as multiple WAN interfaces 

Those who are using a modem in bridge mode would normally have all (or almost all) other features of the modem disabled or unused.  That is, they just want to bridge the VDSL connection to an Ethernet interface that their firewall/router connects to. However, the DGA0231 also has a 4G interface which could be utilised by the firwwall/router in a multi-wan (VDSL and 4G) configuration. You might also want to do this if you are not happy with native 4G failover in the modem, for example it does not cutover quickly enough, leaving long periods of no internet connectivity.

### Assumptions

1. Using a Technicolor DGA0231, although other modems should also work.  In this example the Telstra vaiant was used.
2. Ansuel GUI has been installed: https://github.com/Ansuel/tch-nginx-gui
3. The modem has been configured in bridge mode
4. The WAN connection is VDSL/DHCP with 4G, other modes like PPPoE should also work with a small modification to the config.

### Confirm bridge mode is working

You need to be sure bridge mode is configured and working correctly.  Configure your PC's Ethernet adaptor for DHCP and plug it  directly into onw of the modem's LAN ports.  If confiugred correctly you will get an IP address from your ISP.  

**Don't forget to reapply the static IP address on your PC so that you can continue to configure the modem**
    
!!! info "Turning on bridging with Ansuel GUI" 
The Ansuel GUI allows the modem to be configured into bridge mode, but unlile the native Telstra code, is not a one-step press "Bridge Mode" button. The advanatage is that it leaves much of the features intact and allows you to reverse it without doing a factory reset.

### Network Diagram

The following depicts what we are trying to achieve from a layer-3 networking porint of view.

**Diagram**

The diagram above shows the IP layer connections in green with the green circles representing IP addresses. The VDSL connection is bridged through the modem and is effectively invisible from an IP perspective.  On the 4G path the IP connection terminates on the router in the modem, which will create a double NAT path from your home network (firewall/router and DJA0231 modem). 

This example will allocate a dedicated LAN port 1 (eth0) for the bridged VDSL connection, while leaving the other ports on the existing LAN segment to allow connection to the modem as router hop on the 4G connection.  Note this is also the connection that you use to manage the modem as it terminates on an IP address in the modem.

### Disable `wansensing`
We need to stop the modem from detecting the WAN state which causes the 4G to be brought down if it detects the VDSL interface is up.

```
# Check status
/etc/init.d/wansensing enabled && echo on

# Stop service and confirm status
/etc/init.d/wansensing disable
/etc/init.d/wansensing enabled && echo on
```
### Enable `wwan`
`wwan` is the 4G interface which needs to be enabled. 

```
# Check status
uci show network.wwan.enabled

# Enable wwan
uci set network.wwan.enabled=1
uci show network.wwan.enabled
uci commit

# reload config files
/etc/init.d/network reload
```
### Change `/etc/config/network` 
Firstly LAN port 1 and the VDSL connection needs to be removed from the existing LAN. I used WinSCP to perform the modifications to `/etc/config/network`. Under the section `config interface 'lan'` remove the following lines:

```
    list ifname 'eth0'
    list ifname 'ptm0'
```

Now we need to add a new interface `vdslbr` for the bridged VDSL segement.  Add the following just after the `config interface 'lan'` section:

```
config interface 'vdslbr'
	option force_link '1'
	option type 'bridge'
	list ifname 'eth0'
	list ifname 'ptm0'
```

After saving `/etc/config/network` apply the new config with the following commands:

```
uci commit
/etc/init.d/network reload
```

### Update static routes
The modem (4G router) needs to know the existence of your downstream networks, otherwise it does not know how to get the packets back to your devices. This can be done via the *IP Extras* card in GUI.

- IP Extras
  - IPv4 Static Routes Configuration 
    - Press `Add new static IPv4 route` button
    - Enter the following values:
      - Destination: 192.168.0.0
      - Mask: 255.255.0.0
      - Gateway: 10.0.0.1
      - Metric: 1
      - Interface: LAN

 
