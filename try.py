import pcapy
from struct import *
import csv


devices = pcapy.findalldevs()
# ind = devices.index('wlan0')
loopback = devices[devices.index('lo')]

# initialize global variables
finack_checker = False
breaker = False
total_bytes = 0
temp_time_g = 0
count = 0
temp_time_gl = 0
total_time = 0

# create live capture instance
cap  = pcapy.open_live(loopback, 1024, 1, 1)

while True:
    (header, payload) = cap.next()

    # Get timestamp to record time between each packets
    epoch, millisecond = header.getts()
    e_str, ms_str = str(epoch), str(millisecond)
    ems_str = e_str+'.'+ms_str
    ems_fl = float(ems_str)
    if count == 0:
        temp_time_g = ems_fl 
    temp_time_gl = ems_fl

    # Unpacking TCP packet
    tcp_header = unpack('!HHLLBBHHH', payload[34:54])
    source_port = tcp_header[0]
    destionation_port = tcp_header[1]
    sequence_number = tcp_header[2]
    acknowledgement_number = tcp_header[3]
    offset = tcp_header[4] >> 4
    reserved = tcp_header[4] & 0xF
    flags = tcp_header[5]

    C_W_R = flags >> 7
    ECN_echo = flags & 0x40
    ECN_echo >>= 6
    Urgent = flags & 0x20
    Urgent >>= 5
    Ack = flags & 0x10
    Ack >>= 4

    Push = flags & 0x8
    Push >>= 3
    Reset = flags & 0x4
    Reset >>= 2
    Sync = flags & 0x2
    Sync >>= 1
    Finish = flags & 0x1


    window = tcp_header[6]
    checksum = tcp_header[7]
    pointer = tcp_header[8]
    total_bytes+=offset

    if(Finish == 0 and Ack == 1):
        breaker = True
    else:
        breaker = False
    
    if (Finish == 1 and Ack ==1):
        finack_checker = True


    with open('log.csv', 'a') as csvf:
        writer = csv.writer(csvf, dialect= csv.excel)
        writer.writerow([ems_fl, source_port, destionation_port, sequence_number, acknowledgement_number, offset, C_W_R, ECN_echo, Urgent, Ack, Push, Reset, Sync, Finish, window, checksum, pointer])

    if (breaker == True and finack_checker == True):
        total_time = temp_time_gl - temp_time_g
        with open('log.csv', 'a') as csvf:
            writer = csv.writer(csvf, dialect= csv.excel)
            writer.writerow(['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', total_bytes])
            writer.writerow(['','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',total_time])

        break

    count+=1