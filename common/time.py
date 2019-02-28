from datetime import datetime

def unix_time(dt):
  # 返回秒
  epoch = datetime.utcfromtimestamp(0)
  delta = dt - epoch
  return delta.total_seconds()


def unix_time_millis(dt):
  # 毫秒
  return int(unix_time(dt) * 1000.0)


def get_millis():
  # 从1970-01-01到现在过了多少毫秒
  return unix_time_millis(datetime.now())


def get_seconds():
  return get_millis() / 1000.0
