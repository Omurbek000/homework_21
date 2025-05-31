from datetime import datetime


def is_it_morning():
    return 5 <= datetime.now().hour < 12
