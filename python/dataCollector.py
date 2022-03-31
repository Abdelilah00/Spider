import psutil as psu


def collect():
    base_path = "/home/"
    users = psu.users()
    data = []
    #todo: https://psutil.readthedocs.io/en/latest/#psutil.process_iter
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


if __name__ == '__main__':
    print(psu.users() )
    print(psu.users() )
