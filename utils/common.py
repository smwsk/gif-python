import platform

def replace_path(path_name):
    if 'Windows' in platform.system():
        path_name = path_name.replace('/','\\')
    else:
        path_name = path_name.replace('\\','/')
    return path_name