import power
import gi

from gi.repository import Notify

gi.require_version('Notify', '0.7')
Notify.init("Charging Status")

source = power.PowerManagement().get_providing_power_source_type()

if source == power.POWER_TYPE_BATTERY:
    notification = Notify.Notification.new('WARNING - Laptop running on battery!')
    notification.show()
