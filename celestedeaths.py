import time
import xml.etree.ElementTree as ET
from os import path

savefile = "C:\Program Files (x86)\Steam\steamapps\common\Celeste\Saves\\1.celeste"
deathfilepath = "deaths.txt"

deathfile = open(deathfilepath, 'w')
previous_deaths = -1

while True:
    if not path.exists(savefile):
        deathfile.seek(0)
        deathfile.truncate(0)
        deathfile.write("")
        deathfile.flush()
        time.sleep(1)
        continue
    try:
        while True:
            root = ET.parse(savefile).getroot()
            death_node = root.find('TotalDeaths')
            deaths = death_node.text
            if previous_deaths != deaths:
                deathfile.seek(0)
                deathfile.truncate(0)
                deathfile.write(deaths)
                deathfile.flush()
                previous_deaths = deaths
            time.sleep(0.1)
    except Exception:
        pass
