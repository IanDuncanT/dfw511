import json
import dfw511

username = '<username>'
password = '<password>'

print('---------------------------------------------------------------------')
token = dfw511.auth(username, password)
with open('token.txt', 'w') as outfile:
    outfile.write(token)
print('Retrieved authentication token')
print('---------------------------------------------------------------------')
cameras = dfw511.getcctv(token)
with open('cctv.json', 'w') as outfile:
    json.dump(cameras, outfile)
print('Retrieved cctv data')
print('---------------------------------------------------------------------')
dms = dfw511.getdms(token)
with open('dms.json', 'w') as outfile:
    json.dump(dms, outfile)
print('Retrieved dms data')
print('---------------------------------------------------------------------')
event = dfw511.getevent(token)
with open('event.json', 'w') as outfile:
    json.dump(event, outfile)
print('Retrieved event data')
