import os, subprocess

def shell(cmd):
    x = subprocess.check_output(cmd).decode()
    return x

def get_lsb():
    command = ['lsb_release', '-as']
    output = shell(command).splitlines()
    return {
        'Distro': output[0],
        'Name': output[1],
        'Version': output[2],
        'Release': output[3]
    }
def get_uname():
    command = ['uname', '-a']
    output = shell(command).split(' ')
    return {
        'OS': output[0],
        'Hostname': output[1],
        'Kernel': output[2],
        'Date': output[3:-4],
        'Arch': output[-2:-1]
    }

def get_user():
    command = ['whoami']
    output = shell(command)
    return {'User': output}

def anaconda():
    lsb_info = get_lsb()
    uname_info = get_uname()
    distro = lsb_info['Distro'].lower()
    ascii_file = 'templates/%s.txt' % distro
    if not os.path.exists(ascii_file):
        ascii_file = 'templates/unknown.txt'
    with open(ascii_file) as f:
        ascii_art = f.read()
        ascii_art = ascii_art.replace('%OS.NAME', lsb_info['Name'])
        ascii_art = ascii_art.replace('%OS.VERSION', lsb_info['Version'])
        ascii_art = ascii_art.replace('%OS.RELEASE', lsb_info['Release'])
        ascii_art = ascii_art.replace('%USER', shell('whoami').strip())
        ascii_art = ascii_art.replace('%HOST', uname_info['Hostname'])
        print(ascii_art)
anaconda()