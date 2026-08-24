# Title: IEEE 1722 Examples

The commands need to be adjusted based on your environment. 

```
cd $HOME
git clone https://github.com/nayakned/scapy.git
cd scapy
git checkout add_proto/avtp
cd $HOME
git clone https://github.com/nayakned/scapy-ieee1722-examples.git
cd scapy-ieee1722-examples
sudo PYTHONPATH=$HOME/scapy python3 1722-example.py
```