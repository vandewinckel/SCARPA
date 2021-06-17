from scapy.all import *

def capture(n):
    print('  \u001b[0m[~] Sniffing',n,'Packets ...')
    pcap = sniff(count=n)
    print('  \u001b[0m[#] Capture Success',n,'Packets Captured!')
    print('  \u001b[32;1m[#] '+str(pcap).replace('<Sniffed: ','').replace('>','')+'\u001b[0m')
    return pcap
    
def capture_static(file_path,filter_):
    print('  \u001b[0m[~] Sniffing Packets From', file_path,'...')
    pcap = sniff(offline=file_path, filter=filter_, store=0)
    print('  \u001b[0m\u001b[32;1m[!] Capture successful!')
    print('  \u001b[0m[#] '+str(pcap).replace('<Sniffed: ','').replace('>','')+'\u001b[0m')
    return pcap