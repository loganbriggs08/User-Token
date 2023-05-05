import datetime

class Time:
    def seconds_since_epoch(year: int, month: int, day: int) -> int:
        start_date = datetime.datetime(year=year, month=month, day=day)
        current_date = datetime.datetime.now()

        time_diff = current_date - start_date
        total_seconds = time_diff.total_seconds()
        
        return int(total_seconds)