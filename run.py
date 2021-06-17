import os, sys
import argparse

import lib.scarpa_banners as banner
import lib.tools.hasher as sha256
import lib.menu as menu

def is_valid_file(parser, arg):
    try:
        if not os.path.exists(arg):
            parser.error("The file %s does not exist!" % arg)
            sys.exit()
        else:
            return True
    except:
        return False

def base_menu(inp_file, input_path):
    os.system('mode con: cols=67 lines=25')
    print(banner.show_banner()[0])
    if inp_file == True:
        print(u"\n  [-] FILE   :", os.path.abspath(input_path))
        print(u"  [-] SHA256 :",sha256.hash(input_path))
        print(u"  [-] SIZE   :",int(os.path.getsize(input_path)/1024),"KB")
        if int(os.path.getsize(input_path)/1024) > 7500:
            print("  \u001b[31;1m[!] FILE EXCEEDED 7KB!\u001b[0m")
            print("  [-] Quitting SCARPA")
            sys.exit()
            try:
                print(u'\n  [~] Attempting to Load',input_path)
                menu.main(inp_file,input_path)
            except:
                print("  \u001b[31;1m[!] FILE IS NOT COMPATIBLE!\u001b[0m")
                print("  [-] Quitting SCARPA")
                sys.exit()
    else:
        menu.main(inp_file)
    

def main():
    parser = argparse.ArgumentParser(description='Strategic Capture and Reconnaissance Packet Analyzer')
    parser.add_argument("-i","--load", type=str, required=False)
    
    inp_file = False
    args = parser.parse_args()
    input_path = args.load 
    inp_file = is_valid_file(parser, input_path)
    
    try:
        while True:
            base_menu(inp_file, input_path)
    except KeyboardInterrupt:
        print('')
    
main()
    