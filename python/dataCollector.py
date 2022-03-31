import psutil as psu


def collect():
    base_path = "/home/"
    users = psu.users()
    data = []
    for user in users:
        path = base_path + user.name
        info = {
            'storage': round(psu.disk_usage(path).used / (1024 ** 3), 2),
            'memory': psu.virtual_memory().percent,
            'cpu': psu.cpu_percent(2),
            'user': user.name
        }
        data.append(info)
    return data
