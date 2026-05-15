# Network Setup

The DVL has several services available over Ethernet:

* [Multicast DNS](#multicast-dns-mdns) (mDNS) for easy discovery
* Web GUI for live data, configuration, diagnostics, and software updates
* [TCP data stream](#tcp-data-stream)
* [Software updates](sw-update.md)

Use Ethernet for first setup whenever possible. It gives access to the web GUI, diagnostics, configuration, software updates, and the TCP data stream.

## Network configuration

### Multicast DNS (mDNS)

The DVL runs a DHCP client which attempts to obtain an IP address from a DHCP server on the same network, such as a router.

The DVL also supports mDNS. On a computer that supports mDNS, open the web GUI at:

```text
http://waterlinked-dvl
```

!!! note
    If no DHCP server is available on the network, use the [fallback IP](#fallback-ip) or configure a [static IP address](#via-the-gui). The DVL can spend up to 5 minutes searching for a DHCP server.

### Fallback IP

The DVL is always available with the static fallback IP address:

```text
192.168.194.95
```

To connect using the fallback IP:

1. Connect an Ethernet cable directly from the DVL to your computer.
2. Configure the computer Ethernet interface with a static IP address in the same subnet, for example `192.168.194.90` with subnet mask `255.255.255.0`.
3. Activate the Ethernet interface.
4. Open `http://192.168.194.95` in a web browser.

### Via the web GUI { #via-the-gui }

The DVL IP configuration can be changed in the web GUI:

* DHCP client: the DVL obtains an IP address from a DHCP server on the network.
* Static IP: the DVL uses a configured static IP address.

After changing the IP configuration, reboot the DVL for the settings to take effect.

!!! note
    Boot time depends on IP configuration. Using the fallback IP, boot time can be as much as 1 min 30 sec. With static IP, it can be as low as 20 sec.

## TCP data stream

The DVL can output data and receive commands over Transmission Control Protocol (TCP). A TCP server is available on port **16171**. It outputs the latest data to connected clients and listens for commands from connected clients.

See the DVL TCP JSON API for:

* [DVL A50/A125 TCP JSON API](dvl-json-protocol.md#json-protocol-tcp)
* [DVL A100/A250 TCP JSON API](dvl-a250_a100-json-protocol.md#json-protocol-tcp)
