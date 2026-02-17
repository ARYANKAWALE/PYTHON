from datetime import datetime

now = datetime.now()               # Current date & time
print(now)                         # 2023-10-27 10:30:00.123456
print(now.year)                    # 2023
print(now.strftime("%d/%m/%Y"))    # Format: 27/10/2023