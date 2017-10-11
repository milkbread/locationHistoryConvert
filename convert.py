#!/usr/bin/python

from datetime import datetime
from simplejson import loads, dumps

england = []
with open('Standortverlauf.json', 'r') as _data:
    data = loads(_data.read())
    print len(data['locations'])
    for l in data['locations']:
        date = datetime.fromtimestamp(int(l['timestampMs'][:10]))
        # .strftime('%Y-%m-%d %H:%M:%S')
        if (date > datetime.strptime('2017-09-30 0:00', '%Y-%m-%d %H:%M') and
                date < datetime.strptime('2017-10-07 23:00', '%Y-%m-%d %H:%M')):
            print l
            geojsonFeature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(l['longitudeE7']) / 10000000, float(l['latitudeE7']) / 10000000]
                }
            };
            england.append(geojsonFeature)
print len(england)
with open('england.json', 'w') as out:
    result = {
        "type": "FeatureCollection",
        "features": england
    }
    out.write("var fc = %s" % dumps(result))

# 1507639201902
