import power
import time
import notify2 
from notify2 import Notification

notify2.init("Charger Warning")
n = Notification("WARNING", "Laptop running on battery. Plug in charger!")
n.set_urgency(notify2.URGENCY_CRITICAL)

while(True):
    source = power.PowerManagement().get_providing_power_source_type()

    if source == power.POWER_TYPE_BATTERY:
        n.show()
        print('NOT CHARGING!')
    else:
        print('CHARGING')
    time.sleep(300)

