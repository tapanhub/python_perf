import datetime
import builtins as __builtin__
builtin_print = __builtin__.print


def time_print(*args, **kwargs):
    now = datetime.datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S] ")
    builtin_print(dt_string, *args, **kwargs)


__builtin__.print = time_print

print("hello world")
