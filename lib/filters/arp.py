from scapy.all import *
from lib.search import vendor, vendors

def filter_traffic(pcap):
    results = []
    for packet in pcap[ARP]:
        results.append((packet.psrc, vendor(vendors, packet.hwsrc)))
    return set(results)

def get_mac(pcap):
    for item in pcap:
        print('             '+item[0])
        print('    '+'  MAC ADDRESS :',item[1][0])
        print('    '+'       VENDOR :',item[1][1])
        print('    '+'VENDOR ORIGIN :',item[1][2])
        print('')