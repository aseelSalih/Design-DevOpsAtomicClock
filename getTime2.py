import ntplib
from time import *
from datetime import datetime

c = ntplib.NTPClient()
response = c.request('0.uk.pool.ntp.org', version=3)
ntp_time = datetime.strptime(ctime(response.tx_time), "%a %b %d %H:%M:%S %Y")
formatted_time = datetime.strftime(ntp_time, "%d-%m-%Y %H:%M:%S")
print(ctime(response.tx_time))
print('formatted time: ' + formatted_time)