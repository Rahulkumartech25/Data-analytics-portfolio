import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title="Water Drinking Reminder",
            message="Quick reminder, go hydrate 🥤💧 ",

            timeout=10
        )
        time.sleep(3600) # remind after every hour
        # time.sleep(5) # remind after every 5 sec for testing purpose

water_reminder()

