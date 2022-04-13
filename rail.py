from datetime import timedelta
from datetime import datetime
from operator import length_hint

class RTC_Time:
    start_time = None

    def __init__(self) -> None:
        self.start_time = datetime.now()

    def get_time(self):
        return datetime.now()

    def get_timer_value(self):
        return datetime.now() - self.start_time


class Rail_Line:
    length = None
    busy_flag = False
    speed_train = 0
    start_time = None

    def __init__(self, lenght) -> None:
        self.length = lenght

    def start_rail(self, speed):
        if self.busy_flag == False and self.length > 0:
            self.busy_flag = True
            self.speed_train = speed

    def exit_rail(self):
        if self.busy_flag == True:
            self.busy_flag = False
    

    

