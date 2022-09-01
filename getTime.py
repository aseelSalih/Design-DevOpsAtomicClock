import socket
import struct
import sys
import time
from datetime import datetime


def RequestTimefromNtp(addr='0.uk.pool.ntp.org'):
    REF_TIME_1970 = 2208988800  # Reference time
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (addr, 123))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= REF_TIME_1970
    return time.ctime(t), t

if __name__ == "__main__":
    ntp_time = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    formatted_time = datetime.strftime(ntp_time, "%d-%m-%Y %H:%M:%S")
    print(RequestTimefromNtp())
    print('\tTime=%s' % time.ctime())
    print(formatted_time)

