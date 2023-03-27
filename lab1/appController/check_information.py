import os

import psutil
import platform
import subprocess


def check():
    os_info = platform.system() + ' ' + platform.release()

    cpu_info = f'{psutil.cpu_count(logical=True)} cores, load {psutil.cpu_percent()}%'

    ram_info = f'{psutil.virtual_memory().total / (1024 ** 3):.2f} Gb, load {psutil.virtual_memory().percent}%'

    disk_info = psutil.disk_usage('/')

    try:
        xprotect_info = 'Installed, Enable' if psutil.pid_exists(216) else 'Not set'
        xprotect_signature_info = 'Updated' if psutil.pid_exists(216) else 'Not updated'
    except psutil.NoSuchProcess:
        xprotect_info = 'Not set'
        xprotect_signature_info = 'Unable to verify'

    firewall_info = 'Enable' if psutil.pid_exists(159) else 'Disable'

    software_update_info = 'There are updates' if psutil.pid_exists(1366) else 'No updates required'

    system_information = {
        'OS': os_info,
        'CPU': cpu_info,
        'RAM': ram_info,
        'DiskTotal': disk_info.total,
        'DiskFree': disk_info.free,
        'Antivirus': xprotect_info,
        'Signa': xprotect_signature_info,
        'Firewall': firewall_info,
        'OSUpdate': software_update_info
    }

    return system_information


def check_file(path):
    file_stat = os.stat(path)
    file_name = os.path.basename(path)
    file_owner = file_stat.st_uid
    filename = str(path)
    result = subprocess.run(["ls", "-l", filename], capture_output=True, text=True)
    file_version = result.stdout
    print(result.stdout)

    return {
        'file_name': file_name,
        'owner': file_owner,
        'version': file_version
    }
