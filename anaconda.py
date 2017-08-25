import os, subprocess

def shell(cmd):
    x = subprocess.check_output(cmd)
    return x

def by_lsb():
    command = ['lsb_release', '-as']
    output = shell(command).splitlines()
    print(output)
    return {
        'Distro': output[0],
        'Name': output[1],
        'Version': output[2],
        'Release': output[3]
    }

def by_uname():
    command = ['uname', '-a']
    output = str(shell(command)).split(' ')
    return {
        'OS': output[0],
        'Hostname': output[1],
        'Kernel': output[2],
        'Date': output[3:-4],
        'Arch': output[-2:-1]
    }

def by_whoami():
    command = ['whoami']
    output = shell(command)
    return {'User': output}

def anaconda():
    lsb_info = by_lsb()
    uname_info = by_uname()
    distro = lsb_info['Distro'].decode().lower()
    print(distro)
    with open('templates/%s.txt' % distro) as f:
        print('here')
        ascii_art = f.read()
        ascii_art = ascii_art.replace('%OS.NAME', lsb_info['Name'].decode())
        ascii_art = ascii_art.replace('%OS.VERSION', lsb_info['Version'].decode())
        ascii_art = ascii_art.replace('%OS.RELEASE', lsb_info['Release'].decode())



        print(ascii_art)
anaconda()