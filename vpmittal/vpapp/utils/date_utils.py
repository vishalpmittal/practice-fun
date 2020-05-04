from datetime import datetime, timedelta, date
import pytz


def get_day_start_time(d):
    return d.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)


def get_day_end_time(d):
    return d.replace(hour=23, minute=59, second=59, microsecond=999999, tzinfo=pytz.UTC)


def get_datetime_from_string(date_str):
    return datetime.strptime(date_str[:26], '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=pytz.UTC)


def get_datetime_from_url_ts(url_ts):
    if not url_ts:
        return None, None
    try:
        ts = url_ts.split(',')
        from_ts = datetime.strptime(ts[0], '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        to_ts = datetime.strptime(ts[1], '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        to_ts = to_ts.replace(hour=23, minute=59,
                              second=59, microsecond=999999)
    except Exception as ex:
        return None, None

    return from_ts, to_ts


def get_previous_month(d):
    """
    replace date with 1st of the month. do a time delta of 1 day and get month
    :param d: datetime object
    :return: month number of previous month
    """
    return (d.replace(day=1) - timedelta(days=1)).month


def get_previous_year(d):
    """
    replace date with 1st of the month. do a time delta of 1 day and get month
    :param d:datetime object
    :return: year number of previous year
    """
    return (d.replace(month=1).replace(day=1) - timedelta(days=1)).year


def get_curr_date_str():
    """
    :return: today's date in format yyyy-mm-dd
    """
    return date.today().isoformat()


def get_curr_ts_str():
    """
    :return: current timestamp string upto seconds '2019-06-04T161544'
    """
    return datetime.today().isoformat().replace(':', '').split('.', 1)[0]


def get_curr_year():
    """
    return current year as integer
    """
    return int(date.today().year)
