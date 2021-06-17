import pandas as pd

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

vendors = pd.read_csv('resources/macaddress-db.csv')

def vendor(df,mac):
    valid_mac = mac[:8].upper()
    company_name = str(list(df.loc[df['oui'] == valid_mac]['companyName'])).replace("['",'').replace("']",'')
    origin_country = str(list(df.loc[df['oui'] == valid_mac]['countryCode'])).replace("['",'').replace("']",'')
    return (mac, company_name, origin_country)