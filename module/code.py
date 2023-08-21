import datetime
import pytz


def get_key():
    current_time = datetime.datetime.now()
    tz = pytz.timezone('Asia/Shanghai')
    current_time_gmt8 = current_time.astimezone(tz)
    formatted_time = current_time_gmt8.strftime('%Y-%m-%d-%H')

    split_parts = formatted_time.split("-")

    key1 = 1
    key2 = 0

    for i in split_parts:
        key1 = key1 * int(i)
        key2 = key2 + int(i)

    return key1 ^ key2
