#!/usr/bin/env python
from zabbix_api import ZabbixAPI
from getpass import getpass
import time, csv, sys, json

# API Connection
url = 'https://monitoramento.eitisolucoes.com.br'
username = 'joao.foltran'
password = getpass("Password: ")
zapi = ZabbixAPI(server=url)
zapi.login(username, password)

group_name = 'MUELLER'
hostgroup = zapi.hostgroup.get({ "output": "extended", "sortfield": "name", "filter": { "name": group_name } })

zbx_inventory_fields = ['os']
zbx_group_id = hostgroup[0]['groupid']
hosts = zapi.host.get({ 'output': [ 'host' ], 'groupids': zbx_group_id, 'selectInventory': zbx_inventory_fields, 'searchInventory': { 'os': 'Windows' }, 'withInventory': 'true' })

print("HOST;OS")
for host in hosts:
    name = host['host']
    ops = str(host['inventory']).split(':')[1].split('}')[0]
    print('{0};{1}'.format(name, ops))