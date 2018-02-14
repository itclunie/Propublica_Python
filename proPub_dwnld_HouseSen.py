#roumanos: YgsKtATqn73bwDrv9ar1M3ElbWSKsjyY24dMWsgq
#mine: 9QhaTiNvHgaAMdXd8S8pE5kIeW1tBG8X7ucfOVtn
import json, httplib2, requests


urlHouse = "https://api.propublica.org/congress/v1/115/house/members.json"
urlSenate = "https://api.propublica.org/congress/v1/115/senate/members.json"
apiKey = '9QhaTiNvHgaAMdXd8S8pE5kIeW1tBG8X7ucfOVtn'



#download all members JSON
response = requests.get(urlSenate, headers={'X-API-Key': apiKey})
parsed = json.dumps(response.json())
writeOut = open("H:\\Python\\senateJSON.json", 'w') 
writeOut.write(parsed)

response = requests.get(urlHouse, headers={'X-API-Key': apiKey})
parsed = json.dumps(response.json())
writeOut = open("H:\\Python\\houseJSON.json", 'w') 
writeOut.write(parsed)
