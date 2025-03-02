import math
degrees=float(input())
time_1=12*60/360
minute=int(time_1*degrees)
hours=int(minute//60)
print(hours, minute%60)
