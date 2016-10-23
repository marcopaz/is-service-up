import sched
import time
from datetime import datetime, timedelta
from isserviceup.scripts.update_status import update_status

scheduler = sched.scheduler(timefunc=time.time)

UPDATE_INTERVAL = timedelta(seconds=10)


def truncate_time(t):
    return t.replace(second=0, microsecond=0)


def update():
    new_time = truncate_time(datetime.now()) + UPDATE_INTERVAL
    print('Update at ' + datetime.now().strftime('%Y-%m-%d %H:%M'))
    update_status()
    scheduler.enterabs(new_time.timestamp(), priority=0, action=update)

update()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped.')
