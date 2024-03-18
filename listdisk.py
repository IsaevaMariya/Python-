#import psutil
#def makelistdisk():
#	return(psutil.disk_partitions())

#res=makelistdisk()
#print(res)
import os
import json
import psutil
from platform import uname

def correct_size(bts, ending='iB'):
    size = 1024
    for item in ["", "K", "M", "G", "T", "P"]:
        if bts < size:
            return f"{bts:.2f}{item}{ending}"
        bts /= size

def creating_file():
    collect_info_dict = dict()
    if 'info' not in collect_info_dict:
        collect_info_dict['info'] = dict()
        collect_info_dict['info']['system_info'] = dict()


#Диски
    for partition in psutil.disk_partitions():
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        if 'disk_info' not in collect_info_dict['info']:
            collect_info_dict['info']['disk_info'] = dict()
        if f"'device': {partition.device}" not in collect_info_dict['info']['disk_info']:
            collect_info_dict['info']['disk_info'][partition.device] = dict()
            collect_info_dict['info']['disk_info'][partition.device] = {'file_system': partition.fstype,
 'mountpoint':partition.mountpoint,                                                                       'size_total': correct_size(
                                                                            partition_usage.total),
                                                                        'size_used': correct_size(
                                                                            partition_usage.used),
                                                                        'size_free': correct_size(
                                                                            partition_usage.free),
                                                                        'percent':
                                                                            f'{partition_usage.percent}'}


    return collect_info_dict


def print_info(dict_info):
    for item in dict_info['info']:

        if item == "disk_info":
            for elem in dict_info['info'][item]:
                print(f"[+] Информация о дисках\n"
                      f"\t- Имя диска: {elem}\n"
                      f"\t- Файловая система: {dict_info['info'][item][elem]['file_system']}\n"
                      f"\t- Объем диска: {dict_info['info'][item][elem]['size_total']}\n"
                      f"\t- Занято: {dict_info['info'][item][elem]['size_used']}\n"
                      f"\t- Свободно: {dict_info['info'][item][elem]['size_free']}\n"
                      f"\t- Заполненность: {dict_info['info'][item][elem]['percent']}%\n")


def print_info2(dict_info):
 mass=list()
 m=list()
 for item in dict_info['info']:
  if item == "disk_info":
   for elem in dict_info['info'][item]:
    mass.append(elem)
    mass.append(dict_info['info'][item][elem]['size_total'])
    mass.append(dict_info['info'][item][elem]['file_system'])
    mass.append(dict_info['info'][item][elem]['mountpoint'])
   m.append(mass) 
 return m

def makelistdisk():
 dict_info = creating_file()
 a=print_info2(dict_info)
#        return print_info(dict_info)
 return a


print(makelistdisk())
#os.listmounts()
