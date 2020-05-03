import esp32
import time
from ota_updater import OTAUpdater
import config

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/stlagger/unfassbar')
    o.download_and_install_update_if_available(config.SSID, config.PASS)    

def boot():
    download_and_install_update_if_available()
    start()
    
def start():
    print("start")
    


print("RUN")
boot()
