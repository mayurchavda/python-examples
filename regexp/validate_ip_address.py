import re

ips = ["10.10.10.10", "0.10.10.10", "10.10.10.310", "10.10.10", '99.15.1.1']

for ip in ips:
    host_bytes = ip.split('.')
    valid = [int(x) for x in host_bytes]
    valid = [x for x in valid if 0<= x <256]
    print(valid)

    isValid =  len(host_bytes) == 4 and len(valid) == 4
    print(isValid)

for ip in ips:

    if re.match(r'(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.'
                r'([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.'
                r'([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.'
                r'([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$',ip) != None:
        print("Verified as passed")
    else:
        print("Verified as failed")
