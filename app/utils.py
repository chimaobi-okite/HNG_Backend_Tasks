from datetime import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_utc_time_day():
    utc_time = datetime.utcnow()
    utc_time_formatted = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    day_int = datetime.utcnow().weekday()
    current_day = days[day_int]
    return utc_time_formatted, current_day