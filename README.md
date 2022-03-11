# scaleway-vpn-summoner

Quickly pop VPNs on your scaleway infrastructure

## Setup

```
➜  git clone --depth 1 https://github.com/senges/scaleway-vpn-summoner.git /opt/scaleway-vpn-summoner
➜  pip install --user -r /opt/scaleway-vpn-summoner/requirements.txt
➜  ln -s /opt/scaleway-vpn-summoner/spwn.py /usr/local/sbin/spwn
```

## Usage

* `configure` : first usage setup (API Token)
* `list` : list active VPN instances
* `new` : create new VPN instance
* `connect` : connect to one of VPN instance
* `describe` : describe VPN instance
* `destroy` : destroy VPN instance