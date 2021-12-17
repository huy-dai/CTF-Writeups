#!/usr/bin/env python3
from scapy.all import *
import base64

# See: https://stackoverflow.com/questions/18256342/parsing-a-pcap-file-in-python
filename = 'constela.pcapng'

gps_coords = []
prefix = ""
last_packet = ""

# $GPGGA,,39.0,N,20.0,W,7,00,,10020.0,ft,,,,*47

cap = rdpcap(filename)
for packet in cap:
    # <CookedLinux  pkttype=unicast lladdrtype=0x304 lladdrlen=6 src='' proto=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=71 id=51338 flags=DF frag=0 ttl=64 proto=udp chksum=0x73e5 src=127.0.0.1 dst=127.0.0.53 |<UDP  sport=54772 dport=domain len=51 chksum=0xfe7a |<DNS  id=45248 qr=0 opcode=QUERY aa=0 tc=0 rd=1 ra=0 z=0 ad=1 cd=0 rcode=ok qdcount=1 ancount=0 nscount=0 arcount=1 qd=<DNSQR  qname='soundcloud.com.' qtype=A qclass=IN |> an=None ns=None ar=<DNSRROPT  rrname='.' type=OPT rclass=1200 extrcode=0 version=0 z=0 rdlen=None |> |>>>>
    if DNS in packet:
        target = packet.qd.qname.split(b'.')[0].decode("UTF8")
        # print(target)
        try:
            if 'MDAs' != target[0:4] and 'JEdQ' != target[0:4]:
                continue
            decode = base64.b64decode(target).decode("UTF8")
            # print(target, decode)
            if decode != last_packet:
                if decode[0:6] == "$GPGGA": #prefix
                    prefix = decode
                else: #suffix
                    assert(prefix is not None)
                    coordinate = prefix + decode
                    gps_coords.append(coordinate)
                    prefix = None
                    print(coordinate)
                last_packet = decode
        except:
            continue

    # print(type(packet))