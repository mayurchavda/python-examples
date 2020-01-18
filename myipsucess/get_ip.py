import re

ifconfig = '''eth0      Link encap:Ethernet  HWaddr 08:00:27:9a:c7:c8  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fe9a:c7c8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2246 errors:0 dropped:0 overruns:0 frame:0
          TX packets:923 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2282872 (2.2 MB)  TX bytes:69164 (69.1 KB)
'''


p = re.compile(r'\b\d+(?:\.\d+){3}\b', re.MULTILINE)
test_str = u"eth0      Link encap:Ethernet  HWaddr 00:18:F3:BE:18:1E\n          inet addr:192.168.10.15  Bcast:192.168.10.255  Mask:255.255.255.0\n          inet6 addr: fe80::218:f3ff:febe:181e/64 Scope:Link\n          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1\n          RX packets:39456 errors:0 dropped:0 overruns:0 frame:0\n          TX packets:45730 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:1000\n          RX bytes:25457904 (24.2 Mb)  TX bytes:6540945 (6.2 Mb)\n          Interrupt:20\n\nlo        Link encap:Local Loopback\n          inet addr:127.0.0.1  Mask:255.0.0.0\n          inet6 addr: ::1/128 Scope:Host\n          UP LOOPBACK RUNNING  MTU:16436  Metric:1\n          RX packets:182 errors:0 dropped:0 overruns:0 frame:0\n          TX packets:182 errors:0 dropped:0 overruns:0 carrier:0\n          collisions:0 txqueuelen:0\n          RX bytes:12812 (12.5 Kb)  TX bytes:12812 (12.5 Kb)"
print(re.findall(p, ifconfig))
print(re.search(p, ifconfig).group())