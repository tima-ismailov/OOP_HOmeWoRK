import pytz
from datetime import datetime


now = datetime.now()

ny_tz = pytz.timezone("America/New_York")

ny_time = now.astimezone(ny_tz)

print("Local time:", now)  
print("New York time:", ny_time)  

