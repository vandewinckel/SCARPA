from scapy.all import *

def launch_listener(inp_file):
    UAGENT_SET = set()    
    
    def stopfilter(x):
        if len(set(UAGENT_SET)) == int(N):
            return True
        else:
            return False
    
    def uagent_l(pkt):
        for uagent_c in str(pkt.load).split('\\r\\n'):
            if uagent_c.startswith('USER-AGENT: '):
                if pkt.src not in UAGENT_SET:
                    UAGENT_SET.add(pkt.src)
                    return f"      \u001b[0m{pkt[IP].src} \u001b[33;1mhas user agent \u001b[0m%s" % uagent_c[12:]
    
    if inp_file == False:
        N = input(u"  [#] ENTER NUMBER OF USER AGENTS TO CAPTURE: ")
        print('  \u001b[0m[~] Listening for User Agents ...\n')
        sniff(prn=uagent_l, filter='port 1900 and udp', store=0, stop_filter=stopfilter)
        
if __name__ == '__main__':
    launch_listener(False)