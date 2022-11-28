from ipware.ip import get_ip
ip = get_ip(request)
if ip is not None:
    print("찾았다")
else:
    print("못찾았다")