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
        return (datetime.now() - self.start_time).total_seconds()


class Rail_Line:
    length = None
    busy_flag = False
    speed_train = 0
    start_time = None

    def __init__(self, lenght) -> None:
        self.length = lenght

    def start_rail(self, speed, timer):
        if self.busy_flag == False and self.length > 0:
            self.busy_flag = True
            self.speed_train = speed
            self.start_time = timer.get_time()

    def on_exit_rail(self, timer):
        if self.busy_flag == True:
            if self.length // self.speed_train > timer.get_timer_value():
                self.busy_flag = False
                self.speed_train = 0


def main():
    rtc_time = RTC_Time()
    line = Rail_Line(300000)
    line.start_rail(3, rtc_time)
    while line.busy_flag:
        line.on_exit_rail(rtc_time)

    
if __name__ == '__main__':
    main()