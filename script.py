import calendar
import requests
import time
import math


# Create a plain text calendar
c = calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(2025, 1, 0, 0)
print(str)

warm_up = time.time()

variable = []
urls = [
    'http://manage-vagrant.fashion-ec.asia/brand/lip-service',
    'http://manage-vagrant.fashion-ec.asia/goods/lip-service/tops/0004523135607',
    'http://manage-vagrant.fashion-ec.asia/brand/lip-service',
    'http://manage-vagrant.fashion-ec.asia/goods/lip-service/jacket-outerwear/0004634515707',
    'http://manage-vagrant.fashion-ec.asia/brand/lip-service',
    'http://manage-vagrant.fashion-ec.asia/goods/lip-service/dress/0004623011307',
    'http://manage-vagrant.fashion-ec.asia/brand/lip-service',
    'http://manage-vagrant.fashion-ec.asia/goods/lip-service/skirt/0004632015907',
    'http://manage-vagrant.fashion-ec.asia/brand/lip-service',
    'http://manage-vagrant.fashion-ec.asia/',
    'http://manage-vagrant.fashion-ec.asia/brand/american-holic',
    'http://manage-vagrant.fashion-ec.asia/goods/american-holic/jacket-outerwear/h0184i30020.html',
    'http://manage-vagrant.fashion-ec.asia/goods/american-holic/jacket-outerwear/h0184i30014.html',
    'http://manage-vagrant.fashion-ec.asia/brand/american-holic',
    'http://manage-vagrant.fashion-ec.asia/goods/american-holic/dress/h0173h40030.html',
    'http://manage-vagrant.fashion-ec.asia/brand/american-holic',
    'http://manage-vagrant.fashion-ec.asia/goods/american-holic/jacket-outerwear/h0184i30020.html',
    'http://manage-vagrant.fashion-ec.asia/goods/american-holic/jacket-outerwear/h0184i30004.html',
    'http://manage-vagrant.fashion-ec.asia/',
    ]

print(variable)



# x = 1234.5678

# x = 1234.5678
# print(math.modf(x)) # (0.5678000000000338, 1234.0)
# print(x // 1) # (0.5678000000000338, 1234.0)
# print(x) # (0.5678000000000338, 1234.0)

# for url in urls:
#     print( url )

# for url in urls:
#     start_time = time.time()
#     r = requests.get(url)
#     print( ((time.time() - start_time) * 1000) // 1)

for url in urls:
    print( url )

for url in urls:
    start_time = time.time()
    r = requests.get(url).elapsed.total_seconds()
    print(r * 1000)
    time.sleep(0.1)
    # print( ((time.time() - start_time) * 1000) // 1)

