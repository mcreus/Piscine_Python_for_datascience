import time
from datetime import datetime

# Récupération du temps actuel en secondes depuis le 1er janvier 1970 (timestamp)
before_date = time.time()

# Conversion du timestamp en date
formatted_date = f"{before_date:.2e}"

# Récupération et formatage de la date actuelle
actual_date = datetime.now().strftime("%b %d %Y")

# Impression des résultats
print(f"Seconds since January 1, 1970: {before_date} or {formatted_date} in scientific notation \n {actual_date}")
