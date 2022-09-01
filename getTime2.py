import ntplib
from datetime import datetime, timezone
c = ntplib.NTPClient()
# Provide the respective ntp server ip in below function
response = c.request('uk.pool.ntp.org', version=3)
response.offset
print (datetime.fromtimestamp(response.tx_time, timezone.utc))
