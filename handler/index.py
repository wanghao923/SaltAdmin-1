#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KStudio
# 控制中心

import dmidecode
import tornado
import platform
import os
import psutil
from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth

def format_timestamp(s):
    s = int(float(s))
    D = 0
    H = 0
    M = 0
    S = s
    if S > 59:
        M = S / 60
        S = S % 60
        if M > 59:
            H = M / 60
            M = M % 60
            if H > 23:
                D = H / 24
                H = H % 24
    return "%d天%d小时%d分%d秒" % ( D, H, M, S )

class LocalInfo(object):
    def local_uptime(self):
        uptime = os.popen('uptime|awk -F"," \'{print $1$2}\'|awk -F"up" \'{print $2}\'')
        return uptime.read()

    def net_stat(self):
         net = {}
         f = open("/proc/net/dev")
         lines = f.readlines()
         f.close()
         i = 1
         for line in lines:
             if i < 3 :
                i += 1
                continue
             con = line.split(':')
             name = con[0].split()[0]
             var = con[1].split()
             net[name] = var
             i += 1
         return net
    def process_num(self):
        i = 0
        for j in os.listdir('/proc'):
            if j.isdigit():
                i += 1
        return i

    def login_user_num(self):
        p = os.popen('who | wc -l')
        return p.read().split()[0]

    def cpu_used(self):
        return "%.1f" % psutil.cpu_percent(0.1)

    def cpu_nums(self):
        cpu_physical_num = psutil.cpu_count(logical=False)
        cpu_logical_cores = psutil.cpu_count() # 返回CPU逻辑核数量
        return {'cpu_physical_num':cpu_physical_num, 'cpu_logical_cores':cpu_logical_cores}

    def manu(self):
        info = dmidecode.system()
        if len(info) > 0 :
            for i in info :
                try:
                    if info[i]['dmi_type'] == 1 :
                        Manufacturer = info[i]['data']['Manufacturer']
                        Product_Name = info[i]['data']['Product Name']
                except Exception,e:
                    print "Error: ",Exception,":",e
                    Manufacturer = 'General'
                    Product_Name = 'PC'
        else:
            Manufacturer = 'General'
            Product_Name = 'PC'
        m = {'Manufacturer':Manufacturer,'Product_Name':Product_Name}
        return m

Local = LocalInfo()

class IndexHandler(BaseHandler):

    # 获取系统信息
    def get_system_info(self):
        tornado_verion = tornado.version
        try:
            import salt.version
            salt_version = salt.version.__version__
        except:
            salt_version = 0

        r = os.popen("ip a | grep inet | grep -Ev 'inet6|127.0.0.1' | awk -F'[ /]+' '{print $3}'")
        r = r.read()
        ip = r.split()
        if len(ip) > 1:
            ip = ', '.join(ip)
        else:
            ip = ip[0]
        # Get OS
        os_info = os.popen("uname -a|awk \'{print $1,$3}\'").read()
        # get disk
        d = os.statvfs('/')
        da = d.f_frsize * d.f_blocks / 1024.0 / 1024 / 1024
        df = d.f_frsize * d.f_bavail / 1024.0 / 1024 / 1024
        du = ( d.f_blocks - d.f_bavail ) * d.f_frsize / 1024.0 / 1024 / 1024
        dp = ( d.f_blocks - d.f_bavail ) * 100 / float(d.f_blocks)
        #dp = d.f_bfree * 100 / float(d.f_blocks)
        da = "%.2f" % da
        df = "%.2f" % df
        du = "%.2f" % du
        dp = int(dp)
        # Get Loadavg
        f = open('/proc/loadavg')
        l = f.read().split()
        f.close()
        loadavg_1 = l[0]
        loadavg_5 = l[1]
        loadavg_15 = l[2]
        # Get Memory
        f = open('/proc/meminfo')
        m = f.readlines()
        f.close()
        mem = {}
        for n in m:
            if len(n) < 2 : continue
            name = n.split(':')[0]
            var = n.split()[1]
            mem[name] = int(var) / 1024
        mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
        # Get Net Stat
        net = Local.net_stat()
        net_in = 0
        net_out = 0
        for i in net:
            if i == 'lo':continue
            net_in += int(net[i][0])
            net_out += int(net[i][8])
        net_in = net_in / 1024 / 1024
        net_out = net_out / 1024 /1024

        manu = Local.manu()
        cpu_num = Local.cpu_nums()
        data = {
            'tornado': tornado_verion,
            'saltadmin': self.app_version,
            'saltstack': salt_version,
            'login_time': self.format_time(self.session.get('login_time')),
            'login_ip': self.session.get('login_ip'),
            'login_ua': self.session.get('login_ua'),
            #'uptime': format_timestamp(Local.local_uptime()),
            'uptime': Local.local_uptime(),
            'ip':ip,
            'hostname':platform.node(),
            'os':os_info,
            'disk_all':da,
            'disk_free':df,
            'disk_used':du,
            'disk_used_p':dp,
            'loadavg_1':loadavg_1,
            'loadavg_5':loadavg_5,
            'loadavg_15':loadavg_15,
            'salt_version':salt.version.__version__,
            'mem_total':mem['MemTotal'],
            'mem_free':mem['MemFree'],
            'mem_used':mem['MemUsed'],
            'mem_used_p':mem['MemUsed'] * 100 / mem['MemTotal'],
            'net_in':net_in,
            'net_out':net_out,
            'cpu_physical_num':cpu_num['cpu_physical_num'],
            'cpu_logical_cores':cpu_num['cpu_logical_cores'],
            'process_num':Local.process_num(),
            'login_user_num':Local.login_user_num(),
            'cpu_percent':Local.cpu_used(),
            'Manufacturer':manu.get('Manufacturer'),
            'Product_Name':manu.get('Product_Name'),
        }
        return data

    #@Auth
    def get(self):
        data = self.get_system_info()
        self.render('index/index.html',data=data)
