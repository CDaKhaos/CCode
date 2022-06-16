from datetime import date

today = date.today()

def sin_get_file_addr(str_file_name, str_file_ex):
    str_file_name = '../storage/shared/Documents/%s%s.%s' % (str_file_name, today, str_file_ex)
    return str_file_name
