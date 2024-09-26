# FreePIE-to-opentrack-UDP
a TrackIR5 exporter for freepie to opentrack. useful for linux.







Additional config and diagnostics are in the script.
IP addresses can be changed from localhost to go over LAN or WAN for multi-pc setups
port is configurable but defaulted to 4242
optional output to FreePIE diagnostics window exists if desired for debugging




Special thanks to Raincoon for the setsockopt line of code for reusing existing sockets to make it work a lot better if restarting the program. Best QoL thing in the script.
