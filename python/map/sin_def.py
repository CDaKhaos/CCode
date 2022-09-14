from datetime import date
import platform


def get_platfrom():
    str_sys = platform.system()
    if str_sys == 'Windows':
        return 'win'
    elif str_sys == 'Linux':
        str_mac = platform.machine()
        if str_mac == 'aarch64':
            return 'pad'
        elif str_mac == 'x86_64':
            return 'vm'
    else:
        return ''
    # return 'pad' 'vm' 'win'


def get_map_addr(file_name = 'map.html'):
    str_addr = ''
    str_pf = get_platfrom()
    if str_pf == 'win':
        str_addr = './'
    elif str_pf == 'vm':
        str_addr = './'
    elif str_pf == 'pad':
        str_addr = '../storage/shared/Documents/'
    else:
        return ''
    return str_addr + file_name


def get_file_addr(str_file_name, str_file_ex):
    today = date.today()
    str_file_name = '../storage/shared/Documents/%s%s.%s' % (
        str_file_name, today, str_file_ex)
    return str_file_name


if __name__ == '__main__':
    print(get_platfrom())
    print(get_map_addr())
