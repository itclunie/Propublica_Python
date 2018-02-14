import requests, csv, os, sys, json

stateABRV = {
        "AL": {"name":"Alabama","cds":[], "Offices":[] },
        "AK": {"name":"Alaska", "cds":[], "Offices":[] },
        "AZ": {"name":"Arizona", "cds":[], "Offices":[] },
        "AR": {"name":"Arkansas", "cds":[], "Offices":[] },
        "CA": {"name":"California", "cds":[], "Offices":[] },
        "CO": {"name":"Colorado", "cds":[], "Offices":[] },
        "CT": {"name":"Connecticut", "cds":[], "Offices":[] },
        "DE": {"name":"Delaware", "cds":[], "Offices":[] },
        "FL": {"name":"Florida", "cds":[], "Offices":[] },
        "GA": {"name":"Georgia", "cds":[], "Offices":[] },
        "HI": {"name":"Hawaii", "cds":[], "Offices":[] },
        "ID": {"name":"Idaho", "cds":[], "Offices":[] },
        "IL": {"name":"Illinois", "cds":[], "Offices":[] },
        "IN": {"name":"Indiana", "cds":[], "Offices":[] },
        "IA": {"name":"Iowa", "cds":[], "Offices":[] },
        "KS": {"name":"Kansas", "cds":[], "Offices":[] },
        "KY": {"name":"Kentucky", "cds":[], "Offices":[] },
        "LA": {"name":"Louisiana", "cds":[], "Offices":[] },
        "ME": {"name":"Maine", "cds":[], "Offices":[] },
        "MD": {"name":"Maryland", "cds":[], "Offices":[] },
        "MA": {"name":"Massachusetts", "cds":[], "Offices":[] },
        "MI": {"name":"Michigan", "cds":[], "Offices":[] },
        "MN": {"name":"Minnesota", "cds":[], "Offices":[] },
        "MS": {"name":"Mississippi", "cds":[], "Offices":[] },
        "MO": {"name":"Missouri", "cds":[], "Offices":[] },
        "MT": {"name":"Montana", "cds":[], "Offices":[] },
        "NE": {"name":"Nebraska", "cds":[], "Offices":[] },
        "NV": {"name":"Nevada", "cds":[], "Offices":[] },
        "NH": {"name":"New Hampshire", "cds":[], "Offices":[] },
        "NJ": {"name":"New Jersey", "cds":[], "Offices":[] },
        "NM": {"name":"New Mexico", "cds":[], "Offices":[] },
        "NY": {"name":"New York", "cds":[], "Offices":[] },
        "NC": {"name":"North Carolina", "cds":[], "Offices":[] },
        "ND": {"name":"North Dakota", "cds":[], "Offices":[] },
        "OH": {"name":"Ohio", "cds":[], "Offices":[] },
        "OK": {"name":"Oklahoma", "cds":[], "Offices":[] },
        "OR": {"name":"Oregon", "cds":[], "Offices":[] },
        "PA": {"name":"Pennsylvania", "cds":[], "Offices":[] },
        "RI": {"name":"Rhode Island", "cds":[], "Offices":[] },
        "SC": {"name":"South Carolina", "cds":[], "Offices":[] },
        "SD": {"name":"South Dakota", "cds":[], "Offices":[] },
        "TN": {"name":"Tennessee", "cds":[], "Offices":[] },
        "TX": {"name":"Texas", "cds":[], "Offices":[] },
        "UT": {"name":"Utah", "cds":[], "Offices":[] },
        "VT": {"name":"Vermont", "cds":[], "Offices":[] },
        "VA": {"name":"Virginia", "cds":[], "Offices":[] },
        "WA": {"name":"Washington", "cds":[], "Offices":[] },
        "WV": {"name":"West Virginia", "cds":[], "Offices":[] },
        "WI": {"name":"Wisconsin", "cds":[], "Offices":[] },
        "WY": {"name":"Wyoming", "cds":[], "Offices":[] }
               }

countR = 0
cdCountR = 0
for state in stateABRV: #pulling each state"s CDs, putting into stateABRV
    countR = countR + 1
    print(countR, state)

    apiKey = "AIzaSyB8GawykpqPHCYiMNSk06tWAqYFRW-4XTk"
    cdsUrl = "https://www.googleapis.com/civicinfo/v2/divisions?query=" + state + "&alt=json&key=" + apiKey     #api to get state congressional dists
    stateUrl = "https://www.googleapis.com/civicinfo/v2/representatives/ocd-division%2Fcountry%3Aus%2Fstate%3A" + state.lower() + "?key=" + apiKey      #api to get state reps

    r = requests.get(cdsUrl) #GET request #1 congressional dists
    cdsJSON = r.json()

    for item in cdsJSON["results"]: #
        if "congressional district" in item["name"]:
            cdNum = item["ocdId"].split(":")

            cdInfoUrl = "https://www.googleapis.com/civicinfo/v2/representatives/ocd-division%2Fcountry%3Aus%2Fstate%3A" + state.lower() + "%2Fcd%3A" + cdNum[3] + "?key=" + apiKey
            r2 = requests.get(cdInfoUrl)
            cdRepsJSON = r2.json()

            stateABRV[state]["cds"].append({ cdNum[3]:cdRepsJSON })


    r3 = requests.get(stateUrl) #GET request #2 state reps
    stateRepsJSON = r3.json()


    othrOffices = stateRepsJSON['offices']
    nameAndOfficesIndx = []

    for i in range(len(othrOffices)): #get official's office indxs, append
        if othrOffices[i]['name'] == "United States Senate":
            nameAndOfficesIndx.append([othrOffices[i]['name'], othrOffices[i]['officialIndices'][0]])
            nameAndOfficesIndx.append([othrOffices[i]['name'], othrOffices[i]['officialIndices'][1]])
        else:
            nameAndOfficesIndx.append([othrOffices[i]['name'], othrOffices[i]['officialIndices'][0]])

    for office in nameAndOfficesIndx:  # use official's office indxs to append person info into stateABRV
        stateABRV[state]["Others"].append({
            'office': office[0],
            'Indx': office[1],
            'Info': stateRepsJSON["officials"][office[1]]
        })

    if countR == 3:
        break


with open('rep_&_cd_data.json', 'w') as outfile:
    json.dump(stateABRV, outfile)



#CD  https://www.googleapis.com/civicinfo/v2/representatives/ocd-division%2Fcountry%3Aus%2Fstate%3Aca%2Fcd%3A1?key=AIzaSyB8GawykpqPHCYiMNSk06tWAqYFRW-4XTk
#State  https://www.googleapis.com/civicinfo/v2/representatives/ocd-division%2Fcountry%3Aus%2Fstate%3Aca?key=AIzaSyB8GawykpqPHCYiMNSk06tWAqYFRW-4XTk