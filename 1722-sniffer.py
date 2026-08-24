

#from modules.AVTPpy import AVTP_Common, AVTP_ACF
from scapy.contrib.ieee1722 import AVTP_ACF_CAN_Header, AVTP_TSCF_Header, AVTP_NTSCF_Header
from scapy.all import *

def handle(pkt):
    pkt.show2()
    writer.write(pkt)

global writer
writer = PcapWriter("out.pcap", append=False, sync=True)
pkts = sniff(iface="lo", prn=lambda x: handle(x) if x.haslayer(AVTP_ACF_CAN_Header) or x.haslayer(AVTP_TSCF_Header) or x.haslayer(AVTP_NTSCF_Header) else None, timeout=5)
writer.close()
