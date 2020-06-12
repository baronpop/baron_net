from subprocess import call , check_output
from optparse import OptionParser
import scapy.all as scapy
import socket ,sys ,time
from termcolor import colored
from re import search
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
    color = colored('[+] Changed Succssesfully', 'green' ,'on_blue' ,['bold'])
    print(color)
    #call('ifconfig '+interface+' | grep ether', shell=True)
    ifconfig_result = check_output(['ifconfig',interface]).decode()
    role = search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_result)
    print('Your New Mac : ',role.group(0))


def ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip
    
def arp():
    arp_request = scapy.arping(ar)
    print(ar)

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
        arp()

    else:
        invalid = colored('[!] Invalid Option', 'red')
        print(invalid)
        sys.exit()

