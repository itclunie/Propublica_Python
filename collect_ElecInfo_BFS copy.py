import requests, csv, os, sys, json

stateABRV = {
        "AL": {"name":"Alabama","cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "AK": {"name":"Alaska", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "AZ": {"name":"Arizona", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "AR": {"name":"Arkansas", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "CA": {"name":"California", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "CO": {"name":"Colorado", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "CT": {"name":"Connecticut", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "DE": {"name":"Delaware", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "FL": {"name":"Florida", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "GA": {"name":"Georgia", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "HI": {"name":"Hawaii", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "ID": {"name":"Idaho", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "IL": {"name":"Illinois", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "IN": {"name":"Indiana", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "IA": {"name":"Iowa", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "KS": {"name":"Kansas", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "KY": {"name":"Kentucky", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "LA": {"name":"Louisiana", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "ME": {"name":"Maine", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MD": {"name":"Maryland", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MA": {"name":"Massachusetts", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MI": {"name":"Michigan", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MN": {"name":"Minnesota", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MS": {"name":"Mississippi", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MO": {"name":"Missouri", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "MT": {"name":"Montana", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NE": {"name":"Nebraska", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NV": {"name":"Nevada", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NH": {"name":"New Hampshire", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NJ": {"name":"New Jersey", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NM": {"name":"New Mexico", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NY": {"name":"New York", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "NC": {"name":"North Carolina", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "ND": {"name":"North Dakota", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "OH": {"name":"Ohio", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "OK": {"name":"Oklahoma", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "OR": {"name":"Oregon", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "PA": {"name":"Pennsylvania", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "RI": {"name":"Rhode Island", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "SC": {"name":"South Carolina", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "SD": {"name":"South Dakota", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "TN": {"name":"Tennessee", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "TX": {"name":"Texas", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "UT": {"name":"Utah", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "VT": {"name":"Vermont", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "VA": {"name":"Virginia", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "WA": {"name":"Washington", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "WV": {"name":"West Virginia", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "WI": {"name":"Wisconsin", "cds":[], "Senators":[], "Governor":{}, "Others":[] },
        "WY": {"name":"Wyoming", "cds":[], "Senators":[], "Governor":{}, "Others":[] }
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