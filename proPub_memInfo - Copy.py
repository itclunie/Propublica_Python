#roumanos: YgsKtATqn73bwDrv9ar1M3ElbWSKsjyY24dMWsgq
#mine: 9QhaTiNvHgaAMdXd8S8pE5kIeW1tBG8X7ucfOVtn
import datetime, json, os, time, sys, urllib, httplib2, requests

apiKey = '9QhaTiNvHgaAMdXd8S8pE5kIeW1tBG8X7ucfOVtn'

from congress import Congress, CongressError, NotFound, get_congress

congress = Congress(apiKey)


with open('H:\\Python\\senateJSON.json', encoding='utf-8') as data_file:
    senMembers = json.loads(data_file.read())
with open('H:\\Python\\houseJSON.json', encoding='utf-8') as data_file:
    houseMembers = json.loads(data_file.read())

	
congressFullMems = [[],[]]	#0=sen, 1=house


for membR in senMembers['results'][0]['members']:
	fullMem = congress.members.get(membR['id'])
	congressFullMems[0].append(fullMem)

# for membR in houseMembers['results'][0]['members']:
	# fullMem = congress.members.get(membR['id'])
	# congressFullMems[1].append(fullMem)

for item in congressFullMems[0]
	print item
sys.exit()
	
	
##member calls
# new = congress.members.new()
# out = congress.members.departing(chamber='house', congress=114)
# pelosi = congress.members.get('P000197')
# ri = congress.members.filter(chamber='senate', state='RI')
# introd = congress.bills.recent(chamber='house', congress=111, type='introduced')
# updated = congress.bills.recent(chamber='house', congress=111, type='updated')
# comparison = congress.members.compare("G000575", "D000624", "house", "votes", 114)

##committee calls
# HSIG = congress.committees.get('house', 'HSIG', 115) #committee_detail
# house = congress.committees.filter('house', 115) #committee_list

##bill calls
# latest = congress.bills.recent(chamber='house', congress=114, type='introduced')
# bills = congress.bills.by_member('L000287', 'introduced')
# hr21 = congress.bills.get('hr21', 115) #bill_detail
# hr2393 = congress.bills.subjects('hr2393', 114) #bill_subjects

##Nomination calls
# received = congress.nominations.filter('received', 114)
# withdrawn = congress.nominations.filter('withdrawn', 114)
# confirmed = congress.nominations.filter('confirmed', 114)
# updated = congress.nominations.filter('updated', 114)
# pn50 = congress.nominations.get('PN40', 115) #nomination_detail
# nom_votes = congress.votes.nominations(114)
# IL = congress.nominations.by_state('IL', 114) #noms / state

##vote calls
# jan = congress.votes.by_month('house', 2016, 1) #by month
# sept = congress.votes.by_range('house', datetime.date(2010, 9, 1), datetime.date(2010, 9, 30)) #range

# today = datetime.date.today()
# last_week = today - datetime.timedelta(days=7)
# congress.votes.by_range('house', today, last_week) #votes_by_reversed_range
# congress.votes.by_range('house', last_week, today)

# today = datetime.datetime.today()
# votes = congress.votes.today('house') #votes_today

# june14 = datetime.date(2010, 6, 14)
# votes = congress.votes.by_date('house', june14) #votes_by_date

# vote = congress.votes.get('senate', 17, 2, 114) #vote_rollcall
# missed = congress.votes.by_type('house', 'missed', 114) #votes_by_type