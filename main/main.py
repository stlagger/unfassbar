import esp32
import time
from ota_updater import OTAUpdater
import config

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/stlagger/unfassbar')
    o.download_and_install_update_if_available(config.SSID, config.PASS)    
    o.check_for_update_to_install_during_next_reboot()

def boot():
    download_and_install_update_if_available()
    start()
    
def start():
    print("start")
    


print("RUN")
boot()
