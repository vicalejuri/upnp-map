upnp-map
========

This tool only feature is to open ports in the firewall via UPNP.
Tested on linux arch (2017), should work correctly on osx and windows.

# Usage

 ```upnp-map -h```
>
> usage: upnp-map [-h] [-action {open,close}] [-ports PORTS]
> 
> Punch a hole throught the firewall to this machine.
>
> optional arguments:
>
>  -h, --help            show this help message and exit
>
>  -action {open,close}
>
>  -ports PORTS          What ports to be mapped? format is LOCAL:REMOTE (Ex. 8000:80)
>


# Example

```$ upnp-map -ports 8000:80```

>
> INFO:root:Port Forward Attempt: Mapping http://80.202.10.40:80 --> http://192.168.0.60:8000 ... OK
>
