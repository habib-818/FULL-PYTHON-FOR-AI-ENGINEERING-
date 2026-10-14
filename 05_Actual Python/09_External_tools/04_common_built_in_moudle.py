from datetime import datetime
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

import os
current_dir = os.getcwd()
print(current_dir)