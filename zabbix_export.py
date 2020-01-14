#!/usr/bin/env python
from zabbix_api import ZabbixAPI
import time
import csv
from statistics import mean
import sys
from getpass import getpass

# API Connection
url = 'http://' + sys.argv[1]
username = sys.argv[2]
password = getpass("Password: ")
zapi = ZabbixAPI(server=url)
zapi.login(username, password)

# Today
current_timestamp = int(time.time())
# 90 days
from_timestamp = int(current_timestamp - 7776000)

# Zabbix Keys
items_keys = ['vm.memory.size[total]','vm.memory.size[free]','system.cpu.load[percpu,avg5]']

# Hosts (ALL)
hosts = zapi.host.get({})

""" Host filtering if needed
hosts = zapi.host.get({ "filter": {'host': host_name } }) """

def find_memcpu(hid, kname):
    try:
        itemvalue = zapi.item.get({ 'hostids': hid, 'search': {'key_': kname } })
        if len(itemvalue) == 1:
            # Collect trends
            item_trend = zapi.trend.get({ 'itemids': itemvalue[0]['itemid'], 'time_from': from_timestamp, 'time_till': current_timestamp })

            # Collects min, avg and max values.
            trend_max = [float(x['value_max']) for x in item_trend]
            trend_min = [float(x['value_min']) for x in item_trend]
            trend_avg = [float(x['value_avg']) for x in item_trend]
            
            # Output formatting
            if kname == 'vm.memory.size[free]' or kname == 'vm.memory.size[total]':
                print('{0};{1};{2};{3};{4};{5}'.format(host['host'], host['name'], kname, round(min(trend_min)/1024/1024/1024,1), round(mean(trend_avg)/1024/1024/1024,1), round(max(trend_max)/1024/1024/1024,1)))
            elif kname == 'system.cpu.load[percpu,avg5]':
                print('{0};{1};{2};{3};{4};{5}'.format(host['host'], host['name'], kname, round(min(trend_min),1), round(mean(trend_avg),1), round(max(trend_max),1)))
    # CTRL + C
    except KeyboardInterrupt:
        sys.exit('Exit.')
    except:
        print('{0};{1};{2}'.format(host['name'], kname, 'ERROR'))
    

def find_fs(iid, kname):
    try:
        if 'total' in kname or 'pfree' in kname:
            # Collects trends
            fs_trend = zapi.trend.get({ 'itemids': iid, 'time_from': from_timestamp, 'time_till': current_timestamp })
            
            # Collects min, avg and max values.
            trend_max = [float(x['value_max']) for x in fs_trend]
            trend_min = [float(x['value_min']) for x in fs_trend]
            trend_avg = [float(x['value_avg']) for x in fs_trend]

            # Output formatting
            if 'total' not in kname:
                print('{0};{1};{2};{3};{4};{5}'.format(host['host'], host['name'], kname, round(min(trend_min)), round(mean(trend_avg)), round(max(trend_max))))
            else:
                print('{0};{1};{2};{3};{4};{5}'.format(host['host'], host['name'], kname, round(min(trend_min)/1024/1024/1024,1), round(mean(trend_avg)/1024/1024/1024,1), round(max(trend_max)/1024/1024/1024,1)))
    # CTRL + C
    except KeyboardInterrupt:
        sys.exit('Exit.')
    except:
        print('{0};{1};{2}'.format(host['name'], kname, 'ERROR'))


# Execution
print("hostname;nome;metrica;minimo;medio;maximo")
for host in hosts:
    for key in items_keys:
        find_memcpu(host['hostid'],key)
    
    filesystems_wrk = zapi.item.get( {'hostids': host['hostid'], 'search': {'key_': 'vfs.fs.size'}, 'output': ['itemid','key_'] })
    for fsystem in filesystems_wrk:
        find_fs(fsystem['itemid'], fsystem['key_'])

