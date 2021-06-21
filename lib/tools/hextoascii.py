import argparse


def main():
    parser = argparse.ArgumentParser(description='Strategic Capture and Reconnaissance Packet Analyzer')
    parser.add_argument("-i","--input", type=str, required=False)
    
    args = parser.parse_args()
    if args.input != None: s = args.input
    
    #try:
    byte_s = bytes.fromhex(s)
    ASCII_S = byte_s.decode("ASCII")
    print(ASCII_S)
    #except Exception:
        #print('FAIL')
        
if __name__ == '__main__':
    main()
    
    