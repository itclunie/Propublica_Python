import requests, csv, os, sys, json, time


distPointsPath = os.path.abspath("pointPerDist/cds_w_points_final.csv")
with open(distPointsPath, 'r') as output:
    reader = csv.reader(output, lineterminator = '\n')
    next(reader, None)
    distPoints = list(reader)

cdAddressInfo = {}

countR = 0
for pnt in distPoints:
    state = pnt[5]
    cdAddressInfo[state] = []

for pnt in distPoints:
    countR = countR + 1

    r = requests.get("https://maps.google.com/maps/api/geocode/json?latlng=" + pnt[3] + ',' + pnt[4]) #do this in another script, add to csv cds_w_points_final
    adrsJSON = r.json()

    state = pnt[5]
    cd = pnt[1]

    print(state, cd)

    distAddress = adrsJSON['results'][0]['formatted_address']

    print(countR, '------' + distAddress)

    cdAddressInfo[state].append({'cd':cd, 'adrs':distAddress})

    time.sleep(.5)

    # if countR == 20:
    #     break

with open('cdAddressInfo.json', 'w') as outfile:
    json.dump(cdAddressInfo, outfile)



#         0    1  2   3   4   5
#pnt = state CD pop lat lng abrv


