from datetime import datetime


def time_now() -> str:
    return f"Сейчас время: {datetime.now().time()}"


print(time_now())
