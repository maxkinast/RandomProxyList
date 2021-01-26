from requests import get
from bs4 import BeautifulSoup

def newProxyList(fileo=False, localip=False):
    URL = "https://free-proxy-list.net/"
    l = None
    m = get(URL)
    m = BeautifulSoup(m.content, "html.parser")
    m = m.find({"textarea":{"class": "form-control"}})
    m = str(m).split("\n")
    iplist = []
    for ip in m:
        #Nimmt alle strings mit Buchstaben raus
        if ip.lower().islower() == True:
            continue
        else:
            iplist.append(ip)

    #nimmt die local ip raus (local ip ist ein leerer string)
    if localip == False:
        iplist = iplist[+1:]

    #Fileoutput
    if fileo == True:
        l = open("temp_proxylist", "w")
        for ip in iplist:
            # damit datei nicht mit NEWLINE endet
            if ip == iplist[len(iplist) -1]:
                l.write(ip)
            else:
                l.write(ip + "\n")
        l.close()
    
    return iplist