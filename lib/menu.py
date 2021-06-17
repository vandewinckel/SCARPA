import lib.tools.arpmon as arpmon
import lib.tools.user_agent_listener as uagent_l
import lib.tools.spotifydiscovery as spotifydiscovery
import lib.tools.icmplistener as icmplistener_call
import os

def options():
    print("""\u001b[0m
          [1] ARP RESPONSE LISTENER
          [2] ARP REQUEST LISTENER
          [3] USER AGENT LISTENER
          [4] SPOTIFY LISTENER
          [5] ICMP LISTENER
          """)

def disbatch(inp_file, n):
    def arpmonitor(inp_file):
        os.system('cls')
        os.system('mode con: cols=75 lines=40')
        arpmon.launch_response(inp_file)
        input("\n  [#] PRESS ENTER TO RETURN TO THE SELECTION MENU ...")
        return None
    
    def arprequester(inp_file):
        os.system('cls')
        os.system('mode con: cols=75 lines=40')
        arpmon.launch_requests(inp_file)
        input("\n  [#] PRESS ENTER TO RETURN TO THE SELECTION MENU ...")
        return None
    
    def agentlistener(inp_file):
        os.system('cls')
        os.system('mode con: cols=75 lines=40')
        uagent_l.launch_listener(inp_file)
        input("\n  [#] PRESS ENTER TO RETURN TO THE SELECTION MENU ...")
        return None
    
    def spotifylistener(inp_file):
        os.system('cls')
        os.system('mode con: cols=75 lines=40')
        spotifydiscovery.launch_listener(inp_file)
        input("\n  [#] PRESS ENTER TO RETURN TO THE SELECTION MENU ...")
        return None
    
    def icmplistener(inp_file):
        os.system('cls')
        os.system('mode con: cols=75 lines=40')
        icmplistener_call.launch_listener(inp_file)
        input("\n  [#] PRESS ENTER TO RETURN TO THE SELECTION MENU ...")
        return None
    
    case = {
        '1': arpmonitor,
        '2': arprequester,
        '3': agentlistener,
        '4': spotifylistener,
        '5': icmplistener
        }
    
    run = case.get(n)
    try:
        return run(inp_file)
    except TypeError:
        exit()

def main(inp_file, *args):
    if inp_file:
        print("  \u001b[1m\u001b[33;1m[-] STATIC ANALYSIS OPTIONS FOR",args[0])
        options()
        n = input(u"  \u001b[1m\u001b[33;1m[#] SELECT OPTION TO RUN: \u001b[0m")
        disbatch(inp_file, n)
    else:
        print("\n  \u001b[1m\u001b[33;1m[-] LIVE CAPTURE ANALYSIS OPTIONS")
        options()
        n = input(u"  \u001b[1m\u001b[33;1m[#] SELECT OPTION TO RUN: \u001b[0m")
        disbatch(inp_file, n)

if __name__ == '__main__':
    main()