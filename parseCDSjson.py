import json

with open('8/cds115.geojson') as json_data:
    cdsJson = json.load(json_data)

for i in range(len(cdsJson['features'])):
    print(cdsJson['features'][i]['properties']['STATEFP'])
    

    
#{
#"type": "FeatureCollection",
#"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::4269" } },
#"features": [
#{ "type": "Feature", "properties": { "STATEFP": "02", "CD115FP": "00", "GEOID": "0200", "NAMELSAD": "Congressional District #(at Large)", "LSAD": "C1", "CDSESSN": "115", "MTFCC": "G5200", "FUNCSTAT": "N", "ALAND": 1477946266785, "AWATER": #245390495931, "INTPTLAT": "+63.3461909", "INTPTLON": "-152.8370690" }, "geometry": { "type": "MultiPolygon", "coordinates": #[ [ [ [ 179.388742, 51.941917 ], [ 179.404562, 51.968358 ], 