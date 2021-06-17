from scapy.all import *
import time

def launch_listener(inp_file): 
    
    def uagent_l(pkt):
        if pkt[ICMP].type == 0:
            return f"      \u001b[32;1mICMP REP: \u001b[0m{pkt[IP].src} \u001b[33;1mreplying \u001b[0m{pkt[IP].dst}"
        if pkt[ICMP].type == 8:
            return f"      \u001b[31;1mICMP REQ: \u001b[0m{pkt[IP].src} \u001b[33;1mrequesting \u001b[0m{pkt[IP].dst}"
    
    if inp_file == False:
        N = input(u"  [#] ENTER LENGTH IN SECONDS TO RUN CAPTURE: ")
        print('  \u001b[0m[~] Listening for ICMP Packets ...\n')
        sniff(prn=uagent_l, filter='icmp', store=0, timeout=int(N))
        
if __name__ == '__main__':
    launch_listener(False)