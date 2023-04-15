import datetime
import time
import ntplib

class NTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def get_nowtime(self):
        try:
            res = self.ntp_client.request(self.ntp_server_host)
            return datetime.datetime.strptime(time.ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")
        except Exception as e:
            raise Exception(e)
