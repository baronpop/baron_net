from subprocess import call
from optparse import OptionParser
import scapy.all as scapy
import socket ,sys ,time
from termcolor import colored
###################################

parser = OptionParser()
parser.add_option('-i','--interface',dest='interface',help='\t\t Set your interface')
parser.add_option('-m','--mac',dest='new_mac',help='\t\t Set your mac address')
parser.add_option('-a','--arp',dest='arp_request',help='\t\t Creates protocol ARP')

(options , args)= parser.parse_args()

interface = options.interface
nummac = options.new_mac
ar = options.arp_request


def mac():
    call('ifconfig '+interface+' down', shell=True)
    call('ifconfig '+interface+' hw ether '+nummac, shell=True)
    call('ifconfig '+interface+' up', shell=True)
    call('clear',shell=True)
    color = colored('\t[+] Changed Succssesfully', 'green' ,'on_yellow' ,['bold'])
    print(color)
    call('ifconfig '+interface+' | grep ether', shell=True)


def ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip
    
def arp():
    arp_request = scapy.arping(ar)


def arp2():
    arp_request = scapy.arping(input(str('Inter IP : ')))


###################################
if ar != None:
    arp()
    sys.exit()
elif interface != None:
    mac()
    sys.exit()

###################################
if interface == None:
    print('[+] Change Mac Press (1) > ')
    print('[+] To create a protocol ARP Press (2) > ')
    print('')
    butt = input('>>> ')
    time.sleep(1)
    print('===========================================')

    if butt == '1':
        interface = input('Inter You Inter face : ')
        nummac =input('Please put on the Mac : ')
        mac() 


    elif butt == '2':
        print('Your Local IP : '+ip())
        arp2()

    else:
        invalid = colored('[!] Invalid Option', 'red')
        print(invalid)
        sys.exit()
print('''
                   ===================================
                   |                                 |
                   |              BARON              |
                   |                                 |
                   ===================================
''')
