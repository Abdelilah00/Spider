import psutil as psu


def test():
    path = "/home/alexis"
    info = {
        'user': psu.users(),
        'storage': round(psu.disk_usage(path).used / (1024 ** 3), 2),
        'cpu': psu.cpu_percent(2),
        'memory': psu.virtual_memory().percent
    }
    print(info)


if __name__ == '__main__':
    test()
