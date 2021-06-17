import subprocess

def nslookup(host):
    process = subprocess.Popen(["nslookup", host], stdout=subprocess.PIPE)
    output = process.communicate()[0]

    addr = (str(output).replace("b'",'').replace("'",'').replace(' ','').replace('\\r\\n',' ').split('  ')[0:-1])
    if len(addr) > 1:
        return str(addr[1:]).replace("['",'').replace("']",'')
    else:
        return host