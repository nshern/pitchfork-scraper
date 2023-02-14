import helpers
from datetime import datetime
import os

file_name = f'{os.getcwd()}/data/{datetime.now().strftime("%H%M%S%f")}.csv'

l = helpers.get_album_links()

for i in l:
    with open(file_name, "a") as f:
        f.write(f"{i}\n")
