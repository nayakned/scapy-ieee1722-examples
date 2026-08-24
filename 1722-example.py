
from scapy.all import *
from scapy.contrib.ieee1722 import AvtpAcfCanHeader, AvtpTscfHeader, AvtpNtscfHeader

# Packet 1 - UDP + TSCFv0
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpTscfHeader(encapsulation_sequence_num=25, acf_tlv=acf_pkt)
pkt = Ether() / IP(dst="127.0.0.1") / UDP(sport=20000, dport=17220) / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")

# Packet 2 - UDP + NTSCFv0
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpNtscfHeader(encapsulation_sequence_num=3, acf_tlv=acf_pkt)
pkt = Ether() / IP(dst="127.0.0.1") / UDP(sport=20000, dport=17220) / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")

# Packet 3 - UDP + TSCFv1
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpTscfHeader(version=1, encapsulation_sequence_num=25, acf_tlv=acf_pkt)
pkt = Ether() / IP(dst="127.0.0.1") / UDP(sport=20000, dport=17220) / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")

# Packet 4 - UDP + NTSCFv1
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpNtscfHeader(version=1, encapsulation_sequence_num=3, acf_tlv=acf_pkt)
pkt = Ether() / IP(dst="127.0.0.1") / UDP(sport=20000, dport=17220) / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")


# Packet 5 - Ether + TSCFv0
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpTscfHeader(acf_tlv=acf_pkt)
pkt = Ether(type=0x22F0) / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")
 
# Packet 6 - Ether + NTSCFv0
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03\x04\x05"
)
cf_pkt = AvtpNtscfHeader(version=0, acf_tlv=[acf_pkt, acf_pkt, acf_pkt])
pkt = Ether(type=0x22F0) / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")

# Packet 7 - Ether + TSCFv1
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpTscfHeader(version=1, encapsulation_sequence_num=25, acf_tlv=acf_pkt)
pkt = Ether() / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")

# Packet 8 - Ether + NTSCFv1
acf_pkt = AvtpAcfCanHeader(can_bus_id=0x14, can_identifier=0x45) / Raw(
    load="\x01\x02\x03"
)
cf_pkt = AvtpNtscfHeader(version=1, encapsulation_sequence_num=3, acf_tlv=acf_pkt)
pkt = Ether() / cf_pkt
pkt.show2()
sendp(pkt, iface="lo")

