# -*- coding: utf-8 -*-

def print_logs(func, msg):
    print("[BEGIN LOGS '{}']{}".format(func.__name__, "=" * 20))

    print(msg)

    print("[END LOGS '{}']{}".format(func.__name__, "=" * 20))