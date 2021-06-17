from scapy.all import *

def launch_response(inp_file):
    ARP_STOPPER = False
    ARP_SET = set()
    
    def stopfilter(x):
        if len(set(ARP_SET)) == int(N):
            return True
        else:
            return False
    
    def arpmonitor(pkt):
        if pkt[ARP].op == 2: #is-at (response)
            if str(pkt[ARP].hwsrc) not in ARP_SET:
                ARP_SET.add(str(pkt[ARP].hwsrc))
                return f"      \u001b[32;1mResponse : \u001b[0m{pkt[ARP].hwsrc} \u001b[33;1mhas address \u001b[0m{pkt[ARP].psrc}"
    
    if inp_file == False:
        N = input(u"  [#] ENTER NUMBER OF MAC ADDRESSES TO CAPTURE: ")
        print('  \u001b[0m[~] Listening for',N,'ARP Responces ...\n')
        sniff(prn=arpmonitor, filter="arp", store=0, stop_filter=stopfilter)

def launch_requests(inp_file):
    ARP_STOPPER = False
    ARP_SET = set()
    
    def stopfilter(x):
        if len(set(ARP_SET)) == int(N):
            return True
        else:
            return False
    
    def arpmonitor(pkt):
        if pkt[ARP].op == 1: #who-has (request)
            if str(pkt[ARP].hwsrc) not in ARP_SET:
                ARP_SET.add(str(pkt[ARP].hwsrc))
                return f"      \u001b[31;1mRequest : \u001b[0m{pkt[ARP].psrc} \u001b[33;1mis asking about \u001b[0m{pkt[ARP].pdst}"
    
    if inp_file == False:
        N = input(u"  [#] ENTER NUMBER OF ARP REQUESTS TO LISTEN FOR: ")
        print('  \u001b[0m[~] Listening for',N,'ARP REQUESTS ...\n')
        sniff(prn=arpmonitor, filter="arp", store=0, stop_filter=stopfilter)
    
if __name__ == '__main__':
    globals()[sys.argv[1]](False) #run from command-line "python arpmon.py <function>"