from datetime import datetime, date, timedelta

def get_days_from_today(input_date):
    try:
        delta = date.today() - datetime.strptime(input_date, "%Y.%m.%d").date()
        return delta.days
    except ValueError:
        print("Date format is invalid")
        return None
