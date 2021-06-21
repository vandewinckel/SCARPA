from scapy.all import *
import pandas as pd
import argparse

def launch_requests():
    parser = argparse.ArgumentParser(description='mac address listener')
    N = 0 #default count number unless specified
    T = 15 #default time in seconds unless specified
    L = None #default unless specified
    parser.add_argument("-c","--count", type=int, required=False)
    parser.add_argument("-t","--timer", type=int, required=False)
    parser.add_argument("-l","--listen", type=str, required=False)
    
    args = parser.parse_args()
    if args.count != None: N = args.count
    if args.timer != None: T = args.timer
    if args.listen != None: L = args.listen
    
    ARP_STOPPER = False
    ARP_SET = set()
    DF = pd.read_csv('macaddress-db.csv')

    def vendor(mac):
        valid_mac = mac[:8].upper()
        company_name = str(list(DF.loc[DF['oui'] == valid_mac]['companyName'])).replace("['",'').replace("']",'')
        origin_country = str(list(DF.loc[DF['oui'] == valid_mac]['countryCode'])).replace("['",'').replace("']",'')
        return (mac, company_name, origin_country)
    
    def stopfilter(x):
        if len(set(ARP_SET)) == int(N):
            return True
        else:
            return False
    
    def arpmonitor(pkt):
        if pkt[ARP].op == 1: #who-has (request)
            if str(pkt[ARP].hwsrc) not in ARP_SET and vendor(pkt[ARP].hwsrc)[1] != "Dell Inc":
                ARP_SET.add(str(pkt[ARP].hwsrc))
                mac_res = vendor(pkt[ARP].hwsrc)
                print(f"      \u001b[31;1mADDRESS : \u001b[0m{pkt[ARP].hwsrc} \u001b[33;1mis located at \u001b[0m{pkt[ARP].psrc}")
                print(f"      \u001b[31;1mRequest : \u001b[0m{pkt[ARP].psrc} \u001b[33;1mis asking about \u001b[0m{pkt[ARP].pdst}\n\t\t%s" % mac_res[1],mac_res[2])

    def arp_listen(pkt):
        if pkt[ARP].op == 1: #who-has (request)
            if str(pkt[ARP].hwsrc) not in ARP_SET:
                if L.upper() in vendor(pkt[ARP].hwsrc)[1].upper():
                    ARP_SET.add(str(pkt[ARP].hwsrc))
                    mac_res = vendor(pkt[ARP].hwsrc)
                    print(f"      \u001b[31;1mADDRESS : \u001b[0m{pkt[ARP].hwsrc} \u001b[33;1mis located at \u001b[0m{pkt[ARP].psrc}")
                    print(f"      \u001b[31;1mRequest : \u001b[0m{pkt[ARP].psrc} \u001b[33;1mis asking about \u001b[0m{pkt[ARP].pdst}\n\t\t%s" % mac_res[1],mac_res[2])

    
    def stats(arp_set):
        vendors = []
        for hwaddr in arp_set:
            vendors.append(str(vendor(hwaddr)[1]))
        return {i:vendors.count(i) for i in vendors}

    if N > 0:
        try:
            print('  \u001b[0m[~] Listening for',N,'ARP REQUESTS ...\n')
            sniff(prn=arpmonitor, filter="arp", store=0, stop_filter=stopfilter)
            print(f"\n  [@] VENDORS LIST IN SAMPLE SIZE\u001b[0m", N)
            vendr_dict = dict(stats(ARP_SET))
            for vendr in vendr_dict:
                print(f"      \u001b[33;1mVENDOR :\u001b[0m",vendr,vendr_dict[vendr])
        except Exception:
            print('\u001b[31;1m[CRITICAL FAULT] Quitting ...')
            
    elif L != None:
        try:
            print('  \u001b[0m[~] Listening for',L,'machines for',T,'SECONDS ...\n')
            sniff(prn=arp_listen, filter="arp", store=0, timeout=T)
        except Exception:
            print('\u001b[31;1m[CRITICAL FAULT] Quitting ...')
            
    elif T > 0:
        try:
            print('  \u001b[0m[~] Listening for',T,'SECONDS ...\n')
            sniff(prn=arpmonitor, filter="arp", store=0, timeout=T)
            print(f"\n  [@] VENDORS LIST IN SAMPLE SIZE\u001b[0m", len(list(ARP_SET)))
            vendr_dict = dict(stats(ARP_SET))
            for vendr in vendr_dict:
                print(f"      \u001b[33;1mVENDOR :\u001b[0m",vendr,vendr_dict[vendr])
        except Exception:
            print('\u001b[31;1m[CRITICAL FAULT] Quitting ...')
            

        
    
if __name__ == '__main__':
    launch_requests()