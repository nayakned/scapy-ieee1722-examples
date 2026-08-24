
from scapy.contrib.ieee1722 import AvtpAcfCanHeader, AvtpAcfCanV2Header
from scapy.all import *

def handle(pkt):
    pkt.show2()
    writer.write(pkt)

global writer
writer = PcapWriter("out.pcap", append=False, sync=True)
pkts = sniff(iface="lo", prn=lambda x: handle(x) if x.haslayer(AvtpAcfCanHeader) or x.haslayer(AvtpAcfCanV2Header) else None, timeout=5)
writer.close()
