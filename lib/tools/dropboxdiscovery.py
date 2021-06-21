from scapy.all import *
import time

def launch_listener(inp_file):
    UAGENT_SET = set()    
    
    def uagent_l(pkt):
        if pkt.src not in UAGENT_SET:
            UAGENT_SET.add(pkt.src)
            return f"      \u001b[0m\u001b[33;1m{pkt[IP].src} has \u001b[34;1mDropbox \u001b[0m"
    
    if inp_file == False:
        N = input(u"  [#] ENTER LENGTH IN SECONDS TO RUN CAPTURE: ")
        print('  \u001b[0m[~] Listening for Dropbox users ...\n')
        sniff(prn=uagent_l, filter='port 17500 and udp', store=0, timeout=int(N))
        print('\n  \u001b[0m[!] FOUND\u001b[0m',len(UAGENT_SET),'USERS WITH DROPBOX AFTER LISTENING FOR',N,'SECONDS')
        
if __name__ == '__main__':
    launch_listener(False)